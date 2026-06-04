import re
from app.models.pinecone_db import query_pinecone
from app.config import PINECONE_NAMESPACE, PINECONE_RESPONSE_COUNT
from app.utils import MODEL, query_embedding, clean_and_normalize_text

# def clean_and_normalize_text(text: str):
#     """Lowercase, remove special chars, and normalize whitespace."""
#     text = text.lower()
#     text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
#     text = re.sub(r"\s+", " ", text).strip()
#     return text

# def query_embedding(query: str):
#     return MODEL.encode(query).tolist()

def search_pinecone_service(query, top_k=PINECONE_RESPONSE_COUNT):
    # vector = MODEL.encode(query).tolist()
    cleaned_text= clean_and_normalize_text(query)
    vector = query_embedding(cleaned_text)
    matches = query_pinecone(vector, top_k=top_k, namespace=PINECONE_NAMESPACE)
    
    # Remove deduplicate title
    seen = set()
    unique_res = []
    for r in matches:
        title = r['metadata']['title']
        if title not in seen:
            unique_res.append(r)
            seen.add(title)
    return unique_res

def format_results(obj):
    desc_list = obj['metadata']['desc'].split('|@|')
    desc = ' '.join(desc_list)
    return {
        'title': obj['metadata']['title'],
        'link': obj['metadata']['link'],
        'desc': desc
    }

def perform_search(query):
    try:
        objarray = search_pinecone_service(query)
        return [format_results(o) for o in objarray]
    except Exception as e:
        return {"error": str(e)}
