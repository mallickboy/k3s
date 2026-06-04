from app.utils import query_embedding

def test_query_embedding_returns_list():
    emb = query_embedding("python array")

    print(len(emb))

    assert isinstance(emb, list)
    assert len(emb) == 768      # 384 or 768 depending on model
    assert all(isinstance(x, float) for x in emb)