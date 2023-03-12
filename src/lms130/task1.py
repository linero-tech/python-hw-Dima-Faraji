from to_do import TODO
import random

def task1(items):

    return random.choice(items)

if __name__ == "__main__":
    print(task1(items=[111, 222, 333, 444, 555]))
