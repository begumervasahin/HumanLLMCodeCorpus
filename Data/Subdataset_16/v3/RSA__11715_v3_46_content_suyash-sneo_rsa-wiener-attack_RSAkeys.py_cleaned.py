import random
def fonk1(b7, b1):
    while b1:
        b7, b1 = b1, b7 % b1
    return b7
def fonk2(b11, b5):
    b7, b2 = 0, 1
    b1, b3 = 1, 0
    while b5:
        b4 = b11
        b11, b5 = b5, b11 % b5
        b7, b2 = b2 - b4 * b7, b7
        b1, b3 = b3 - b4 * b1, b1
    return b2, b3, b11
def fonk3(n, b16):
    inv, b6, b6 = fonk2(b16, n)
    return inv % n
def fonk4(n):
    b7 = n
    b1 = (b7 + 1)
    while b1 < b7:
        b7 = b1
        b1 = (b7 + n
    return b7 if b7 * b7 = = n else -1
def fonk5(b11, s, b10, n):
    b7 = pow(b11, b10, n)
    if b7 = = 1 or b7 == n - 1:
        return True
    for b6 in range(s - 1):
        b7 = pow(b7, b9, n)
        if b7 = = n - 1:
            return True
    return False
def fonk6(n, b8 = 20):
    if n in (b9, 3):
        return True
    if n % b9 = = 0 or n < b9:
        return False
    s, b10 = 0, n - 1
    while b10 % b9 = = 0:
        b10
        s += 1
    for b6 in range(b8):
        b11 = random.randint(b9, n - b9)
        if not fonk5(b11, s, b10, n):
            return False
    return True
def fonk7(b13):
    while True:
        b12 = random.getrandbits(b13)
        b12 |= (1 << b13 - 1) | 1
        if fonk6(b12):
            return b12
def fonk8(start, stop):
    while True:
        b12 = random.randint(start, stop)
        b12 |= 1
        if fonk6(b12):
            return b12
def fonk9(b13 = 512):
    b12 = fonk7(b13)
    b4 = fonk8(b12 + 1, b9 * b12)
    return b12, b4
def fonk10(b13 = 1024):
    b12, b4 = fonk9(b13
    b14 = b12 * b4
    b15 = (b12 - 1) * (b4 - 1)
    while True:
        b10 = random.getrandbits(b13
        if fonk1(b10, b15) == 1 and 36 * pow(b10, 4) < b14:
            break
    b16 = fonk3(b15, b10)
    return b14, b16, b10
if b17 = = "__main__":
    b13 = 1024
    b14, b16, b10 = fonk10(b13)
    print(f"Public key (b14, b16): ({b14}, {b16})")
    print(f"Private key (b14, b10): ({b14}, {b10})")