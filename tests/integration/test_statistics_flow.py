import os
import csv

from src.menus import statistics_flow
from src.export import EXPORT_DIR


def test_statistics_flow_full_pipeline(mocker):

    filename = "stats_test.csv"
    filepath = os.path.join(EXPORT_DIR, filename)

    mocker.patch(
        "src.menus.get_available_currencies",
        return_value=["USD"]
    )

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "rates": [
            {"mid": 4.0},
            {"mid": 4.1},
            {"mid": 3.9}
        ]
    }

    mocker.patch(
        "src.api.requests.get",
        return_value=mock_response
    )

    mocker.patch(
        "builtins.input",
        side_effect=[
            "1",
            "3",
            "YES",
            "YES",
            filename
        ]
    )

    statistics_flow()

    assert os.path.exists(filepath)

    with open(filepath, newline="") as file:
        rows = list(csv.reader(file))

    assert rows[0] == [
        "Currency",
        "Period (days)",
        "Median",
        "Mode",
        "Standard Deviation",
        "Coefficient of Variation"
    ]

    assert rows[1][0] == "USD"
    assert rows[1][1] == "30"

    assert rows[1][2] != ""
    assert rows[1][4] != ""
    assert rows[1][5] != ""

    os.remove(filepath)
