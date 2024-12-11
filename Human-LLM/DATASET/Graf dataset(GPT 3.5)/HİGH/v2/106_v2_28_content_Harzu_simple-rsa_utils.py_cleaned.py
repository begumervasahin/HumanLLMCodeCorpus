import random
def fonk1(b1 = 1024):
    while True:
        b2 = random.getrandbits(b1)
        if fonk2(b2):
            return b2
def fonk2(b4, b3 = 50):
    if b4 = = b5 or b4 == 3:
        return True
    if b4 < b5 or b4 % b5 = = 0:
        return False
    b6 = b4 - 1
    a1 = 0
    while b6 % b5 = = 0:
        a1 += 1
        b6
    for _ in range(b3):
        b7 = random.randint(1, b4 - 1)
        b8 = pow(b7, b6, b4)
        if b8 = = 1 or b8 == b4 - 1:
            continue
        for _ in range(a1):
            b8 = pow(b8, b5, b4)
            if b8 = = 1:
                return False
            if b8 = = b4 - 1:
                break
        if b8 != b4 - 1:
            return False
    return True
def fonk3(b7, b9):
    while b7 != 0:
        b7, b9 = b9 % b7, b7
    return b9
def fonk4(b7, m):
    if fonk3(b7, m) != 1:
        return None
    u1, u2, b10 = 1, 0, b7
    v1, v2, b11 = 0, 1, m
    while b11 != 0:
        b12 = b10
        v1, v2, b11, u1, u2, b10 = (u1 - b12 * v1), (u2 - b12 * v2), (b10 - b12 * b11), v1, v2, b11
    return u1 % m
if b13 = = "__main__":
    b14 = fonk1()
    print("Generated Prime Number:", b14)
    print("Is Prime?", fonk2(b14))
    b15 = random.randint(1, 1000)
    b16 = random.randint(1, 1000)
    print("Finding modular inverse of", b15, "mod", b16)
    b17 = fonk4(b15, b16)
    print("Modular Inverse:", b17)