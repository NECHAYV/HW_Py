import pytest
from unittest.mock import mock_open, patch
from src.utils.file_operations import read_json_file


@pytest.fixture
def sample_data():
    return [
        {"id": 441945886, "state": "EXECUTED"},
        {"id": 41428829, "state": "EXECUTED"}
    ]


def test_read_json_file_success(sample_data):
    json_data = '{"id": 441945886, "state": "EXECUTED"}'
    with patch("builtins.open", mock_open(read_data=json_data)):
        with patch("json.load", return_value=sample_data):
            result = read_json_file("dummy_path.json")
            assert len(result) == 2
            assert result[0]["id"] == 441945886


def test_read_json_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_json_file("nonexistent.json")
        assert result == []


def test_read_json_file_invalid_json():
    with patch("builtins.open", mock_open(read_data="invalid json")):
        result = read_json_file("invalid.json")
        assert result == []


def test_read_json_file_not_list():
    with patch("builtins.open", mock_open(read_data='{"key": "value"}')):
        with patch("json.load", return_value={"key": "value"}):
            result = read_json_file("not_list.json")
            assert result == []