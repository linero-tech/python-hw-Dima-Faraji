from to_do import TODO
import re

def task10(password):
    flag = 0

    if not re.search('[0-9]', password):
        flag = 1

    if not re.search('[a-z]', password):
        flag = 1

    if not re.search('[A-Z]', password):
        flag = 1

    if not re.search('[$#@]', password):
        flag = 1

    if len(password) < 6 or len(password) > 10:
        flag = 1

    if (flag == 0):
        print('Password is valid')
    else:
        print('Password is invalid')

if __name__ == "__main__":
    task10("DmFf1w3#@")