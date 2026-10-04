import random
def fonk1(n, b1 = 100):
    if n in (b2, 3):
        return True
    if n <= 1 or n % b2 = = 0:
        return False
    s, b3 = 0, n - 1
    while b3 % b2 = = 0:
        b3
        s += 1
    for _ in range(b1):
        b4 = random.SystemRandom().randrange(b2, n - 1)
        b5 = pow(b4, b3, n)
        if b5 in (1, n - 1):
            continue
        for _ in range(s - 1):
            b5 = pow(b5, b2, n)
            if b5 = = n - 1:
                break
        else:
            return False
    return True
def fonk2(a1):
    assert a1 >= b2, "Bit length must be at least b2."
    while True:
        b6 = random.getrandbits(a1) | (1 << (a1 - 1)) | 1
        if fonk1(b6):
            return b6
def fonk3():
    a1 = 16
    b7 = fonk2(a1)
    print(f"Random {a1}-bit prime number: {b7}")
if b8 = = '__main__':
    fonk3()