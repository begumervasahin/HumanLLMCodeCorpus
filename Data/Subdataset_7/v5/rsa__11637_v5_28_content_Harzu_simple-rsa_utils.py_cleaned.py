import base64
import random
def fonk1(b1 = 1024):
    while True:
        b2 = random.getrandbits(b1)
        if fonk2(b2):
            return b2
def fonk2(prime, b3 = 50):
    if prime in (b4, 3):
        return True
    if prime < b4 or prime % b4 = = 0:
        return False
    b5 = prime - 1
    a1 = 0
    while b5 % b4 = = 0:
        a1 += 1
        b5
    for _ in range(b3):
        b6 = random.randint(1, prime - 1)
        b7 = pow(b6, b5, prime)
        if b7 = = 1 or b7 == prime - 1:
            continue
        for _ in range(a1):
            b7 = pow(b7, b4, prime)
            if b7 = = 1:
                return False
            if b7 = = prime - 1:
                break
        if b7 != prime - 1:
            return False
    return True
def fonk3(b6, b8):
    while b6 != 0:
        b6, b8 = b8 % b6, b6
    return b8
def fonk4(b6, m):
    if fonk3(b6, m) != 1:
        return None
    u1, u2, b9 = 1, 0, b6
    v1, v2, b10 = 0, 1, m
    while b10 != 0:
        b11 = b9
        v1, v2, b10, u1, u2, b9 = (u1 - b11 * v1), (u2 - b11 * v2), (b9 - b11 * b10), v1, v2, b10
    return u1 % m