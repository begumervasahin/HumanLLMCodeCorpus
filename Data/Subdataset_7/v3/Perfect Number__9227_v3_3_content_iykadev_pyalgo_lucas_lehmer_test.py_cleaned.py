from sys import stdout
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
def fonk2(b4):
    if b4 = = b2:
        return True
    else:
        b5 = (1 << b4) - 1
        a1 = 4
        for b3 in range(3, b4 + 1):
            a1 = (a1 ** b2 - b2) % b5
        return a1 = = 0
def fonk3(b9, a4):
    print("Finding Mersenne primes in M[b2..%d]:" % b9)
    a2 = 0
    for b4 in range(b2, int(b9 + 1)):
        if fonk1(b4) and fonk2(b4):
            print("M%d" % b4, b6 = " ")
            stdout.flush()
            a2 += 1
        if a2 >= a4:
            break
    print()
if b7 = = "__main__":
    a3 = 20000
    b8 = a3 * log(10, b2)
    b9 = int(b8 - 1) / b2
    a4 = 45
    fonk3(b9, a4)