# main.py
from typing import List, Dict, Optional
from operations import (
    search_by_description,
    count_by_category,
    filter_by_status,
    sort_transactions,
    filter_by_currency
)


def get_user_input(prompt: str, options: Optional[List[str]] = None) -> str:
    
    while True:
        user_input = input(prompt).strip()
        if not options or user_input.lower() in [o.lower() for o in options]:
            return user_input
        print(f"Некорректный ввод. Допустимые варианты: {', '.join(options)}")


def print_transaction(transaction: Dict) -> None:

    date = datetime.fromisoformat(transaction['date']).strftime('%d.%m.%Y')
    description = transaction['description']
    amount = transaction['operationAmount']['amount']
    currency = transaction['operationAmount']['currency']['code']

    print(f"\n{date} {description}")
    if 'from' in transaction:
        print(f"{mask_sensitive_data(transaction['from'])} -> ", end='')
    print(mask_sensitive_data(transaction['to']))
    print(f"Сумма: {amount} {currency}")


def mask_sensitive_data(data: str) -> str:

    if data.startswith('Счет'):
        return f"Счет **{data[-4:]}"
    elif ' ' in data and len(data.split()[-1]) == 16:
        parts = data.split()
        number = parts[-1]
        return f"{' '.join(parts[:-1])} {number[:4]} {number[4:6]}** **** {number[-4:]}"
    return data


def main() -> None:
    """Основная логика программы."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")


    file_type = get_user_input(
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n",
        ['1', '2', '3']
    )

    file_types = {'1': 'JSON', '2': 'CSV', '3': 'XLSX'}
    print(f"\nДля обработки выбран {file_types[file_type]}-файл.")


    transactions = []


    status = get_user_input(
        "\nВведите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n",
        ['EXECUTED', 'CANCELED', 'PENDING']
    )
    transactions = filter_by_status(transactions, status)
    print(f"\nОперации отфильтрованы по статусу '{status}'")


    if get_user_input("\nОтсортировать операции по дате? (Да/Нет)\n", ['Да', 'Нет']) == 'Да':
        order = get_user_input(
            "Отсортировать по возрастанию или по убыванию? (возрастание/убывание)\n",
            ['возрастание', 'убывание']
        )
        transactions = sort_transactions(transactions, order == 'убывание')

    if get_user_input("\nВыводить только рублевые транзакции? (Да/Нет)\n", ['Да', 'Нет']) == 'Да':
        transactions = filter_by_currency(transactions, 'RUB')

    if get_user_input("\nОтфильтровать список транзакций по определенному слову в описании? (Да/Нет)\n",
                      ['Да', 'Нет']) == 'Да':
        search_word = input("Введите слово для поиска в описании: ")
        transactions = search_by_description(transactions, search_word)


    print("\nРаспечатываю итоговый список транзакций...")
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"\nВсего банковских операций в выборке: {len(transactions)}")
        for transaction in transactions:
            print_transaction(transaction)


if __name__ == "__main__":
    main()