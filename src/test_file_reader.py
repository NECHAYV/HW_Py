# test_file_reader.py
import pytest
from unittest.mock import patch, mock_open
import pandas as pd
from file_reader import read_csv_file, read_excel_file


@pytest.fixture
def sample_csv_data():
    return """id,amount,currency
1,100,USD
2,200,EUR
3,300,GBP"""


@pytest.fixture
def sample_excel_data(tmp_path):
    df = pd.DataFrame({
        'id': [1, 2, 3],
        'amount': [100, 200, 300],
        'currency': ['USD', 'EUR', 'GBP']
    })
    file_path = tmp_path / "test.xlsx"
    df.to_excel(file_path, index=False)
    return file_path


def test_read_csv_file_success(sample_csv_data):
    with patch('builtins.open', mock_open(read_data=sample_csv_data)):
        with patch('pandas.read_csv') as mock_read_csv:
            mock_read_csv.return_value = pd.DataFrame({
                'id': [1, 2],
                'amount': [100, 200],
                'currency': ['USD', 'EUR']
            })
            result = read_csv_file('dummy.csv')
            assert isinstance(result, list)
            assert len(result) == 2
            assert 'id' in result[0]


def test_read_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_csv_file('nonexistent.csv')


@patch('pandas.read_excel')
def test_read_excel_file_success(mock_read_excel, sample_excel_data):
    mock_read_excel.return_value = pd.DataFrame({
        'id': [1, 2],
        'amount': [100, 200],
        'currency': ['USD', 'EUR']
    })
    result = read_excel_file(sample_excel_data)
    assert isinstance(result, list)
    assert len(result) == 2
    assert 'id' in result[0]


def test_read_excel_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_excel_file('nonexistent.xlsx')