from to_do import TODO


def task2(items):
    if items == []:
        return 0
    else:
        return sum(items[::2]) # every second element (starting from element 0)

if __name__ == "__main__":
    print(task2(items=[1, 2, 3, 4]))
    print(task2(items=[]))