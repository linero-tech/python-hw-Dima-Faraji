from to_do import TODO
import re

def task10(password):
    result = 0
    while True:
        if (len(password) < 6):
            result = -1
            break
        elif (len(password) > 10):
            result = -1
            break
        elif not re.search("[a-z]", password):
            result = -1
            break
        elif not re.search("[A-Z]", password):
            result = -1
            break
        elif not re.search("[0-9]", password):
            result = -1
            break
        elif not re.search("[$#@]", password):
            result = -1
            break

        else:
            result = 0
            print("Valid Password")
            break

    if result == -1:
        print("Not a Valid Password ")


if __name__ == "__main__":
    task10("DmFf11298@")