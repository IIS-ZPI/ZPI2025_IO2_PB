import requests
from requests.exceptions import RequestException

BASE_URL = "https://api.nbp.pl/api/exchangerates/rates/A"


def get_available_currencies():
    url = "https://api.nbp.pl/api/exchangerates/tables/A/?format=json"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print("Cannot download currency list from NBP API. Please try again later.")
            return []

        data = response.json()[0]["rates"]

        currencies = []

        for rate in data:
            currencies.append(rate["code"])

        return sorted(currencies)

    except RequestException:
        print("Network error: cannot connect to NBP API. Check your internet connection and try again.")
        return []

    except (ValueError, KeyError, IndexError):
        print("Data error: received invalid response from NBP API.")
        return []


def get_currency_data(currency, start_date, end_date):
    url = f"{BASE_URL}/{currency}/{start_date}/{end_date}/?format=json"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(f"Cannot download data for {currency}. Please check the selected date range or try again later.")
            return []

        data = response.json()

        return data["rates"]

    except RequestException:
        print("Network error: cannot connect to NBP API. Check your internet connection and try again.")
        return []

    except (ValueError, KeyError):
        print("Data error: received invalid response from NBP API.")
        return []