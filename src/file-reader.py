# file_reader.py
import pandas as pd
from typing import List, Dict
import logging

# Настройка логгера
logger = logging.getLogger('file_reader')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('logs/file_reader.log', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
))
logger.addHandler(handler)


def read_csv_file(file_path: str) -> List[Dict]:

    try:
        logger.debug(f'Попытка чтения CSV файла: {file_path}')
        df = pd.read_csv(file_path)
        transactions = df.to_dict('records')
        logger.info(f'Успешно прочитано {len(transactions)} транзакций из CSV')
        return transactions
    except FileNotFoundError:
        logger.error(f'CSV файл не найден: {file_path}')
        raise
    except Exception as e:
        logger.error(f'Ошибка при чтении CSV: {str(e)}')
        raise ValueError(f'Ошибка обработки CSV файла: {str(e)}')


def read_excel_file(file_path: str) -> List[Dict]:

    try:
        logger.debug(f'Попытка чтения Excel файла: {file_path}')
        df = pd.read_excel(file_path)
        transactions = df.to_dict('records')
        logger.info(f'Успешно прочитано {len(transactions)} транзакций из Excel')
        return transactions
    except FileNotFoundError:
        logger.error(f'Excel файл не найден: {file_path}')
        raise
    except Exception as e:
        logger.error(f'Ошибка при чтении Excel: {str(e)}')
        raise ValueError(f'Ошибка обработки Excel файла: {str(e)}')