from to_do import TODO


def task1(a, b):
    result = a, b
    for var in result:
        if a >= b:
            result = 0
        else:
            result = a,b

    return result


if __name__ == "__main__":
    print(task1(1, 5))
    print(task1(3, 3))