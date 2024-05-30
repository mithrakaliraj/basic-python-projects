def get_static_exchange_rates():
    return {
        "USD": 1.0,
        "EUR": 0.85,
        "GBP": 0.75,
        "JPY": 110.57,
        "AUD": 1.34,
        "CAD": 1.25,
        "CHF": 0.91,
        "CNY": 6.45,
        "SEK": 8.58,
        "NZD": 1.40,
        "INR": 74.50
    }

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Invalid currency code")

    if from_currency != 'USD':
        amount = amount / rates[from_currency]
    converted_amount = amount * rates[to_currency]
    return converted_amount

def main():
    rates = get_static_exchange_rates()
    print("Available currencies:", ', '.join(rates.keys()))
    
    try:
        amount = float(input("Enter amount: "))
        from_currency = input("From currency (e.g., USD): ").upper()
        to_currency = input("To currency (e.g., EUR): ").upper()

        converted_amount = convert_currency(amount, from_currency, to_currency, rates)
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
