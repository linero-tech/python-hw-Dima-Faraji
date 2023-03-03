from to_do import TODO


def task4():
    total = 0

    for result in range(1, 1000):
        if result % 9 == 0:
            total += result
    return total

if __name__ == "__main__":
        print(task4())
