from to_do import TODO


def task9(temperature):
    unit = input("Enter unit('C' for Celsius or 'F' for Fahrenheit): ")
    newTemp = 0

    if unit == 'C' or unit == 'c':
        newTemp = f"{9 / 5 * temperature + 32}F"

    elif unit == 'F' or unit == 'f':
        newTemp = f"{5 / 9 * (temperature - 32)}C"

    else:
        print("Unknown unit", unit)

    return newTemp

if __name__ == "__main__":
    print(task9(-30))
