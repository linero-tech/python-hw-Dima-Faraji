from to_do import TODO


def task3(number):
    factorial = 1
    if number == 0:
        return 1
    else:
        for i in range(1, number + 1):
            factorial = factorial * i
        return factorial

if __name__ == "__main__":
    print(task3(5))