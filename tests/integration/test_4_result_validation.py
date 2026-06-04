import os
import requests

BASE_URL = "http://localhost:3000"
DEBUG = os.getenv("DEBUG_TESTS") == "1"

def check_relevance(query: str, min_match: float = 0.5, top_k: int = 5, log=False):
    query_words = set(query.lower().split())
    total_query_words = len(query_words)

    assert total_query_words > 0

    res = requests.get(f"{BASE_URL}/search", params={"q": query})
    assert res.status_code == 200

    data = res.json()
    top_results = data[:top_k]

    relevant_count = 0

    best_idx = -1
    best_ratio = 0.0
    best_title = ""

    for idx, item in enumerate(top_results):
        title_words = set(item["title"].lower().split())

        matched_words = len(query_words & title_words)
        match_ratio = matched_words / total_query_words

        if match_ratio > best_ratio:
            best_ratio = match_ratio
            best_idx = idx
            best_title = item["title"].strip()

        # rule 1: at least 1 word must match
        if matched_words < 1:
            continue

        # rule 2: fraction threshold
        if match_ratio >= min_match:
            relevant_count += 1
    if log or DEBUG:
        print(
            f"query='{query}' | "
            f"relevant={relevant_count}/{top_k} | "
            f"min_match={min_match} | "
            f"best_idx={best_idx} | "
            f"best_ratio={best_ratio:.2f} | "
            f"title={best_title[:60]}"
        )

    assert relevant_count >= 1, f"No relevant results for query: {query}"


def test_relevance_multiple_queries(log=False):
    QUERIES = [
        # Basic (5)
        "python variables",
        "python data types",
        "python for loop",
        "python functions",
        "python if else",

        # DSA (5)
        "python array",
        "python list vs tuple",
        "binary search python",
        "merge sort python",
        "python stack implementation",

        # Dev (5)
        "read csv file with python ",
        "save json file in python",
        "python http request",
        "python web scraping",
        "flask api example",

        # Advanced (5)
        "pandas dataframe tutorial",
        "numpy array operations",
        "python threading vs multiprocessing",
        "django",
        "memory management"
    ]

    for q in QUERIES:
        check_relevance(query= q, log= log)