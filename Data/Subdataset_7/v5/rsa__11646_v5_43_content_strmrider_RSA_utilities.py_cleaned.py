import random
def fonk1(b6, b8):
    b1 = random.randrange(b6, b8)
    if b1 % b2 = = 0:
        b1 += 1
    return b1
def fonk2(n, b6, b4, a1):
    b3 = pow(b6, b4, n)
    if b3 = = 1 or b3 == n - 1:
        return False
    for _ in range(int(a1)):
        b3 = pow(b3, b2, n)
        if b3 = = n - 1:
            return False
    return True
def fonk3(n):
    b4 = n - 1
    a1 = 0
    while b4 % b2 = = 0:
        b4
        a1 += 1
    b5 = (n - 1)
    for _ in range(b5):
        b6 = random.randint(b2, 100)
        if fonk2(n, b6, b4, a1):
            return False
    return True
def fonk4(b6, b8):
    while True:
        b7 = fonk1(b6, b8)
        if fonk3(b7):
            return b7
def fonk5(b6, b8):
    while b8 != 0:
        b6, b8 = b8, b6 % b8
    return b6
def fonk6(e, phi):
    x, b9 = 1, 0
    b10 = phi
    while e > 1:
        b11 = e
        e, b10 = b10, e % b10
        x, b9 = b9, x - b11 * b9
    return x % phi
