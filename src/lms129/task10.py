from to_do import TODO
import re

def task10(password):
    rules = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@])[A-Za-z\d@$#]{6,10}$"

    # compiling regex
    match_re = re.compile(rules)
    # searching regex
    result = re.search(match_re, password)
    # validating conditions
    if result:
        print("Valid Password")
    else:
        print("Invalid Password")

if __name__ == "__main__":
    task10("DmFf2@")