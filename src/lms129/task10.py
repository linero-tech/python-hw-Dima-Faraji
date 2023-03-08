from to_do import TODO
import re

def task10(password):
    result = True
    while result:
        if (len(password) <= 6 or len(password) > 10):
            break
        elif not re.search("[a-z]", password):
            break
        elif not re.search("[0-9]", password):
            break
        elif not re.search("[A-Z]", password):
            break
        elif not re.search("[$#@]", password):
            break
        else:
            print("Valid Password")
            result = False
            break

    if result:
        print("Not a Valid Password")


if __name__ == "__main__":
    task10("DmFf2345@")
