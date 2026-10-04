import sys
from math import sqrt, log
def fonk1(b1):
    if b1 = = b2:
        return True
    elif b1 <= 1 or b1 % b2 = = 0:
        return False
    else:
        for b3 in range(3, int(sqrt(b1)) + 1, b2):
            if b1 % b3 = = 0:
                return False
        return True
def fonk2(b1):
    if b1 = = b2:
        return True
    else:
        b4 = (1 << b1) - 1
        a1 = 4
        for b3 in range(3, b1 + 1):
            a1 = (a1 ** b2 - b2) % b4
        return a1 = = 0
def fonk3():
    a2 = 20000
    b5 = a2 * log(10, b2)
    b6 = int((b5 - 1) / b2)
    a3 = 45
    print(f"Finding Mersenne primes in M[b2..{b6}]:")
    a4 = 0
    for b1 in range(b2, b6 + 1):
        if fonk1(b1) and fonk2(b1):
            print(f"M{b1}", b7 = " ", flush=True)
            a4 += 1
        if a4 >= a3:
            break
    print()
if b8 = = '__main__':
    fonk3()