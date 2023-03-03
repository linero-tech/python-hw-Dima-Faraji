from to_do import TODO


def task9(temperature):
    temperature = float(input("Enter Temperature: "))
    unit = input("Enter unit('C' for Celsius or 'F' for Fahrenheit): ")

    if unit == 'C' or unit == 'c':
        newTemp = 9 / 5 * temperature + 32
        print("Temperature is", newTemp,"F")
    elif unit == 'F' or unit == 'f':
        newTemp = 5 / 9 * (temperature - 32)
        print("Temperature is", newTemp,"C")
    else:
        print("Unknown unit", unit)


if __name__ == "__main__":
    (task9(30))
