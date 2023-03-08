from to_do import TODO
import re

def task10(password):
    SpecialSym = ['$', '@', '#']
    result = True

    if len(password) < 6:
        result = False

    if len(password) > 10:
        result = False

    if not any(char.isdigit() for char in password):
        result = False

    if not any(char.isupper() for char in password):
        result = False

    if not any(char.islower() for char in password):
        result = False

    if not any(char in SpecialSym for char in password):
        result = False
    else:
        return result


if __name__ == "__main__":
    print(task10("DmFf1w3#@"))