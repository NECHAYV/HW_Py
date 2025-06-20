# Банковские транзакции

## Новые функции:

### Поиск транзакций
- `search_by_description(transactions, search_str)` - поиск по описанию (с использованием regex)
- `filter_by_status(transactions, status)` - фильтрация по статусу
- `filter_by_currency(transactions, currency)` - фильтрация по валюте

### Анализ транзакций
- `count_by_category(transactions, categories)` - подсчет операций по категориям
- `sort_transactions(transactions, reverse)` - сортировка по дате

### Основной интерфейс
Запуск: `python main.py`

Программа предоставляет интерактивный интерфейс для:
1. Выбора источника данных (JSON/CSV/XLSX)
2. Фильтрации по статусу
3. Сортировки по дате
4. Дополнительной фильтрации
5. Вывода результатов

## Тестирование
```bash
pytest --cov=operations --cov-report=html