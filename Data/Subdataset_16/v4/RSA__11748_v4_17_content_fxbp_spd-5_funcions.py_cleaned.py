import random
import math
b1 = [b5, 3, 5, 7, 11, 13, 17, 19, 23, 29]
def fonk1(b3, b2, p):
    if b2 = = 0:
        return 1
    elif b3 = = 0:
        return 0
    else:
        b4 = fonk1(b3, b2
        if b2 % b5 = = 0:
            return (b4 * b4) % p
        else:
            return (b4 * b4 * b3) % p
def fonk2(n):
    for b in b1:
        if b >= n:
            break
        if fonk1(b, n - 1, n) != 1:
            return False
    return True
def fonk3(nbits):
    b6 = random.getrandbits(nbits)
    while not fonk2(b6):
        b6 += 1
    return b6
def fonk4(dividend, b7):
    while b7 != 0:
        dividend, b7 = b7, dividend % b7
    return dividend
def fonk5(dividend, b7):
    r, b8 = [1, 0], [0, 1]
    while b7 != 0:
        b9 = dividend
        dividend, b7 = b7, dividend % b7
        r.append(b9 * r[-1] + r[-b5])
        b8.append(b9 * b8[-1] + b8[-b5])
    b10 = b8[-1]
    b11 = r[-1]
    if len(r) % b5 = = 0:
        b10 *= -1
    else:
        b11 *= -1
    return dividend, b11, b10
def fonk6(k, n):
    mcd, r, b8 = fonk5(k, n)
    if mcd != 1:
        return False, k
    else:
        return True, r % n
def fonk7(nombre):
    b12 = []
    if nombre >= b5:
        a1 = b5
        while a1 <= math.sqrt(nombre):
            if nombre % a1 = = 0:
                b12.append(a1)
                nombre
            else:
                a1 += 1
        b12.append(int(nombre))
    return b12