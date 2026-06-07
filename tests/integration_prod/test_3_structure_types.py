import os
import requests

BASE_URL = os.getenv("TARGET_API_URL", "http://localhost:3000")
DEBUG = os.getenv("DEBUG_TESTS") == "1"

def test_search_schema(log= False):
    res = requests.get(f"{BASE_URL}/search?q=python array")
    data = res.json()

    assert len(data) > 0

    for item in data:
        assert isinstance(item, dict)

        assert "title" in item
        assert "link" in item
        assert "desc" in item

        assert isinstance(item["title"], str)
        assert isinstance(item["link"], str)
        assert isinstance(item["desc"], str)