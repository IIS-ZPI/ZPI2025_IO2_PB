import matplotlib.pyplot as plt


# ==========================================
# DISPLAY HISTOGRAM
# ==========================================
def display_histogram(histogram, title):

    print("\n=== HISTOGRAM ===\n")

    print(f"{'Interval':<25} {'Number of changes'}")

    labels = []
    values = []

    for h in histogram:

        print(f"{h['interval']:<25} {h['count']}")

        labels.append(h["interval"])
        values.append(h["count"])

    plt.figure(figsize=(12, 6))

    plt.bar(labels, values)

    plt.title(title)

    plt.xlabel("Interval")
    plt.ylabel("Number of changes")

    plt.xticks(rotation=45)

    plt.grid(True)

    plt.show()