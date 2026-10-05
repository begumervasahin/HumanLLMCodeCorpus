import sys
import datetime
import operator
import functools
import decimal
def fonk1():
    return datetime.datetime.now()
def fonk2(filename, content):
    with open(filename, "a") as file:
        file.write(content)
def fonk3(b8, b9, filename):
    a1 = 0
    while a1 < b8:
        b1 = a1 + 1
        a1 += b9
        b2 = fonk1()
        fonk2(filename, f"Start time {b2.strftime('%H%m%S.%f')}\n")
        b3 = [i for i in range(a1, 0, -1)]
        b4 = functools.reduce(operator.mul, b3, 1)
        b5 = fonk1()
        fonk2(filename, f"End time {b5.strftime('%H%m%S.%f')}\n")
        b6 = decimal.Decimal(b4)
        fonk2(filename, f"Factorial of {a1} is {format(b6, '.6e')}\n")
        fonk2(filename, f"The time difference is {(b5 - b2).total_seconds()} seconds\n")
if b7 = = "__main__":
    b8 = int(input('What will the maximum count be?: '))
    b9 = int(input('What will be the number added per round?: '))
    fonk3(b8, b9, "Factorial.txt")