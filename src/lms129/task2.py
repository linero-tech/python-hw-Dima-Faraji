from to_do import TODO


def task2(number):
    # Program to check if a number is prime or not
    # define a flag variable

    result = False

    if number == 1:
        print(number, "is not a prime number")
    elif number > 1:
        # check for factors
        for i in range(2, number):
            if (number % i) == 0:
                # if factor is found, set flag to True
                result = True
                # break out of loop
                break

        # check if flag is True
        if result:
            print(number, "is not a prime number")
        else:
            print(number, "is a prime number")

    return result
if __name__ == "__main__":
    task2(5)
    task2(12)
    task2(23)