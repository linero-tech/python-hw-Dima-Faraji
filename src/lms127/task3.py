from to_do import TODO
# Area of Circle: It is the area occupied by the circle. Given by the formula
# Area = π*R*R
# Value of π = 3.14, R is the radius of a circle.
# Perimeter of Circle: Also known as the circumference. It is given by the formula
# Perimeter = 2*π*R
# π = 3.14

def task3(radius):
    pi = 3.14
    result = 2 * pi * radius
    return result
if __name__ == "__main__":
        print(task3(radius=2.0))