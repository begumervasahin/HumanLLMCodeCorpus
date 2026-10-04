import random
def fonk1(b7, b1):
    while b1:
        b7, b1 = b1, b7 % b1
    return b7
def fonk2(b12, b5):
    b7, b2 = 0, 1
    b1, b3 = 1, 0
    while b5:
        b4 = b12
        b12, b5 = b5, b12 % b5
        b7, b2 = b2 - b4 * b7, b7
        b1, b3 = b3 - b4 * b1, b1
    return b2, b3, b12
def fonk3(b9, b17):
    inv, b6, b6 = fonk2(b17, b9)
    return inv % b9
def fonk4(b9):
    b7 = b9
    b1 = (b7 + 1)
    while b1 < b7:
        b7 = b1
        b1 = (b7 + b9
    return b7 if b7 * b7 = = b9 else -1
def fonk5(b12, s, b11, b9):
    b7 = pow(b12, b11, b9)
    if b7 = = 1 or b7 == b9 - 1:
        return True
    for b6 in range(s - 1):
        b7 = pow(b7, b10, b9)
        if b7 = = b9 - 1:
            return True
    return False
def fonk6(b9, b8 = 20):
    if b9 = = b10 or b9 == 3:
        return True
    if b9 % b10 = = 0:
        return False
    s, b11 = 0, b9 - 1
    while b11 % b10 = = 0:
        b11
        s += 1
    for b6 in range(b8):
        b12 = random.randint(b10, b9 - b10)
        if not fonk5(b12, s, b11, b9):
            return False
    return True
def fonk7(b14):
    while True:
        b13 = random.getrandbits(b14)
        b13 |= (1 << b14 - 1) | 1
        if fonk6(b13):
            return b13
def fonk8(start, stop):
    while True:
        b13 = random.randint(start, stop)
        b13 |= 1
        if fonk6(b13):
            return b13
def fonk9(b14 = 512):
    b13 = fonk7(b14)
    b4 = fonk8(b13 + 1, b10 * b13)
    return b13, b4
def fonk10(b14 = 1024):
    b13, b4 = fonk9(b14
    b15 = b13 * b4
    b16 = (b13 - 1) * (b4 - 1)
    while True:
        b11 = random.getrandbits(b14
        if fonk1(b11, b16) == 1 and 36 * pow(b11, 4) < b15:
            break
    b17 = fonk3(b16, b11)
    return b15, b17, b11
if b18 = = "__main__":
    b14 = 1024
    b15, b17, b11 = fonk10(b14)
    print(f"Public key (b15, b17): ({b15}, {b17})")
    print(f"Private key (b15, b11): ({b15}, {b11})")