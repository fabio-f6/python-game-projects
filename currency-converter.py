def get_currency(label):
    choices = ("EUR", "USD", "BRL", "CAD", "GBP")
    while True:
        currency = input(f"Enter {label} currency (EUR/USD/BRL/CAD/GBP): ").upper()
        if currency in choices:
            return currency
        else:
            print("Please enter a valid currency (EUR/USD/BRL/CAD/GBP)")

def get_amount():
    while True:
        try:
            inputamount = float(input("Enter Amount: "))
            if inputamount <= 0:
                raise ValueError()
            return inputamount
        except ValueError:
            print("Invalid input. Please enter a positive numeric value")

def convert(inputAmount, inputCurrency):
    exchange_rates = {
        "USD": {"EUR": 0.86, "BRL": 5.39, "GBP": 0.73, "CAD": 1.39},
        "EUR": {"USD": 1.16, "BRL": 6.34, "GBP": 0.85, "CAD": 1.62},
        "BRL": {"EUR": 0.16, "USD": 0.19, "GBP": 0.14, "CAD": 0.29},
        "GBP": {"USD": 1.35, "EUR": 1.17, "BRL": 7.50, "CAD": 1.90},
        "CAD": {"USD": 0.72, "EUR": 0.62, "BRL": 3.90, "GBP": 0.53},
    }

    results = []

    for currency in exchange_rates[inputCurrency]:
        converted_amount = inputAmount * exchange_rates[inputCurrency][currency]
        results.append(f"{inputAmount} {inputCurrency} to {currency} -> {converted_amount:.2f}")

    return results

def main():
    history = []
    while True:
        input_amount = get_amount()
        input_currency = get_currency("source")

        history.append(convert(input_amount, input_currency))
        print(history[-1])
        if "n" in input("Type 'n' if you want to stop the program.").lower():
            print("Conversion history:")
            for record in history:
                print(record)
            break


if __name__ == '__main__':
    main()