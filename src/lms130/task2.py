from to_do import TODO


def task2(items):
    listOfZeros = [0] * (2 * len(items) - 1)
    result = 0
    for i in range(0, len(listOfZeros)):
        if (i % 2 == 0):
            listOfZeros[i] = result
            result += 1
    return result

if __name__ == "__main__":
    print(task2(items=[1, 2, 3, 4]))