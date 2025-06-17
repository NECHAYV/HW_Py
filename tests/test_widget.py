import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize(
    "data, expected",
    [
        ("Карта 1234567890123456", "Карта 1234 56** **** 3456"),
        ("Счет 12345678", "Счет **5678"),
        ("Неизвестный формат", "Неизвестный формат"),
    ],
)
def test_mask_account_card(data: str, expected: str) -> None:
    assert mask_account_card(data) == expected

@pytest.mark.parametrize(
    "raw_date, expected",
    [
        ("2023-10-20T12:30:45.123", "20.10.2023"),
        ("2021-01-01T00:00:00.000", "01.01.2021"),
        ("invalid-date", "Некорректная дата"),
    ],
)
def test_get_date(raw_date: str, expected: str) -> None:
    assert get_date(raw_date) == expected