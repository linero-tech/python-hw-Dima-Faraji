from to_do import TODO


def task4():
    begin = 1
    end = 1000
    for result in range(begin, end + 1):
        if result % 9 == 0:
            print(result)

    return result

if __name__ == "__main__":
    print(task4())
