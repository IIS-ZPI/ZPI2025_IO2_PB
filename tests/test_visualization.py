import src.visualization as viz


def test_display_histogram(mocker):
    hist = [{"interval": "0 1", "count": 2}]

    mock_show = mocker.patch("src.visualization.plt.show")

    viz.display_histogram(hist, "TEST")

    mock_show.assert_called_once()