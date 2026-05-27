import statistics


# ==========================================
# SESSION ANALYSIS
# ==========================================
def analyze_sessions(rates):

    up = 0
    down = 0
    same = 0

    for i in range(1, len(rates)):

        previous = rates[i - 1]["mid"]
        current = rates[i]["mid"]

        if current > previous:
            up += 1

        elif current < previous:
            down += 1

        else:
            same += 1

    return up, down, same


# ==========================================
# STATISTICS
# ==========================================
def calculate_statistics(rates):

    values = [r["mid"] for r in rates]

    median = statistics.median(values)

    try:
        mode = statistics.mode(values)
    except:
        mode = "No mode"

    std_dev = statistics.stdev(values)

    mean = statistics.mean(values)

    variation = (std_dev / mean) * 100

    return {
        "median": median,
        "mode": mode,
        "std_dev": std_dev,
        "variation": variation
    }


# ==========================================
# CREATE CURRENCY PAIR
# ==========================================
def create_currency_pair(first_rates, second_rates):

    pair_rates = []

    min_length = min(len(first_rates), len(second_rates))

    for i in range(min_length):

        pair_value = (
            first_rates[i]["mid"] /
            second_rates[i]["mid"]
        )

        pair_rates.append({
            "mid": pair_value
        })

    return pair_rates


# ==========================================
# BUILD HISTOGRAM
# ==========================================
def build_histogram(rates, number_of_bins=13):

    changes = []

    for i in range(1, len(rates)):

        previous = rates[i - 1]["mid"]
        current = rates[i]["mid"]

        changes.append(current - previous)

    minimum = min(changes)
    maximum = max(changes)

    bin_width = (maximum - minimum) / number_of_bins

    histogram = []

    start = minimum

    for i in range(number_of_bins):

        end = start + bin_width

        count = 0

        for change in changes:

            if i == number_of_bins - 1:

                if start <= change <= end:
                    count += 1

            else:

                if start <= change < end:
                    count += 1

        interval = (
            f"{start:.4f} "
            f"{end:.4f}"
        )

        histogram.append({
            "interval": interval,
            "count": count
        })

        start = end

    return histogram