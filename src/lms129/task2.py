from to_do import TODO

def task2(number):
    flag = False

    if number == 1:
        print("false")
    elif number > 1:
        # check for factors
        for i in range(2, number):
            if (number % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

        # check if flag is True
        if flag:
            print("false")
        else:
            print("true")


if __name__ == "__main__":
    task2(5)
    task2(3)
    task2(21)
    task2(12)
