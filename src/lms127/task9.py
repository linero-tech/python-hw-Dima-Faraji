from to_do import TODO


def task9(sentence, character):
    result = character in sentence
    return result
if __name__ == "__main__":
        print(task9("I code in KOTLIN", "i"))
