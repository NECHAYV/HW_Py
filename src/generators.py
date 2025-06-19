# generators.py
from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:

    for transaction in transactions:
        yield transaction['description']


def card_number_generator(start: int, end: int) -> Iterator[str]:

    for number in range(start, end + 1):
        card_num = f"{number:016d}"
        yield f"{card_num[:4]} {card_num[4:8]} {card_num[8:12]} {card_num[12:16]}"