# test_generators.py
import pytest
from generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100",
                "currency": {"code": "USD"}
            },
            "description": "Transaction 1"
        },
        {
            "id": 2,
            "operationAmount": {
                "amount": "200",
                "currency": {"code": "EUR"}
            },
            "description": "Transaction 2"
        },
        {
            "id": 3,
            "operationAmount": {
                "amount": "300",
                "currency": {"code": "USD"}
            },
            "description": "Transaction 3"
        }
    ]


def test_filter_by_currency(sample_transactions):
    # Тестируем фильтрацию USD
    usd_filter = filter_by_currency(sample_transactions, "USD")
    assert next(usd_filter)['id'] == 1
    assert next(usd_filter)['id'] == 3
    with pytest.raises(StopIteration):
        next(usd_filter)

    # Тестируем пустой результат
    empty_filter = filter_by_currency(sample_transactions, "GBP")
    with pytest.raises(StopIteration):
        next(empty_filter)


def test_transaction_descriptions(sample_transactions):
    desc_gen = transaction_descriptions(sample_transactions)
    assert next(desc_gen) == "Transaction 1"
    assert next(desc_gen) == "Transaction 2"
    assert next(desc_gen) == "Transaction 3"
    with pytest.raises(StopIteration):
        next(desc_gen)


@pytest.mark.parametrize("start,end,expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]),
    (9999999999999998, 9999999999999999, [
        "9999 9999 9999 9998",
        "9999 9999 9999 9999"
    ]),
])
def test_card_number_generator(start, end, expected):
    generator = card_number_generator(start, end)
    for expected_num in expected:
        assert next(generator) == expected_num
    with pytest.raises(StopIteration):
        next(generator)