import random
def fonk1(b7, b1):
    if b7 < b1:
        b7, b1 = b1, b7
    while b1 > 0:
        b7, b1 = b1, b7 % b1
    return b7
def fonk2(b7, b1):
    t, b2 = 1, 0
    b6, b3 = 0, 1
    while b1 > 0:
        b4 = b7
        t, b2 = b2, t - b4 * b2
        b6, b3 = b3, b6 - b4 * b3
        b7, b1 = b1, b7 - b4 * b1
    return t, b6, b7
def fonk3(b5, b19):
    return fonk2(b19, b5)[0] % b5
def fonk4(b5):
    if b5 = = 0 or b5 == 1:
        return b5
    b2 = b5.bit_length()
    b6 = b5.bit_length() % b11
    b7 = b11 ** (b2 + b6)
    while True:
        b1 = (b7 + b5
        if b1 >= b7:
            break
        else:
            b7 = b1
    if b7 * b7 = = b5:
        return b7
    return -1
def fonk5(b12, b2, b10, b13):
    b8 = pow(b12, b10, b13)
    if b8 = = 1:
        return True
    for _ in range(b2):
        if b8 = = b13 - 1:
            return True
        b8 = (b8 * b8) % b13
    return b8 = = b13 - 1
def fonk6(b13, b9 = 20):
    b10 = b13 - 1
    b2 = 0
    while b10 % b11 = = 0:
        b10
        b2 += 1
    for _ in range(b9):
        b12 = random.randrange(b11, b13 - 1)
        if not fonk5(b12, b2, b10, b13):
            return False
    return True
def fonk7(b14):
    while True:
        b13 = random.getrandbits(b14)
        b13 |= (1 << (b14 - 1)) | 1
        if fonk6(b13):
            return b13
def fonk8(start, stop):
    while True:
        b4 = random.randrange(start, stop)
        b4 |= 1
        if fonk6(b4):
            return b4
def fonk9(b14 = 512):
    b13 = fonk7(b14)
    b4 = fonk8(b13 + 1, b11 * b13)
    return b13, b4
def fonk10(b14 = 1024):
    b13, b4 = fonk9(b14
    b15 = b13 * b4
    b16 = (b13 - 1) * (b4 - 1)
    b17 = False
    while not b17:
        b18 = random.getrandbits(b14
        if fonk1(b18, b16) == 1 and 36 * pow(b18, 4) < b15:
            b17 = True
    b19 = fonk3(b16, b18)
    return b15, b19, b18