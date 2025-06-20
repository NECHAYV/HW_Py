# operations.py
import re
from collections import Counter
from typing import List, Dict, Optional
from datetime import datetime


def search_by_description(transactions: List[Dict], search_str: str) -> List[Dict]:
    
    pattern = re.compile(search_str, re.IGNORECASE)
    return [t for t in transactions if pattern.search(t.get('description', ''))]


def count_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:

    descriptions = [t.get('description', '').lower() for t in transactions]
    category_counts = Counter()

    for category in categories:
        category_lower = category.lower()
        category_counts[category] = sum(1 for desc in descriptions if category_lower in desc)

    return dict(category_counts)


def filter_by_status(transactions: List[Dict], status: str) -> List[Dict]:

    return [t for t in transactions if t.get('state', '').lower() == status.lower()]


def sort_transactions(transactions: List[Dict], reverse: bool = False) -> List[Dict]:

    return sorted(
        transactions,
        key=lambda x: datetime.fromisoformat(x['date']),
        reverse=reverse
    )


def filter_by_currency(transactions: List[Dict], currency: str = 'RUB') -> List[Dict]:

    return [
        t for t in transactions
        if t.get('operationAmount', {}).get('currency', {}).get('code', '').upper() == currency.upper()
    ]