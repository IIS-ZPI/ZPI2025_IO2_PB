import src.analysis as analysis


sample_rates = [
    {"mid": 1.0},
    {"mid": 2.0},
    {"mid": 2.0},
    {"mid": 1.5},
]


def test_analyze_sessions():
    up, down, same = analysis.analyze_sessions(sample_rates)

    assert up == 1
    assert down == 1
    assert same == 1


def test_calculate_statistics():
    stats = analysis.calculate_statistics(sample_rates)

    assert stats["median"] == 1.75
    assert stats["mode"] == 2.0
    assert isinstance(stats["std_dev"], float)
    assert isinstance(stats["variation"], float)


def test_create_currency_pair():
    first = [{"mid": 4.0}, {"mid": 6.0}]
    second = [{"mid": 2.0}, {"mid": 3.0}]

    result = analysis.create_currency_pair(first, second)

    assert result == [{"mid": 2.0}, {"mid": 2.0}]


def test_build_histogram():
    hist = analysis.build_histogram(sample_rates, number_of_bins=3)

    assert len(hist) == 3
    assert sum(h["count"] for h in hist) == 3
