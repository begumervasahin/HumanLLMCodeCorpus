import operator
from math import sqrt
from functools import reduce
def fonk1(b4, b1):
    return b4 if b1 = = 0 else fonk1(b1, b4 % b1)
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
    for i, is_prime in enumerate(b6):
        if is_prime:
            b5.add(i)
            for n in range(i * i, limit, i):
                b6[n] = False
    return b5
def fonk4(b4):
    b9, b7 = 1, b4
    if b7 < b9:
        b9, b7 = b7, b9
    while b7 - b9 > 1:
        b8 = (b9 + b7)
        if b4
            b9 = b8
        else:
            b7 = b8
    return b9 if b9 * b9 = = b4 else b7
def fonk5(b2):
    return reduce(operator.mul, b2, 1)