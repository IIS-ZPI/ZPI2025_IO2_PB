import os
import csv
import src.export as export


def test_export_session_analysis():

    filename = "session.csv"
    export.export_session_analysis(
        filename,
        "USD",
        "30",
        10,
        5,
        2
    )

    filepath = os.path.join(export.EXPORT_DIR, filename)

    assert os.path.exists(filepath)

    with open(filepath, newline="") as file:
        rows = list(csv.reader(file))

    assert rows[0][0] == "Currency"


def test_export_statistics():

    filename = "statistics.csv"

    export.export_statistics(
        filename,
        "EUR",
        "90",
        {
            "median": 4.5,
            "mode": 4.4,
            "std_dev": 0.2,
            "variation": 5.0
        }
    )

    filepath = os.path.join(export.EXPORT_DIR, filename)

    assert os.path.exists(filepath)


def test_export_histogram():

    filename = "histogram.csv"

    histogram = [
        {"interval": "0-10", "count": 5},
        {"interval": "10-20", "count": 3}
    ]

    export.export_histogram(filename, histogram)

    filepath = os.path.join(export.EXPORT_DIR, filename)

    assert os.path.exists(filepath)