import os
import requests
from typing import Dict, Optional
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rub(transaction: Dict) -> Optional[float]:

    if not transaction or 'operationAmount' not in transaction:
        return None

    amount_data = transaction['operationAmount']
    amount = float(amount_data['amount'])
    currency = amount_data['currency']['code']

    if currency == 'RUB':
        return amount

    if currency in ('USD', 'EUR'):
        rates = get_exchange_rates()
        if rates and currency in rates:
            return round(amount * rates[currency], 2)

    return None


def get_exchange_rates() -> Optional[Dict[str, float]]:


    if not API_KEY:
        return None

    try:
        response = requests.get(
            BASE_URL,
            params={'base': 'RUB', 'symbols': 'USD,EUR'},
            headers={'apikey': API_KEY},
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        # Инвертируем курсы, так как базовая валюта - RUB
        return {
            'USD': 1 / data['rates']['USD'],
            'EUR': 1 / data['rates']['EUR']
        }
    except (requests.RequestException, KeyError):
        return None