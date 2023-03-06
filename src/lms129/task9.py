from to_do import TODO


def task9(temperature):
    import math

    if temperature[-1] == "C" or temperature[-1] == "c":
        result = float(temperature[:-1]) * 9 / 5 + 32
        result = f"{str(math.trunc(result))}F"

    elif temperature[-1] == "F" or temperature[-1] == "f":
        result = (float(temperature[:-1]) - 32) * 5 / 9
        result = f"{str(math.trunc(result))}C"

    else:
        result = "Invalid input"

    return result


if __name__ == "__main__":
    print(task9("-30C"))
    print(task9("37C"))
    print(task9("-22F"))
