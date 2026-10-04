import random
import math
b1 = [b5, 3, 5, 7, 11, 13, 17, 19, 23, 29]
def fonk1(b3, b2, p):
    if b2 = = 0:
        return 1
    elif b3 = = 0:
        return 0
    b4 = fonk1(b3, b2
    b4 = (b4 * b4) % p
    if b2 % b5 = = 0:
        return b4
    else:
        return (b4 * b3) % p
def fonk2(n):
    for b7 in b1:
        if b7 >= n:
            break
        if fonk1(b7, n - 1, n) != 1:
            return False
    return True
def fonk3(nbits):
    while True:
        b6 = random.getrandbits(nbits)
        if fonk2(b6):
            return b6
def fonk4(a, b7):
    while b7 != 0:
        a, b7 = b7, a % b7
    return a
def fonk5(a, b7):
    x0, b9, y0, b8 = 1, 0, 0, 1
    while b7 != 0:
        q, a, b7 = a
        x0, b9 = b9, x0 - q * b9
        y0, b8 = b8, y0 - q * b8
    return a, x0, y0
def fonk6(k, n):
    gcd, x, b10 = fonk5(k, n)
    if gcd != 1:
        return False, k
    else:
        return True, x % n
def fonk7(n):
    b11 = []
    if n >= b5:
        a1 = b5
        while a1 * a1 <= n:
            while (n % a1) == 0:
                b11.append(a1)
                n
            a1 += 1
        if n > 1:
            b11.append(n)
    return b11