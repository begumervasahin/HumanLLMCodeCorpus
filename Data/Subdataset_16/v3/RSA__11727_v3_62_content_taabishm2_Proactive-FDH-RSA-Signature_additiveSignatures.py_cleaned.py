import random
from sympy import nextprime
from sympy.core.numbers import igcdex
def fonk1(b2, m):
    g, x, b1 = igcdex(b2, m)
    if g != 1:
        raise ValueError('Modular inverse does not exist')
    return x % m
class class1:
    @staticmethod
    def fonk2(b16):
        return nextprime(b16)
    @staticmethod
    def fonk3(b6):
        return random.randrange(b6, 2 * b6)
    @staticmethod
    def fonk4(shares, b6, c):
        b2 = random.randrange(2, b6)
        b3 = pow(b2, c, b6)
        b4 = [pow(b2, di, b6) for di in shares]
        return b4, b3, b2
    @staticmethod
    def fonk5(b4, shares, b6, c, b3, gen):
        b5 = [
            (pow(gen, c - shares[i], b6) * b4[i]) % b6 = = b3
            for i in range(len(b4))
        ]
        return b5
b7 = None
b8 = None
b9 = None
b10 = None
b11 = None
b12 = None
b13 = None
b14 = [3, 4, 5]
b15 = len(b14)
b16 = max(b14) + 1
def fonk6():
    global b7, b8, b9, b10, b11, b12
    b8 = class1.fonk2(b16)
    b7 = class1.fonk3(b8)
    b9, b10, b12 = class1.fonk4(b14, b8, b7)
def fonk7():
    global b7, b8, b9, b10, b11, b12, b13
    b11 = class1.fonk5(
        b9, b14, b8, b7, b10, b12
    )
    b13 = b11
    print("ADDITIVE SHARE STATUS:", b11)
    if b11.count(True) != b15:
        print("INVALID SIGNATURE!\nALERT: INVOKE BACKUP")
fonk6()
fonk7()