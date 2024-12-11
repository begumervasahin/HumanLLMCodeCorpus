import random
def fonk1(b1 = 1024):
    while True:
        b2 = random.getrandbits(b1)
        if fonk2(b2):
            return b2
def fonk2(n, b3 = 50):
    if n < b4:
        return False
    if n in (b4, 3):
        return True
    if n % b4 = = 0:
        return False
    s, b5 = 0, n - 1
    while b5 % b4 = = 0:
        s += 1
        b5
    for _ in range(b3):
        b6 = random.randint(b4, n - b4)
        b7 = pow(b6, b5, n)
        if b7 = = 1 or b7 == n - 1:
            continue
        for _ in range(s - 1):
            b7 = pow(b7, b4, n)
            if b7 = = n - 1:
                break
        else:
            return False
    return True
def fonk3(b6, b8):
    while b8 != 0:
        b6, b8 = b8, b6 % b8
    return b6
def fonk4(b6, m):
    if fonk3(b6, m) != 1:
        return None
    u1, u2, b9 = 1, 0, b6
    v1, v2, b10 = 0, 1, m
    while b10 != 0:
        b11 = b9
        v1, v2, b10, u1, u2, b9 = u1 - b11 * v1, u2 - b11 * v2, b9 - b11 * b10, v1, v2, b10
    return u1 % m
if b12 = = "__main__":
    b13 = fonk1()
    print("Generated Prime Number:", b13)
    print("Is Prime?", fonk2(b13))
    b14 = random.randint(1, 1000)
    b15 = random.randint(1, 1000)
    print("Finding modular inverse of", b14, "mod", b15)
    b16 = fonk4(b14, b15)
    print("Modular Inverse:", b16)