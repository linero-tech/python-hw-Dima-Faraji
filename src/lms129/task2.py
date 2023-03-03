from to_do import TODO


def task2(number):
    # Program to check if a number is prime or not
    # define a result variable
    result = False
    if number == 1:
        print("false")
    elif number > 1:
        # check for factors
        for i in range(2, number):
            if (number % i) == 0:
                # if factor is found, set result to True
                result = True
                # break out of loop
                break
        # check if result is True
        if result:
            print("false")
        else:
            print("true")

    return result


if __name__ == "__main__":
    task2(5)