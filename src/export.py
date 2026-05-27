import csv
import os


# ==========================================
# SESSION ANALYSIS EXPORT
# ==========================================
def export_session_analysis(
    filename,
    currency,
    period,
    rising,
    falling,
    unchanged
):

    filepath = os.path.join("..", "exports", filename)

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
    filepath = os.path.join("..", "exports", filename)

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
            stats["median"],
            stats["mode"],
            stats["std_dev"],
            stats["variation"]
        ])

    print("Statistics exported successfully.")


# ==========================================
# HISTOGRAM EXPORT
# ==========================================
def export_histogram(
    filename,
    histogram
):
    filepath = os.path.join("..", "exports", filename)

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