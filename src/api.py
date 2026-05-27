import requests

BASE_URL = "https://api.nbp.pl/api/exchangerates/rates/A"


def get_available_currencies():
    url = "https://api.nbp.pl/api/exchangerates/tables/A/?format=json"

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()[0]["rates"]

    currencies = []

    for rate in data:
        currencies.append(rate["code"])

    return sorted(currencies)


def get_currency_data(currency, start_date, end_date):
    url = f"{BASE_URL}/{currency}/{start_date}/{end_date}/?format=json"

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()

    return data["rates"]