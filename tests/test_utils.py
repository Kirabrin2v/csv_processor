import pytest
from modules.utils import compare, aggregate_column


@pytest.mark.parametrize(
    "val,op,target,expected",
    [
        ("10", ">", "5",  True),
        ("10", "<", "5",  False),
        ("10", "==", "10", True),
        ("apple", "==", "apple", True),
        ("apple", "==", "banana", False),
    ],
)
def test_compare(val, op, target, expected):
    assert compare(val, op, target) is expected


def test_aggregate_avg():
    rows = [{"col": "1"}, {"col": "3"}, {"col": "5"}]
    assert aggregate_column(rows, "col", "avg") == 3.0


@pytest.mark.parametrize(
    "values,func,expected",
    [
        ([{"v": "2"}, {"v": "8"}], "min", 2.0),
        ([{"v": "2"}, {"v": "8"}], "max", 8.0),
    ],
)
def test_aggregate_min_max(values, func, expected):
    assert aggregate_column(values, "v", func) == expected


def test_aggregate_unsupported():
    with pytest.raises(ValueError):
        aggregate_column([{"v": "1"}], "v", "sum")

