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
a2 = 20000
b6 = a2 * log(10, b2)
b7 = int(b6 - 1) / b2
a3 = 45
print("Finding Mersenne primes in M[b2..%d]:" % b7)
a4 = 0
for b4 in range(b2, int(b7 + 1)):
    if fonk1(b4) and fonk2(b4):
        print("M%d" % b4, b8 = " ")
        stdout.flush()
        a4 += 1
    if a4 >= a3:
        break
print()