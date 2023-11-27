from functions import convert_money

while True:
    # Valuuttakoodit
    currencies = {
        1: "USD",
        2: "EUR",
        3: "GBP",
        4: "JPY",
        5: "AUD",
        6: "SEK"
    }

    try:
        # pyydetään ensin summa ja tarkistetaan, että se koostuu vain numeroista
        amount = input("Syötä summa:\n")
        if not amount.isdigit():
            raise ValueError("Syötä vain numeroita.")

        amount = float(amount)

        # tulostetaan ruudulle vaihtoehdot, valuutta valitaan numerolla
        print("Valitse lähtövaluutta (numero):")
        for number, currency in currencies.items():
            print(f"{number}. {currency}")

        from_currency_index = int(input())
        from_currency = currencies.get(from_currency_index)

        # jos käyttäjä valitsee jotain muuta kuin 1-6 väliltä.
        if from_currency is None:
            raise ValueError("Virheellinen lähtövaluutan numero.")

        # sitten lopuksi kohdevaluutta, ja sama homma valinnan kohdalla
        print("Valitse kohdevaluutta (numero):")
        for number, currency in currencies.items():
            print(f"{number}. {currency}")

        to_currency_index = int(input())
        to_currency = currencies.get(to_currency_index)

        # jos käyttäjä valitsee jotain muuta kuin 1-6 väliltä.
        if to_currency is None:
            raise ValueError("Virheellinen kohdevaluutan numero.")

        # tehdään tässä valuuttojen muunnos. näyttäisi toimivan ok, kun lopuksi tulostetaan 2 desimaalilla.
        converted_amount = convert_money(amount, from_currency, to_currency)
        print(f"Lähtövaluutta: {from_currency}, summa: {amount}")
        print(f"Kohdevaluutta: {to_currency}, summa: {converted_amount:.2f}")

        # jos käyttäjä haluaa vielä tehdä lisää muunnoksia niin kysytään aloitetaanko alusta
        restart = input("\nHaluatko tehdä lisää valuuttamuunnoksia? k/e\n").lower()
        if restart == 'e':
            print("Näkemiin!")
            break

    except ValueError as e:
        print(f"{e} Yritä uudelleen.")
