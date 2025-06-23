import pytest
from unittest.mock import patch, mock_open
import pandas as pd
from src.file_reader import read_csv, write_csv, read_excel, write_excel


# Тесты для CSV
def test_read_csv_with_reader():
    csv_content = """name;age
Alice;30
Bob;25"""

    with patch('builtins.open', mock_open(read_data=csv_content)):
        result = read_csv("dummy.csv", use_pandas=False)
        assert len(result) == 2
        assert result[0]["name"] == "Alice"


@patch('pandas.read_csv')
def test_read_csv_with_pandas(mock_read):
    mock_read.return_value = pd.DataFrame([{"name": "Alice", "age": 30}])
    result = read_csv("dummy.csv", use_pandas=True)
    assert len(result) == 1


# Тесты для Excel
@patch('pandas.read_excel')
def test_read_excel(mock_read):
    mock_read.return_value = pd.DataFrame([{"id": 1, "value": 100}])
    result = read_excel("dummy.xlsx")
    assert result[0]["id"] == 1


@patch('pandas.DataFrame.to_excel')
def test_write_excel(mock_write):
    data = [{"id": 1}, {"id": 2}]
    write_excel("output.xlsx", data)
    mock_write.assert_called_once()