from to_do import TODO


def task9(temperature):
    print("Options are: \n")
    print("1.Convert temperatures from Celsius to Fahrenheit \n")
    print("2.Convert temperatures from Fahrenheit to Celsius \n")
    result = int(input("Choose any Option(1 or 2) : "))
    if result == 1:
        cel = float(temperature)
        fahr = (cel * 9 / 5) + 32
        return f"{int(fahr)}F"
    else:
        fahr = float(temperature)
        cel = (fahr - 32) * 5 / 9
        return f"{int(cel)}C"


if __name__ == "__main__":
    print(task9(-30))
