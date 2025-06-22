import pytest
from modules.processor import process_csv

def test_filter_equal():
    result = process_csv("tests/sample.csv", "brand=apple", None)
    assert len(result["data"]) == 4

def test_filter_greater():
    result = process_csv("tests/sample.csv", "price>1000", None)
    assert len(result["data"]) == 1

def test_aggregate_avg():
    result = process_csv("tests/sample.csv", None, "price=avg")
    assert result["data"] == [[602.0]]

def test_invalid_filter():
    with pytest.raises(ValueError):
        process_csv("tests/sample.csv", "price<>100", None)

