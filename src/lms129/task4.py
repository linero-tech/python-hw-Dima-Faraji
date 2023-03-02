from to_do import TODO


def task4():
    begin = 1
    end = 1000
    for number in range(begin, end + 1):
        if number % 9 == 0:
            print(number)

if __name__ == "__main__":
    task4()
