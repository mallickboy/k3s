from app.utils import clean_and_normalize_text

def test_lowercase():
    assert clean_and_normalize_text("Python") == "python"


def test_remove_special_chars():
    assert clean_and_normalize_text("python!!! \tarray???") == "python array"


def test_normalize_whitespace():
    assert clean_and_normalize_text(" python   \n\t array\t") == "python array"


def test_empty_string():
    assert clean_and_normalize_text("") == ""