# utils.py
import logging
from pathlib import Path

# Настройка логгера для модуля utils
utils_logger = logging.getLogger('utils')
utils_logger.setLevel(logging.DEBUG)

# Создаем папку logs, если ее нет
Path('logs').mkdir(exist_ok=True)

# Настройка обработчика файла
utils_file_handler = logging.FileHandler('logs/utils.log', mode='w')
utils_file_handler.setLevel(logging.DEBUG)

# Настройка форматера
utils_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
utils_file_handler.setFormatter(utils_formatter)

# Добавляем обработчик к логгеру
utils_logger.addHandler(utils_file_handler)

# Пример использования в функциях модуля
def example_utils_function():
    try:
        utils_logger.debug('Начало работы example_utils_function')
        # Код функции
        utils_logger.info('Функция example_utils_function выполнена успешно')
    except Exception as e:
        utils_logger.error(f'Ошибка в example_utils_function: {str(e)}')
        raise