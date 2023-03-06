from to_do import TODO


def task9(temperature):

   fahrenheit = (temperature * 1.8) + 32

   return ('%.2f Celsius is equivalent to: %.2f Fahrenheit' % (temperature, fahrenheit))

if __name__ == "__main__":
    print(task9(-30))
