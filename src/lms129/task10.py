from to_do import TODO
import re

def task10(password):
    if len(password) < 6 or len(password) >= 10:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True


if __name__ == "__main__":
    print(task10("DmFw3679@"))