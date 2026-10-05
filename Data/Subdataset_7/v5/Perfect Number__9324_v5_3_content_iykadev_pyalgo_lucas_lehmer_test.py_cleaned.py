import sys
import math
def fonk1(b1):
    if b1 = = b2:
        return True
    elif b1 <= 1 or b1 % b2 = = 0:
        return False
    else:
        for b3 in range(3, int(math.sqrt(b1)) + 1, b2):
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
def fonk3(b8, a4):
    print("Finding Mersenne primes in M[b2..%d]:" % b8)
    a2 = 0
    for b1 in range(b2, int(b8 + 1)):
        if fonk1(b1) and fonk2(b1):
            print("M%d" % b1, b5 = ' ')
            sys.stdout.flush()
            a2 += 1
        if a2 >= a4:
            break
    print()
if b6 = = "__main__":
    a3 = 20000
    b7 = a3 * math.log(10, b2)
    b8 = int(b7 - 1) / b2
    a4 = 45
    fonk3(b8, a4)