from to_do import TODO


def task1(a, b):
    result = a, b
    if a >= b:
        print(0)
    else:
        print(a, b)
    return result

if __name__ == "__main__":
    task1(1, 5)
    task1(3, 3)
   