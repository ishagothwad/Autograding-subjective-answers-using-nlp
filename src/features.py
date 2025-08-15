# src/features.py (part)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def tfidf_similarity(model_answer, student_answer, vectorizer=None):
    if vectorizer is None:
        vectorizer = TfidfVectorizer(ngram_range=(1,2))
    tfidf = vectorizer.fit_transform([model_answer, student_answer])
    sim = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return float(sim), vectorizer


from sentence_transformers import SentenceTransformer
import numpy as np

_model = None
def load_bert(model_name='all-MiniLM-L6-v2'):
    global _model
    if _model is None:
        _model = SentenceTransformer(model_name)
    return _model

def bert_similarity(model_answer, student_answer, model=None):
    model = model or load_bert()
    emb = model.encode([model_answer, student_answer])
    a, b = emb[0], emb[1]
    sim = float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))
    return sim


from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

def extract_keywords(text, top_k=6):
    vec = CountVectorizer(ngram_range=(1,2), stop_words='english').fit([text])
    # get top tokens by frequency (since single doc)
    tokens = vec.get_feature_names_out()
    counts = vec.transform([text]).toarray()[0]
    idx = np.argsort(counts)[::-1]
    top = []
    for i in idx:
        if counts[i] > 0:
            top.append(tokens[i])
        if len(top) >= top_k:
            break
    return top

def keyword_match_score(model_answer, student_answer, top_k=6):
    kw = extract_keywords(model_answer, top_k=top_k)
    sa = student_answer.lower()
    matched = sum(1 for w in kw if w.lower() in sa)
    score = matched / max(len(kw), 1)
    return score, kw, matched


import language_tool_python

_tool = None
def grammar_score(text):
    global _tool
    if _tool is None:
        _tool = language_tool_python.LanguageTool('en-US')
    matches = _tool.check(text)
    # naive scaling: more errors -> lower score
    errors = len(matches)
    max_errors = max(5, int(len(text.split())/5))   # heuristic
    s = max(0.0, 1 - (errors / max_errors))
    return s, errors
