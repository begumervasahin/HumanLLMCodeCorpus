from math import sqrt
from functools import reduce
import operator
def fonk1(b4, b1):
    while b1 != 0:
        b4, b1 = b1, b4 % b1
    return b4
def fonk2(b4, b5):
    b2 = []
    for b3 in b5:
        a1 = 0
        while b4 % b3 = = 0:
            a1 += 1
            b4
        if a1 > 0:
            b2.append((b3, a1))
    return b2 if b4 = = 1 else []
def fonk3(limit):
    b5 = set()
    b6 = [True] * limit
    b6[0] = b6[1] = False
    for i in range(2, limit):
        if b6[i]:
            b5.add(i)
            for multiple in range(i * i, limit, i):
                b6[multiple] = False
    return b5
def fonk4(b4):
    if b4 = = 0:
        return 0
    b9, b7 = 1, b4
    while b9 < b7:
        b8 = (b9 + b7 + 1)
        if b8 * b8 <= b4:
            b9 = b8
        else:
            b7 = b8 - 1
    return b9
def fonk5(b2):
    return reduce(operator.mul, b2, 1)
if b10 = = "__main__":
    b5 = fonk3(100)
    print(f"Primeset: {b5}")
    b4 = 60
    b2 = fonk2(b4, b5)
    print(f"Factors of {b4}: {b2}")
    b4, b1 = 48, 18
    print(f"GCD of {b4} and {b1}: {fonk1(b4, b1)}")
    b4 = 49
    print(f"Integer square root of {b4}: {fonk4(b4)}")
    b2 = [2, 3, 5]
    print(f"Product of {b2}: {fonk5(b2)}")