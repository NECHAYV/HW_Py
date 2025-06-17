import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("", "Некорректный номер карты"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("12345678", "**5678"),
        ("987654", "**7654"),
        ("", "Некорректный номер счёта"),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected