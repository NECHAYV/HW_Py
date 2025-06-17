from datetime import datetime
from .masks import get_mask_card_number, get_mask_account

def mask_account_card(data: str) -> str:
    """Определяет тип данных (карта/счёт) и применяет маскировку."""
    if "счет" in data.lower():
        return f"Счет {get_mask_account(data.split()[-1])}"
    elif "карта" in data.lower():
        return f"Карта {get_mask_card_number(data.split()[-1])}"
    return "Неизвестный формат"

def get_date(raw_date: str) -> str:
    """Преобразует дату из 'YYYY-MM-DDTHH:MM:SS.SSS' в 'DD.MM.YYYY'."""
    try:
        date_obj = datetime.strptime(raw_date, "%Y-%m-%dT%H:%M:%S.%f")
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "Некорректная дата"