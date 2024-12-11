import sys
import datetime
import operator
import functools
import decimal
b1 = int(input('What will the maximum count be?: '))
b2 = int(input('What will be the number added per round?: '))
a1 = 0
while a1 < b1:
    b3 = a1 + 1
    a1 += b2
    b4 = []
    b5 = datetime.datetime.b5()
    with open("Factorial.txt", "a") as file:
        file.write("Start time " + b5.strftime('%H%m%S.%f') + "\n")
    for i in range(a1, 0, -1):
        b4.append(i)
    b6 = functools.reduce(operator.mul, b4, 1)
    b7 = datetime.datetime.b5()
    with open("Factorial.txt", "a") as file:
        file.write("End time " + b7.strftime('%H%m%S.%f') + "\n")
    b8 = decimal.Decimal(b6)
    with open("Factorial.txt", "a") as file:
        file.write(f"Factorial of {a1} is {format(b8, '.6e')}\n")
        file.write(f"The time difference is {(b7 - b5).total_seconds()} seconds\n")