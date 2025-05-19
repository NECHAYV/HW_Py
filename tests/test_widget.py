import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "numbers_info, expected",
    [
        ("MIR 1596837868705199", "MIR 1596 83** **** 5199"),
        ("Master Card 6831982476737658", "Master Card 6831 98** **** 7658"),
        ("Visa 897304958f7290kj", "Error"),
        ("Visa 394075", "Error"),
        ("Счёт 73654108430135874305", "Счёт **4305"),
        ("Счет 19861059860492865092", "Счет **5092"),
        ("Счет saigq54298dfgjkh895h", "Error"),
        ("Счёт 23576908536", "Error"),
    ],
)
def test_mask_account_card(numbers_info, expected):
    assert mask_account_card(numbers_info) == expected


@pytest.mark.parametrize(
    "data_info, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2022-04-12T04:27:18.671407", "12.04.2022"),
        ("2014-03-11T02:26:18.", "Error"),
        ("2024-03-11T02:26:18.671407TR", "Error"),
        ("", "Error"),
    ],
)
def test_get_data(data_info, expected):
    assert get_date(data_info) == expected
