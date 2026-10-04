import sys
from math import sqrt, log
def fonk1(b1):
    if b1 = = b2:
        return True
    if b1 <= 1 or b1 % b2 = = 0:
        return False
    for b3 in range(3, int(sqrt(b1)) + 1, b2):
        if b1 % b3 = = 0:
            return False
    return True
def fonk2(b1):
    if b1 = = b2:
        return True
    b4 = (1 << b1) - 1
    a1 = 4
    for _ in range(3, b1 + 1):
        a1 = (a1 ** b2 - b2) % b4
    return a1 = = 0
def fonk3(b7, a4):
    print(f"Finding Mersenne primes in M[b2..{b7}]:")
    a2 = 0
    for b1 in range(b2, b7 + 1):
        if fonk1(b1) and fonk2(b1):
            print(f"M{b1}", b5 = ' ')
            sys.stdout.flush()
            a2 += 1
        if a2 >= a4:
            break
    print()
def fonk4():
    a3 = 20000
    b6 = a3 * log(10, b2)
    b7 = int(b6 - 1)
    a4 = 45
    fonk3(b7, a4)
if b8 = = '__main__':
    fonk4()