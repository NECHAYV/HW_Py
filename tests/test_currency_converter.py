import pytest
from unittest.mock import patch, MagicMock
from src.external_api.currency_converter import convert_to_rub, get_exchange_rates


@pytest.fixture
def rub_transaction():
    return {
        "operationAmount": {
            "amount": "100.00",
            "currency": {"code": "RUB"}
        }
    }


@pytest.fixture
def usd_transaction():
    return {
        "operationAmount": {
            "amount": "10.00",
            "currency": {"code": "USD"}
        }
    }


@pytest.fixture
def eur_transaction():
    return {
        "operationAmount": {
            "amount": "5.00",
            "currency": {"code": "EUR"}
        }
    }


def test_convert_to_rub_rub(rub_transaction):
    assert convert_to_rub(rub_transaction) == 100.00


@patch('src.external_api.currency_converter.get_exchange_rates')
def test_convert_to_rub_usd(mock_rates, usd_transaction):
    mock_rates.return_value = {'USD': 75.0, 'EUR': 85.0}
    assert convert_to_rub(usd_transaction) == 750.0


@patch('src.external_api.currency_converter.get_exchange_rates')
def test_convert_to_rub_eur(mock_rates, eur_transaction):
    mock_rates.return_value = {'USD': 75.0, 'EUR': 85.0}
    assert convert_to_rub(eur_transaction) == 425.0


def test_convert_to_rub_invalid():
    assert convert_to_rub({}) is None
    assert convert_to_rub(None) is None


@patch('requests.get')
def test_get_exchange_rates_success(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "rates": {"USD": 0.013, "EUR": 0.011},
        "success": True
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    with patch.dict('os.environ', {'EXCHANGE_RATE_API_KEY': 'test_key'}):
        rates = get_exchange_rates()
        assert rates is not None
        assert 'USD' in rates
        assert 'EUR' in rates


@patch('requests.get')
def test_get_exchange_rates_failure(mock_get):
    mock_get.side_effect = Exception("API error")
    with patch.dict('os.environ', {'EXCHANGE_RATE_API_KEY': 'test_key'}):
        assert get_exchange_rates() is None