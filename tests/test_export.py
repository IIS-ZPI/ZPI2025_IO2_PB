import src.export as export


def test_export_session_analysis(tmp_path, mocker):

    filepath = tmp_path / "session.csv"

    mocker.patch(
        "src.export.os.path.join",
        return_value=str(filepath)
    )

    export.export_session_analysis(
        "session.csv",
        "USD",
        "30",
        10,
        5,
        2
    )

    assert filepath.exists()


def test_export_statistics(tmp_path, mocker):

    filepath = tmp_path / "statistics.csv"

    mocker.patch(
        "src.export.os.path.join",
        return_value=str(filepath)
    )

    export.export_statistics(
        "statistics.csv",
        "EUR",
        "90",
        {
            "median": 4.5,
            "mode": 4.4,
            "std_dev": 0.2,
            "variation": 5.0
        }
    )

    assert filepath.exists()


def test_export_histogram(tmp_path, mocker):

    filepath = tmp_path / "histogram.csv"

    mocker.patch(
        "src.export.os.path.join",
        return_value=str(filepath)
    )

    histogram = [
        {"interval": "0-10", "count": 5},
        {"interval": "10-20", "count": 3}
    ]

    export.export_histogram("histogram.csv", histogram)

    assert filepath.exists()