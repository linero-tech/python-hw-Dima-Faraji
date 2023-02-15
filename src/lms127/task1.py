from to_do import TODO

def task1():
    country = "Sweden"
    capital = "Stockholm"
    currency = "SEK"
    message = f"Country: {country} \nCapital: {capital} \nCurrency: {currency} "
    print(f"{message.title()}")
    return message

if __name__ == "__main__":
    task1()
