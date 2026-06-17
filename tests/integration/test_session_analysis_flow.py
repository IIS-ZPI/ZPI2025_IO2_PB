import os
import csv

from src.api import get_currency_data
from src.analysis import analyze_sessions
from src.export import export_session_analysis


def test_session_analysis_export_flow(mocker):
    export_dir = os.path.join("..", "exports")
    os.makedirs(export_dir, exist_ok=True)

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "rates": [
            {"mid": 4.00},
            {"mid": 4.10},
            {"mid": 4.05},
            {"mid": 4.05}
        ]
    }

    mocker.patch(
        "src.api.requests.get",
        return_value=mock_response
    )

    rates = get_currency_data(
        "USD",
        "2025-01-01",
        "2025-01-10"
    )

    up, down, same = analyze_sessions(rates)

    filename = "integration_session_test.csv"

    export_session_analysis(
        filename,
        "USD",
        "10",
        up,
        down,
        same
    )

    filepath = os.path.join(export_dir, filename)

    assert os.path.exists(filepath)

    with open(filepath, newline="") as file:
        rows = list(csv.reader(file))

    assert rows[0] == [
        "Currency",
        "Period (days)",
        "Rising Sessions",
        "Falling Sessions",
        "Unchanged Sessions"
    ]

    assert rows[1] == [
        "USD",
        "10",
        str(up),
        str(down),
        str(same)
    ]

    os.remove(filepath)


def test_session_analysis_export_all_equal_values(mocker):
    export_dir = os.path.join("..", "exports")
    os.makedirs(export_dir, exist_ok=True)

    filename = "integration_session_equal_values.csv"
    filepath = os.path.join(export_dir, filename)

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "rates": [
            {"mid": 4.00},
            {"mid": 4.00},
            {"mid": 4.00},
            {"mid": 4.00}
        ]
    }

    mocker.patch(
        "src.api.requests.get",
        return_value=mock_response
    )

    rates = get_currency_data(
        "USD",
        "2025-01-01",
        "2025-01-10"
    )

    up, down, same = analyze_sessions(rates)

    export_session_analysis(
        filename,
        "USD",
        "10",
        up,
        down,
        same
    )

    assert up == 0
    assert down == 0
    assert same == len(rates) - 1

    assert os.path.exists(filepath)

    with open(filepath, newline="") as file:
        rows = list(csv.reader(file))

    assert rows[1] == [
        "USD",
        "10",
        "0",
        "0",
        str(len(rates) - 1)
    ]

    os.remove(filepath)
