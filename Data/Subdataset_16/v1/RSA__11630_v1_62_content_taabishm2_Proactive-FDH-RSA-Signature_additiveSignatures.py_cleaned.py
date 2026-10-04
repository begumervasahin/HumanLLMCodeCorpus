import random
from sympy import nextprime
from sympy.core.numbers import igcdex
def fonk1(b5, m):
    g, x, b1 = igcdex(b5, m)
    if g != 1:
        raise ValueError('Modular inverse does not exist')
    return x % m
class class1:
    @staticmethod
    def fonk2(b13):
        '''Generate prime group with order > b13'''
        b2 = nextprime(b13)
        return b2
    @staticmethod
    def fonk3(b2):
        '''Pick b5 sum such that di + b3 = sum and b2 < sum < 2p'''
        return random.randrange(b2, 2 * b2)
    @staticmethod
    def fonk4(shares, b2, c):
        '''Generate b4 and b6, return as [fonk4(list), b6(int)]'''
        b4 = []
        b5 = random.randrange(2, b2)
        b6 = pow(b5, c, b2)
        for di in shares:
            b4.append(pow(b5, di, b2))
        return [b4, b6, b5]
    @staticmethod
    def fonk5(b4, shares, b2, c, b6, gen):
        '''Generates b8 by b5 party holding b5 'share' to the b4[i] for all additive shares'''
        b7 = []
        for i in range(len(b4)):
            b8 = (pow(gen, c - shares[i], b2) * b4[i]) % b2
            b7.append(b8 = = b6)
        return b7
b9 = b15 = verify_challenge = verify_verifier = b14 = b16 = None
b10 = None
b11 = [3, 4, 5]
b12 = len(b11)
b13 = max(b11) + 1
def fonk6():
    global b9, b15, verify_challenge, verify_verifier, b14, b16
    verify_challenge, b14 = [], []
    b15 = class1.fonk2(b13)
    b9 = class1.fonk3(max(b11) + 1)
    verify_challenge, verify_verifier, b16 = class1.fonk4(b11, b15, b9)
def fonk7():
    global b9, b15, verify_challenge, verify_verifier, b14, b16, b10
    b14 = class1.fonk5(verify_challenge, b11, b15, b9, verify_verifier, b16)
    b10 = b14
    print("ADDITIVE SHARE STATUS:", b14)
    if b14.count(True) != b12:
        print("INVALID SIGNATURE!\nALERT: INVOKE BACKUP")
fonk6()
fonk7()