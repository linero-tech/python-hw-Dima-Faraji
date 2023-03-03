from to_do import TODO


def task2(number):
    # Program to check if a number is prime or not
    # define a result variable
    result = False

    if number > 1:
        # check for factors
        for i in range(2, number):
            result = True
            break
        else:
            result = False

    return result


if __name__ == "__main__":
    print(task2(5))