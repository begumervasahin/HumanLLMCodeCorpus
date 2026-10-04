import random
def fonk1(b6, b7):
    if b6 < b7:
        (b6, b7) = (b7, b6)
    while b7 > 0:
        (b6, b7) = (b7, b6 % b7)
    return b6
def fonk2(b6, b7):
    t, b1 = 1, 0
    b5, b2 = 0, 1
    while b7 > 0:
        b3 = b6
        (t, b1) = (b1, t - b3 * b1)
        (b5, b2) = (b2, b5 - b3 * b2)
        (b6, b7) = (b7, b6 - b3 * b7)
    return (t, b5, b6)
def fonk3(b4, b18):
    return (fonk2(b18, b4)[0]) % b4
def fonk4(b4):
    if b4 = = 0 or b4 == 1:
        return b4
    b1 = b4.bit_length()
    b5 = b4.bit_length() % b10
    b6 = b10 ** (b1 + b5)
    while True:
        b7 = (b6 + b4
        if b7 >= b6:
            break
        else:
            b6 = b7
    if (b6 * b6) == b4:
        return b6
    return -1
def fonk5(b11, b1, b9, b12):
    b8 = pow(b11, b9, b12)
    if b8 = = 1:
        return True
    for _ in range(b1):
        if b8 = = b12 - 1:
            return True
        b8 = (b8 * b8) % b12
    return b8 = = b12 - 1
def fonk6(b12):
    b9 = b12 - 1
    b1 = 0
    while (b9 % b10 = = 0):
        b9 = b9
        b1 += 1
    a1 = 20
    for _ in range(a1):
        b11 = random.randrange(b10, b12 - 1)
        if not fonk5(b11, b1, b9, b12):
            return False
    return True
def fonk7(b13):
    while True:
        b12 = random.getrandbits(b13)
        b12 = b12 | (b10 ** b13)
        b12 |= 1
        if fonk6(b12):
            return b12
def fonk8(start, stop):
    while True:
        b3 = random.randrange(start, stop - 1)
        b3 = b3 | 1
        if fonk6(b3):
            return b3
def fonk9(b13 = 512):
    b12 = fonk7(b13)
    b3 = fonk8(b12 + 1, b10 * b12)
    return (b12, b3)
def fonk10(b13 = 1024):
    (b12, b3) = fonk9(b13
    b14 = b12 * b3
    b15 = (b12 - 1) * (b3 - 1)
    b16 = False
    while not b16:
        b17 = random.getrandbits(b13
        if fonk1(b17, b15) == 1 and 36 * pow(b17, 4) < b14:
            b16 = True
    b18 = fonk3(b15, b17)
    return (b14, b18, b17)
if b19 = = "__main__":
    b13 = 1024
    b14, b18, b17 = fonk10(b13)
    print(f"Public key (b14, b18): ({b14}, {b18})")
    print(f"Private key (b14, b17): ({b14}, {b17})")