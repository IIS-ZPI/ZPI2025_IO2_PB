from datetime import datetime, timedelta
from src.api import (
    get_available_currencies,
    get_currency_data
)
from src.analysis import (
    analyze_sessions,
    calculate_statistics,
    create_currency_pair,
    build_histogram
)
from src.visualization import display_histogram
from src.export import export_histogram, export_statistics, export_session_analysis
from src.utils import validate_date


# ==========================================
# MAIN MENU
# ==========================================
def main_menu():

    print("\n=== NBP CURRENCY ANALYSIS SYSTEM ===")
    print("Choose analysis type:\n")
    print("1. Calculate the number of rising, falling and unchanged sessions")
    print("2. Calculate statistical measures (Median, Mode, Standard deviation, Coefficient of variation)")
    print("3. Determine distribution of monthly and quarterly changes between currency pairs")
    print("4. Exit application\n")

    return input(
        "Type 1-4 and press Enter "
        "to choose the corresponding option: "
    )


# ==========================================
# CURRENCY MENU
# ==========================================
def choose_currency():

    currencies = get_available_currencies()

    while True:

        print("\n=== SELECT CURRENCY ===")
        print("Here are the available currencies:\n")

        for i, currency in enumerate(currencies, start=1):
            print(f"{i}. {currency}")

        print(f"{len(currencies)+1}. Return\n")

        choice = input(
            f"Type 1-{len(currencies)+1}: "
        )

        try:

            choice = int(choice)

            if 1 <= choice <= len(currencies):
                return currencies[choice - 1]

            elif choice == len(currencies) + 1:
                return None

        except:
            pass

        print("Invalid option.")


def choose_currency_for_histogram(exclude=None):

    if exclude is None:
        exclude = []

    currencies = ["PLN"] + get_available_currencies()

    currencies = [c for c in currencies if c not in exclude]

    while True:

        print("\n=== SELECT CURRENCY ===")
        print("Here are the available currencies:\n")

        for i, currency in enumerate(currencies, start=1):
            print(f"{i}. {currency}")

        print(f"{len(currencies)+1}. Return\n")

        choice = input(f"Type 1-{len(currencies)+1}: ")

        try:
            choice = int(choice)

            if 1 <= choice <= len(currencies):
                return currencies[choice - 1]

            elif choice == len(currencies) + 1:
                return None

        except:
            pass

        print("Invalid option.")


# ==========================================
# PERIOD MENU
# ==========================================
def choose_period():

    while True:

        print("\n=== SELECT TIME PERIOD FOR ANALYSIS ===\n")
        print("1. 1 week")
        print("2. 2 weeks")
        print("3. 1 month")
        print("4. 1 quarter (3 months)")
        print("5. 1/2 year (6 months)")
        print("6. 1 year")
        print("7. Return\n")

        choice = input("Type 1-7: ")

        periods = {
            "1": 7,
            "2": 14,
            "3": 30,
            "4": 90,
            "5": 180,
            "6": 365
        }

        if choice in periods:
            return periods[choice]

        elif choice == "7":
            return None

        print("Invalid option.")


# ==========================================
# START DATE
# ==========================================
def choose_start_date():

    while True:

        print("\n=== DEFINE START DATE ===")

        date = input(
            "Enter date YYYY-MM-DD "
            "or R to return: "
        )

        if date.upper() == "R":
            return None

        if validate_date(date):
            return date

        print("Invalid date format.")


# ==========================================
# DISPLAY MENU
# ==========================================
def display_menu():

    while True:

        print("\n=== ANALYSIS RESULT ===")

        choice = input(
            "Do you want to display the calculated data? "
            "Type YES or NO: "
        ).upper()

        if choice in ["YES", "NO"]:
            return choice

        print("Invalid option.")


# ==========================================
# EXPORT MENU
# ==========================================
def export_menu():

    while True:

        print("\n=== EXPORT ANALYSIS RESULT ===")

        choice = input(
            "Do you want to export the calculated "
            "data into a CSV file? "
            "Type YES or NO: "
        ).upper()

        if choice in ["YES", "NO"]:
            return choice

        print("Invalid option.")


# ==========================================
# CONTINUE MENU
# ==========================================
def continue_menu():

    while True:

        print("\n=== CONTINUE ===")

        choice = input(
            "Do you want to continue using "
            "the application? "
            "Type YES or NO: "
        ).upper()

        if choice in ["YES", "NO"]:
            return choice

        print("Invalid option.")


# ==========================================
# SESSION ANALYSIS FLOW
# ==========================================
def session_analysis_flow():

    currency = choose_currency()

    if currency is None:
        return

    days = choose_period()

    if days is None:
        return

    end_date = datetime.today()

    start_date = end_date - timedelta(days=days)

    rates = get_currency_data(
        currency,
        start_date.strftime("%Y-%m-%d"),
        end_date.strftime("%Y-%m-%d")
    )

    if not rates:
        print("No data available.")
        return

    up, down, same = analyze_sessions(rates)

    display = display_menu()

    if display == "YES":

        print("\n=== SESSION ANALYSIS RESULT ===")
        print("Rising sessions:", up)
        print("Falling sessions:", down)
        print("Unchanged sessions:", same)

    export = export_menu()

    if export == "YES":

        filename = input("Enter filename: ")

        export_session_analysis(
            filename,
            currency,
            f"{days}",
            up,
            down,
            same
        )


# ==========================================
# STATISTICS FLOW
# ==========================================
def statistics_flow():

    currency = choose_currency()

    if currency is None:
        return

    days = choose_period()

    if days is None:
        return

    end_date = datetime.today()

    start_date = end_date - timedelta(days=days)

    rates = get_currency_data(
        currency,
        start_date.strftime("%Y-%m-%d"),
        end_date.strftime("%Y-%m-%d")
    )

    if not rates:
        print("No data available.")
        return

    stats = calculate_statistics(rates)

    display = display_menu()

    if display == "YES":

        print("\n=== STATISTICAL MEASURES ===")
        print("Median:", round(stats["median"], 4))
        print("Mode:", stats["mode"])
        print("Standard deviation:",
              round(stats["std_dev"], 4))
        print("Coefficient of variation:",
              round(stats["variation"], 2), "%")

    export = export_menu()

    if export == "YES":

        filename = input("Enter filename: ")

        export_statistics(
            filename,
            currency,
            f"{days}",
            stats
        )


# ==========================================
# HISTOGRAM FLOW
# ==========================================
def histogram_flow():

    print("\nFIRST CURRENCY")
    first = choose_currency_for_histogram()

    if first is None:
        return

    print("\nSECOND CURRENCY")
    second = choose_currency_for_histogram(exclude=[first])

    if second is None:
        return

    start_date = choose_start_date()

    if start_date is None:
        return

    analysis_type = input(
        "\nType MONTHLY or QUARTERLY: "
    ).upper()

    if analysis_type == "MONTHLY":
        days = 30
    else:
        days = 90

    start = datetime.strptime(
        start_date,
        "%Y-%m-%d"
    )

    end = start + timedelta(days=days)

    if first == "PLN":

        second_rates = get_currency_data(
            second,
            start_date,
            end.strftime("%Y-%m-%d")
        )

        first_rates = [
            {
                "effectiveDate": rate["effectiveDate"],
                "mid": 1.0
            }
            for rate in second_rates
        ]

    elif second == "PLN":

        first_rates = get_currency_data(
            first,
            start_date,
            end.strftime("%Y-%m-%d")
        )

        second_rates = [
            {
                "effectiveDate": rate["effectiveDate"],
                "mid": 1.0
            }
            for rate in first_rates
        ]

    else:

        first_rates = get_currency_data(
            first,
            start_date,
            end.strftime("%Y-%m-%d")
        )

        second_rates = get_currency_data(
            second,
            start_date,
            end.strftime("%Y-%m-%d")
        )

    if not first_rates or not second_rates:
        print("No data available.")
        return

    pair_rates = create_currency_pair(
        first_rates,
        second_rates
    )

    histogram = build_histogram(pair_rates)

    display = display_menu()

    if display == "YES":

        display_histogram(
            histogram,
            f"{first}/{second}"
        )

    export = export_menu()

    if export == "YES":

        filename = input("Enter filename: ")

        export_histogram(
            filename,
            histogram
        )


# ==========================================
# APPLICATION LOOP
# ==========================================
def start_application():

    while True:

        choice = main_menu()

        if choice == "1":
            session_analysis_flow()

        elif choice == "2":
            statistics_flow()

        elif choice == "3":
            histogram_flow()

        elif choice == "4":
            print("Application closed.")
            break

        else:
            print("Invalid option.")
            continue

        if continue_menu() == "NO":
            print("Application closed.")
            break