# src/scoring.py
from src.features import tfidf_similarity, bert_similarity, keyword_match_score, grammar_score

def compute_score(model_answer, student_answer,
                  method='bert',
                  weights=None,
                  vectorizer=None):
    # weights: dict semantic, keyword, grammar
    if weights is None:
        weights = dict(semantic=0.6, keyword=0.3, grammar=0.1)

    if method == 'tfidf':
        semantic, vectorizer = tfidf_similarity(model_answer, student_answer, vectorizer)
    else:
        semantic = bert_similarity(model_answer, student_answer)

    key_score, keywords, matched = keyword_match_score(model_answer, student_answer, top_k=6)
    try:
        gscore, gerrors = grammar_score(student_answer)
    except Exception:
        # if grammar tool not available, set neutral
        gscore, gerrors = 0.7, None

    final = (weights['semantic'] * semantic) + \
            (weights['keyword'] * key_score) + \
            (weights['grammar'] * gscore)

    # scale to 0-10
    final_10 = round(final * 10, 2)
    return {
        'semantic': round(semantic, 3),
        'keyword_score': round(key_score, 3),
        'keywords': keywords,
        'matched': matched,
        'grammar_score': round(gscore, 3),
        'grammar_errors': gerrors,
        'final_score': final_10,
        'vectorizer': vectorizer
    }
