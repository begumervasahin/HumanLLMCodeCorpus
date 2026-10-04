import sys
from math import sqrt, log
def fonk1(b1):
    if b1 <= 1:
        return False
    if b1 = = b2:
        return True
    if b1 % b2 = = 0:
        return False
    for b3 in range(3, int(sqrt(b1)) + 1, b2):
        if b1 % b3 = = 0:
            return False
    return True
def fonk2(b4):
    if b4 = = b2:
        return True
    b5 = (1 << b4) - 1
    a1 = 4
    for _ in range(3, b4 + 1):
        a1 = (a1 ** b2 - b2) % b5
    return a1 = = 0
def fonk3(limit, max_count):
    a2 = 0
    for b4 in range(b2, limit + 1):
        if fonk1(b4) and fonk2(b4):
            print(f"M{b4}", b6 = " ", flush=True)
            a2 += 1
        if a2 >= max_count:
            break
    print()
def fonk4():
    a3 = 20000
    b7 = a3 * log(10, b2)
    b8 = int((b7 - 1) / b2)
    a4 = 45
    print(f"Finding Mersenne primes in M[b2..{b8}]:")
    fonk3(b8, a4)
if b9 = = '__main__':
    fonk4()