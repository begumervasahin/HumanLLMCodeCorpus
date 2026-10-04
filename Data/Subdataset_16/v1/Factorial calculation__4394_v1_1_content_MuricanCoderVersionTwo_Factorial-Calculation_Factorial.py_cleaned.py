import sys
import datetime
import functools
import operator
import decimal
def fonk1(n):
    return functools.reduce(operator.mul, range(1, n + 1), 1)
def fonk2(b4, b6, a1, b5):
    b1 = (b6 - b4).total_seconds()
    with open("Factorial.txt", "a") as file:
        file.write(f"Start time: {b4.strftime('%H%M%S.%f')}\n")
        file.write(f"End time: {b6.strftime('%H%M%S.%f')}\n")
        file.write(f"Factorial of {a1} is {format(b5, '.6e')}\n")
        file.write(f"The time difference is {b1} seconds\n")
def fonk3():
    b2 = int(input('What will the maximum count be?: '))
    b3 = int(input('What will be the a1 added per round?: '))
    a1 = 0
    while a1 < b2:
        a1 += b3
        b4 = datetime.datetime.now()
        b5 = fonk1(a1)
        b6 = datetime.datetime.now()
        fonk2(b4, b6, a1, decimal.Decimal(b5))
if b7 = = "__main__":
    fonk3()