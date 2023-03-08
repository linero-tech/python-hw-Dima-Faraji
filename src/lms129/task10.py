from to_do import TODO
import re

def task10(password):
    result = True
    if re.fullmatch(r'[A-Za-z0-9@#$]{6,10}', password):
        print("Valid Password") # match

    else:
        print("Not a Valid Password") # no match

    return result


if __name__ == "__main__":
    task10("DmFf2@")