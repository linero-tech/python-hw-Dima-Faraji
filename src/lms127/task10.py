from collections import OrderedDict
from itertools import count

from to_do import TODO


def task10_1(assessments):
    result = len(assessments)
    return result

def task10_2(assessments):
    result = assessments[3]
    return result


def task10_3(assessments):
    result = assessments[(len(assessments) - 1) // 2:(len(assessments) + 2) // 2]
    return result


def task10_4(assessments):
    return TODO(
        "Replace this 'TODO' with the variable 'result'. Do not erase the 'return' keyword"
    )
if __name__ == "__main__":
    print(task10_1(assessments="LMHHF"))
    print(task10_2(assessments="LMFHMF"))
    print(task10_3(assessments="LMFHM"))