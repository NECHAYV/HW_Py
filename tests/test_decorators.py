# test_decorators.py
import os
from decorators import log
import pytest


def test_log_to_console(capsys):

    @log()
    def add(a, b):
        return a + b

    result = add(1, 2)
    captured = capsys.readouterr()
    assert "add ok" in captured.out
    assert result == 3


def test_log_to_file(tmp_path):

    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def add(a, b):
        return a + b

    result = add(1, 2)
    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert "add ok" in content
    assert result == 3


def test_log_error_to_console (capsys):


    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out


def test_log_error_to_file(tmp_path):

    log_file = tmp_path / "test_error_log.txt"

    @log(filename=str(log_file))
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert "divide error: ZeroDivisionError" in content
    assert "Inputs: (1, 0), {}" in content


def test_log_preserves_function_metadata():


    @log()
    def sample_func(a: int, b: int) -> int:

        return a + b

    assert sample_func.__name__ == "sample_func"
    assert sample_func.__doc__ == "Sample function for testing."
    assert sample_func.__annotations__ == {"a": int, "b": int, "return": int}