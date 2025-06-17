import pytest
from datetime import datetime
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def sample_operations() -> list[dict]:
    return [
        {"state": "EXECUTED", "date": "2023-10-20T12:30:45.123"},
        {"state": "PENDING", "date": "2022-05-15T08:10:30.456"},
        {"state": "EXECUTED", "date": "2021-01-01T00:00:00.000"},
    ]

def test_filter_by_state(sample_operations: list[dict]) -> None:
    filtered = filter_by_state(sample_operations, "EXECUTED")
    assert len(filtered) == 2
    assert all(op["state"] == "EXECUTED" for op in filtered)

def test_sort_by_date(sample_operations: list[dict]) -> None:
    sorted_ops = sort_by_date(sample_operations)
    dates = [datetime.strptime(op["date"], "%Y-%m-%dT%H:%M:%S.%f") for op in sorted_ops]
    assert dates == sorted(dates, reverse=True)