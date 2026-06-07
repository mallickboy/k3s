import os
import requests

BASE_URL = os.getenv("TARGET_API_URL", "http://localhost:3000")
DEBUG = os.getenv("DEBUG_TESTS") == "1"

def test_homepage_loads(log=False):
    res = requests.get(f"{BASE_URL}/")
    
    if log or DEBUG:
        print("Status Code: ", res.status_code)
        print("\nResponse Text: \n", res.text.lower())

    assert res.status_code == 200
    assert "html" in res.text.lower()