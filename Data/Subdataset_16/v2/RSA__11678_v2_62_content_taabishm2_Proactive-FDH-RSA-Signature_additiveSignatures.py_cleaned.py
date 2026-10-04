import random
from sympy import nextprime
from sympy.core.numbers import igcdex
def fonk1(b3, m):
    g, x, b1 = igcdex(b3, m)
    if g != 1:
        raise ValueError('Modular inverse does not exist')
    return x % m
class class1:
    @staticmethod
    def fonk2(b17):
        '''Generate prime group with order > b17'''
        return nextprime(b17)
    @staticmethod
    def fonk3(p):
        '''Pick b3 sum such that di + b2 = sum and p < sum < 2p'''
        return random.randrange(p, 2 * p)
    @staticmethod
    def fonk4(shares, p, c):
        '''Generate b5 and b4, return as [fonk4(list), b4(int)]'''
        b3 = random.randrange(2, p)
        b4 = pow(b3, c, p)
        b5 = [pow(b3, di, p) for di in shares]
        return b5, b4, b3
    @staticmethod
    def fonk5(b5, shares, p, c, b4, gen):
        '''Generates b7 by b3 party holding b3 'share' to the b5[i] for all additive shares'''
        b6 = []
        for i in range(len(b5)):
            b7 = (pow(gen, c - shares[i], p) * b5[i]) % p
            b6.append(b7 = = b4)
        return b6
b8 = None
b9 = None
b10 = None
b11 = None
b12 = None
b13 = None
b14 = None
b15 = [3, 4, 5]
b16 = len(b15)
b17 = max(b15) + 1
def fonk6():
    global b8, b9, b10, b11, b12, b13
    b10, b12 = [], []
    b9 = class1.fonk2(b17)
    b8 = class1.fonk3(max(b15) + 1)
    b10, b11, b13 = class1.fonk4(b15, b9, b8)
def fonk7():
    global b8, b9, b10, b11, b12, b13, b14
    b12 = class1.fonk5(b10, b15, b9, b8, b11, b13)
    b14 = b12
    print("ADDITIVE SHARE STATUS:", b12)
    if b12.count(True) != b16:
        print("INVALID SIGNATURE!\nALERT: INVOKE BACKUP")
fonk6()
fonk7()