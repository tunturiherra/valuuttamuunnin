import requests


def convert_money(amount, from_currency, to_currency):
    base_url = "https://api.exchangerate-api.com/v4/latest/"

    # haetaan tiedot
    response = requests.get(base_url + from_currency)
    data = response.json()

    # tarkistetaan, että valuutat löytyy lähteestä.
    if 'rates' in data:
        rates = data['rates']
        if from_currency == to_currency:
            return amount

        # tehdään konversio
        if from_currency in rates and to_currency in rates:
            conversion_rate = rates[to_currency] / rates[from_currency]
            converted_amount = amount * conversion_rate
            return converted_amount
