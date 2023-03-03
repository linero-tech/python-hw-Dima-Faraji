from to_do import TODO


def task1(a, b):
    result = a, b
    for i in result:
        if a >= b:
            result = 0
        else:
            result = f"{a}{b}"

    return result


if __name__ == "__main__":
    print(task1(a=1, b=5))
    print(task1(3, 3))