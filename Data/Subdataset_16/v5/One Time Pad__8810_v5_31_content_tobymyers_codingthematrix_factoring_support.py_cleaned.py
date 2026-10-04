import operator
from functools import reduce
def fonk1(b4, b1):
    while b1:
        b4, b1 = b1, b4 % b1
    return b4
def fonk2(b4, b6):
    b2 = []
    for b3 in b6:
        a1 = 0
        while b4 % b3 = = 0:
            a1 += 1
            b4
        if a1 > 0:
            b2.append((b3, a1))
    return b2 if b4 = = 1 else []
def fonk3(limit):
    b5 = [True] * limit
    b5[0] = b5[1] = False
    b6 = set()
    for num in range(2, limit):
        if b5[num]:
            b6.add(num)
            for multiple in range(num * num, limit, num):
                b5[multiple] = False
    return b6
def fonk4(b4):
    b9, b7 = 1, b4
    while b7 - b9 > 1:
        b8 = (b9 + b7)
        if b8 * b8 <= b4:
            b9 = b8
        else:
            b7 = b8
    return b9 if b9 * b9 = = b4 else b7
def fonk5(b2):
    return reduce(operator.mul, b2, 1)