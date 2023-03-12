from to_do import TODO
import random


def task1(items):
    if items == []:
        return 0
    else:
        return random.choice(items)


if __name__ == "__main__":
    print(task1(items=[111, 222, 333, 444, 555]))
    print(task1(items=[]))
