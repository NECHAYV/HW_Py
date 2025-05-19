def filter_by_state(values: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список операций и фильтрует их по второму аргументу."""
    filtered_values = []
    for value in values:
        if value.get("state") == state:
            filtered_values.append(value)
    return filtered_values


def sort_by_date(values: list[dict], setting: bool = True) -> list[dict]:
    """Функция принимает список операций и сортирет их по дате операции."""
    sorted_values = sorted(values, key=lambda value: value["date"], reverse=setting)
    return sorted_values
