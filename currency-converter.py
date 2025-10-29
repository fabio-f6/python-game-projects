def get_currency(label):
    choices = ("EUR", "USD", "BRL")
    while True:
        currency = input(f"Enter {label} currency (EUR/USD/BRL): ").upper()
        if currency in choices:
            return currency
        else:
            print("Please enter a valid currency (EUR/USD/BRL)")

def get_amount():
    while True:
        try:
            inputamount = float(input("Enter Amount: "))
            if inputamount <= 0:
                raise ValueError()
            return inputamount
        except ValueError:
            print("Invalid input. Please enter a positive numeric value")

def convert(inputAmount, inputCurrency, outputCurrency):
    exchange_rates = {
        "USD": {"EUR": 0.86, "BRL": 5.39},
        "EUR": {"USD": 1.16, "BRL": 6.34},
        "BRL": {"EUR": 0.16, "USD": 0.19},
    }

    if inputCurrency == outputCurrency:
        return inputAmount

    return inputAmount * exchange_rates[inputCurrency][outputCurrency]

def main():
    input_amount = get_amount()
    input_currency = get_currency("source")
    output_currency = get_currency("target")
    converted_amount = convert(input_amount, input_currency, output_currency)
    print(f"{input_amount} {input_currency} to {output_currency} -> {converted_amount:.2f}")

if __name__ == '__main__':
    main()