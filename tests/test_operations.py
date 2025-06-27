# test_operations.py
import pytest
from datetime import datetime
from operations import (
    search_by_description,
    count_by_category,
    filter_by_status,
    sort_transactions,
    filter_by_currency
)


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-01-01T12:00:00",
            "description": "Перевод организации",
            "operationAmount": {
                "amount": "100.00",
                "currency": {"code": "USD"}
            }
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2023-01-02T12:00:00",
            "description": "Перевод с карты на карту",
            "operationAmount": {
                "amount": "200.00",
                "currency": {"code": "RUB"}
            }
        }
    ]


def test_search_by_description(sample_transactions):
    result = search_by_description(sample_transactions, "перевод")
    assert len(result) == 2
    result = search_by_description(sample_transactions, "организации")
    assert len(result) == 1
    assert result[0]['id'] == 1


def test_count_by_category(sample_transactions):
    categories = ["Перевод", "Организации"]
    result = count_by_category(sample_transactions, categories)
    assert result == {"Перевод": 2, "Организации": 1}


def test_filter_by_status(sample_transactions):
    result = filter_by_status(sample_transactions, "EXECUTED")
    assert len(result) == 1
    assert result[0]['id'] == 1


def test_sort_transactions(sample_transactions):
    result = sort_transactions(sample_transactions)
    assert result[0]['id'] == 1
    assert result[1]['id'] == 2
    result = sort_transactions(sample_transactions, reverse=True)
    assert result[0]['id'] == 2


def test_filter_by_currency(sample_transactions):
    result = filter_by_currency(sample_transactions, "RUB")
    assert len(result) == 1
    assert result[0]['id'] == 2