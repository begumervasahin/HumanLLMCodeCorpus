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
    b5 = (n - 1) / 4
    for a3 in range(0, b5):
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
    if b8 = = 0:
        return b6
    else:
        return fonk5(b8, b6 % b8)
def fonk6(b12, phi):
    b9 = phi
    a2 = 0
    a3 = 1
    while b12 > 1:
        b10 = b12
        b11 = b9
        b9 = b12 % b9
        b12 = b11
        b11 = a2
        a2 = a3 - (b10 * a2)
        a3 = b11
    if a3 < 0:
        a3 += phi
    return a3