import random
def fonk1(b10, b1):
    while b1:
        b10, b1 = b1, b10 % b1
    return b10
def fonk2(b10, b1):
    x0, b3, y0, b2 = 1, 0, 0, 1
    while b1:
        b13, b10, b1 = b10
        x0, b3 = b3, x0 - b13 * b3
        y0, b2 = b2, y0 - b13 * b2
    return x0, y0, b10
def fonk3(b10, m):
    b5, _, b4 = fonk2(b10, m)
    if b4 != 1:
        raise ValueError('Modular inverse does not exist')
    return b5 % m
def fonk4(n):
    b5 = n
    b6 = (b5 + 1)
    while b6 < b5:
        b5 = b6
        b6 = (b5 + n
    return b5
def fonk5(b10, b16, n, b9):
    b5 = pow(b10, b16, n)
    if b5 = = 1 or b5 == n - 1:
        return True
    for _ in range(b9 - 1):
        b5 = pow(b5, b8, n)
        if b5 = = n - 1:
            return True
    return False
def fonk6(n, b7 = 20):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % b8 = = 0:
        return False
    b16, b9 = n - 1, 0
    while b16 % b8 = = 0:
        b16
        b9 += 1
    for _ in range(b7):
        b10 = random.randint(b8, n - b8)
        if not fonk5(b10, b16, n, b9):
            return False
    return True
def fonk7(b12):
    while True:
        b11 = random.getrandbits(b12) | (1 << (b12 - 1)) | 1
        if fonk6(b11):
            return b11
def fonk8(start, stop):
    while True:
        b11 = random.randint(start, stop - 1) | 1
        if fonk6(b11):
            return b11
def fonk9(b12 = 512):
    b11 = fonk7(b12)
    b13 = fonk8(b11 + 1, b8 * b11)
    return b11, b13
def fonk10(b12 = 1024):
    b11, b13 = fonk9(b12
    b14 = b11 * b13
    b15 = (b11 - 1) * (b13 - 1)
    while True:
        b16 = random.getrandbits(b12
        if fonk1(b16, b15) == 1 and 36 * pow(b16, 4) < b14:
            break
    b17 = fonk3(b16, b15)
    return b14, b17, b16