from to_do import TODO


def task7(a, b):
    result = 1
    for i in range(b):
        result = result * a
    return result


if __name__ == "__main__":
    print(task7(2, 3))