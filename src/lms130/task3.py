from to_do import TODO
import collections

def task3(items):

    return [i for i, y in collections.Counter(items).items() if y > 1]


if __name__ == "__main__":
    print(task3(items=[1, 1, 1, 2, 2, 3]))
    print(task3(items=[1, 1, 1, 2, 2, 3, 3, 4, 5, 5]))