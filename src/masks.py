# masks.py
import logging
from pathlib import Path

# Настройка логгера для модуля masks
masks_logger = logging.getLogger('masks')
masks_logger.setLevel(logging.DEBUG)

# Создаем папку logs, если ее нет
Path('logs').mkdir(exist_ok=True)

# Настройка обработчика файла
masks_file_handler = logging.FileHandler('logs/masks.log', mode='w')
masks_file_handler.setLevel(logging.DEBUG)

# Настройка форматера
masks_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
masks_file_handler.setFormatter(masks_formatter)

# Добавляем обработчик к логгеру
masks_logger.addHandler(masks_file_handler)


# Пример использования в функциях модуля
def mask_card_number(card_number: str) -> str:
    try:
        masks_logger.debug(f'Начало обработки номера карты: {card_number}')
        if len(card_number) != 16 or not card_number.isdigit():
            masks_logger.error('Некорректный номер карты')
            raise ValueError('Номер карты должен содержать 16 цифр')

        masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        masks_logger.info(f'Номер карты успешно замаскирован: {masked}')
        return masked
    except Exception as e:
        masks_logger.error(f'Ошибка при маскировании номера карты: {str(e)}')
        raise