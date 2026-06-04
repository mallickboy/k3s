import re
from sentence_transformers import SentenceTransformer
from app.config import SENTENCE_TRANSFORMER_MODEL, MODEL_CACHE

MODEL = SentenceTransformer(SENTENCE_TRANSFORMER_MODEL, cache_folder=MODEL_CACHE)

def clean_and_normalize_text(text: str):
    """Lowercase, remove special chars, and normalize whitespace."""
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def query_embedding(query: str):
    return MODEL.encode(query).tolist()