from unittest.mock import Mock
from src.utils import json_transactions


def test_json_transactions(test_json):
    test_way = r"data/operations.json"
    assert json_transactions(test_way) == test_json