from to_do import TODO


def task1(a, b):

    for result in (a, b):
        if a >= b:
            result = 0
        else:
            result = f"{a}{b}"

    return result


if __name__ == "__main__":
    print(task1(a=1, b=5))