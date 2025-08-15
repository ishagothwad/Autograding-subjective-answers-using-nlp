# src/preprocess.py

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

_stop = set(stopwords.words('english'))
_lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = (text or "").lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def preprocess(text):
    text = clean_text(text)
    tokens = nltk.word_tokenize(text)
    tokens = [t for t in tokens if t not in _stop]
    tokens = [ _lemmatizer.lemmatize(t) for t in tokens ]
    return " ".join(tokens)
