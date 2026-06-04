import os
import requests

BASE_URL = "http://localhost:3000"
DEBUG = os.getenv("DEBUG_TESTS") == "1"

def test_search_returns_json(log=False):
    res = requests.get(f"{BASE_URL}/search?q=python array")

    assert res.status_code == 200

    # must be valid JSON
    data = res.json()

    if log or DEBUG:
        print(f"Repsonse Type: {type(data)}")
        print(f"Valid JSON: {isinstance(data, list)}")

    assert isinstance(data, list)