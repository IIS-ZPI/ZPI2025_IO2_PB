from src.utils import validate_date


def test_validate_date_valid():
    assert validate_date("2024-01-15") is True


def test_validate_date_invalid_format():
    assert validate_date("15-01-2024") is False


def test_validate_date_invalid_value():
    assert validate_date("2024-02-30") is False


def test_validate_date_empty_string():
    assert validate_date("") is False


def test_validate_date_none():
    assert validate_date(None) is False