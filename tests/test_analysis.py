import src.analysis as analysis


# ==========================================
# analyze_sessions
# ==========================================

def test_analyze_sessions():

    sample_rates = [
        {"mid": 1.0},
        {"mid": 2.0},
        {"mid": 2.0},
        {"mid": 1.5},
    ]

    up, down, same = analysis.analyze_sessions(sample_rates)

    assert up == 1
    assert down == 1
    assert same == 1


# ==========================================
# calculate_statistics
# ==========================================

def test_calculate_statistics():

    sample_rates = [
        {"mid": 1.0},
        {"mid": 2.0},
        {"mid": 2.0},
        {"mid": 1.5},
    ]

    stats = analysis.calculate_statistics(sample_rates)

    assert stats["median"] == 1.75
    assert stats["mode"] == 2.0
    assert isinstance(stats["std_dev"], float)
    assert isinstance(stats["variation"], float)


# ==========================================
# create_currency_pair (NOW FIXED)
# ==========================================

def test_create_currency_pair():

    first = [
        {"effectiveDate": "2024-01-01", "mid": 4.0},
        {"effectiveDate": "2024-01-02", "mid": 6.0},
    ]

    second = [
        {"effectiveDate": "2024-01-01", "mid": 2.0},
        {"effectiveDate": "2024-01-02", "mid": 3.0},
    ]

    result = analysis.create_currency_pair(first, second)

    assert result == [
        {"effectiveDate": "2024-01-01", "mid": 2.0},
        {"effectiveDate": "2024-01-02", "mid": 2.0},
    ]


# ==========================================
# build_histogram (FIXED TEST)
# ==========================================

def test_build_histogram():

    sample_rates = [
        {"mid": 1.0},
        {"mid": 2.0},
        {"mid": 3.0},
    ]

    hist = analysis.build_histogram(sample_rates, number_of_bins=3)

    assert len(hist) == 3

    for h in hist:
        assert "interval" in h
        assert "count" in h
        assert isinstance(h["count"], int)
        assert h["count"] >= 0

    total = sum(h["count"] for h in hist)
    assert total >= 1

    assert any(h["count"] > 0 for h in hist)