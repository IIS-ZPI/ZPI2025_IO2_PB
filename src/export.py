import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPORT_DIR = os.path.join(BASE_DIR, "exports")

os.makedirs(EXPORT_DIR, exist_ok=True)


# ==========================================
# SESSION ANALYSIS EXPORT
# ==========================================
def format_number(value):
    if isinstance(value, float):
        return f"{value:.3f}"
    return value

def export_session_analysis(
    filename,
    currency,
    period,
    rising,
    falling,
    unchanged
):


    filepath = os.path.join(EXPORT_DIR, filename)

    with open(filepath, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Currency",
            "Period (days)",
            "Rising Sessions",
            "Falling Sessions",
            "Unchanged Sessions"
        ])

        writer.writerow([
            currency,
            period,
            rising,
            falling,
            unchanged
        ])

    print("Session analysis exported successfully.")


# ==========================================
# STATISTICS EXPORT
# ==========================================
def export_statistics(
    filename,
    currency,
    period,
    stats
):
    filepath = os.path.join(EXPORT_DIR, filename)

    with open(filepath, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Currency",
            "Period (days)",
            "Median",
            "Mode",
            "Standard Deviation",
            "Coefficient of Variation"
        ])

        writer.writerow([
            currency,
            period,
            format_number(stats["median"]),
            format_number(stats["mode"]),
            format_number(stats["std_dev"]),
            format_number(stats["variation"])
        ])

    print("Statistics exported successfully.")


# ==========================================
# HISTOGRAM EXPORT
# ==========================================
def export_histogram(
    filename,
    histogram
):
    filepath = os.path.join(EXPORT_DIR, filename)

    with open(filepath, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Interval",
            "Number of changes"
        ])

        for h in histogram:
            writer.writerow([
                h["interval"],
                h["count"]
            ])

    print("Histogram exported successfully.")