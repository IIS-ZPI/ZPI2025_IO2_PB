import src.api as api


def test_get_available_currencies_success(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {"rates": [{"code": "USD"}, {"code": "EUR"}]}
    ]

    mocker.patch("src.api.requests.get", return_value=mock_response)

    result = api.get_available_currencies()

    assert result == ["EUR", "USD"]


def test_get_available_currencies_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 500

    mocker.patch("src.api.requests.get", return_value=mock_response)

    assert api.get_available_currencies() == []


def test_get_currency_data_success(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": [{"mid": 4.0}]}

    mocker.patch("src.api.requests.get", return_value=mock_response)

    result = api.get_currency_data("USD", "2024-01-01", "2024-01-10")

    assert result == [{"mid": 4.0}]


def test_get_currency_data_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 404

    mocker.patch("src.api.requests.get", return_value=mock_response)

    assert api.get_currency_data("USD", "2024-01-01", "2024-01-10") == []
