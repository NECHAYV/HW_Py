from datetime import datetime
from typing import List, Dict

def filter_by_state(operations: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Фильтрует операции по статусу."""
    return [op for op in operations if op.get("state") == state]

def sort_by_date(operations: List[Dict], reverse: bool = True) -> List[Dict]:
    """Сортирует операции по дате (по умолчанию — от новых к старым)."""
    return sorted(
        operations,
        key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=reverse,
    )