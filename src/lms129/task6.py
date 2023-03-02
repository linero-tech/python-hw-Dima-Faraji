from to_do import TODO


def task6(number):
    result = 0

    while number != 0:
        digit = number % 10
        result = result * 10 + digit
        number //= 10
    return result


if __name__ == "__main__":
    print(task6(678))