from test_1_home_page import test_homepage_loads
from test_2_api_response import test_search_returns_json
from test_3_structure_types import test_search_schema
from test_4_result_validation import test_relevance_multiple_queries

if __name__=="__main__":
    test_homepage_loads(log=True)
    test_search_returns_json(log=True)
    test_search_schema(log=True)
    test_relevance_multiple_queries(log=True)