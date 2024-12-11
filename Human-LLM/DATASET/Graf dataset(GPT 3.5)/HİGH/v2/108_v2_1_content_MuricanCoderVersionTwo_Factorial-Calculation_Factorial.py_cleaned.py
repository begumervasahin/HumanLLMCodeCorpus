import sys
import datetime
import operator
import functools
import decimal
def fonk1(b8, b9):
    a1 = 0
    while a1 < b8:
        b1 = a1 + 1
        a1 += b9
        b2 = []
        b3 = datetime.datetime.b3()
        with open("Factorial.txt", "a") as f:
            f.write(f"Start time {b3.strftime('%H%m%S.%f')}\n")
        for i in range(a1, 0, -1):
            b2.append(i)
        b4 = functools.reduce(operator.mul, b2, 1)
        b5 = datetime.datetime.b3()
        with open("Factorial.txt", "a") as f:
            f.write(f"End time {b5.strftime('%H%m%S.%f')}\n")
        b6 = decimal.Decimal(b4)
        with open("Factorial.txt", "a") as f:
            f.write(f"Factorial of {a1} is {format(b6, '.6e')}\n")
            f.write(f"The time difference is {(b5 - b3).total_seconds()} seconds\n")
if b7 = = "__main__":
    b8 = int(input('What will the maximum count be?: '))
    b9 = int(input('What will be the number added per round?: '))
    fonk1(b8, b9)