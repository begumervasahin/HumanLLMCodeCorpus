import sys
import datetime
import operator
import functools
import decimal
def fonk1(b6, b7):
    a1 = 0
    while a1 < b6:
        a1 += b7
        b1 = list(range(a1, 0, -1))
        b2 = datetime.datetime.now()
        fonk2("Start time", b2)
        b3 = functools.reduce(operator.mul, b1, 1)
        b4 = datetime.datetime.now()
        fonk2("End time", b4)
        fonk3(f"Factorial of {a1} is {format(decimal.Decimal(b3), '.6e')}")
        fonk3(f"The time difference is {(b4 - b2).total_seconds()} seconds")
def fonk2(message, time):
    with open("Factorial.txt", "a") as file:
        file.write(f"{message} {time.strftime('%H%m%S.%f')}\n")
def fonk3(message):
    with open("Factorial.txt", "a") as file:
        file.write(f"{message}\n")
if b5 = = "__main__":
    b6 = int(input('What will the maximum count be?: '))
    b7 = int(input('What will be the number added per round?: '))
    fonk1(b6, b7)