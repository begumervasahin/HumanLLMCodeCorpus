import random
def fonk1(b1, exp, mod):
    a1 = 1
    while exp > 0:
        if exp & 1:
            a1 = (a1 * b1) % mod
        b1 = (b1 * b1) % mod
        exp >>= 1
    return a1
def fonk2(a5):
    b2 = [random.randint(0, 1) for b12 in range(a5 - b5)]
    a1 = 1
    for bit in b2:
        a1 = a1 * b5 + bit
    return a1 * b5 + 1
def fonk3(b4, b3 = 100):
    if b4 in (b5, 3):
        return True
    if b4 = = 1 or b4 % b5 == 0:
        return False
    def fonk4(b4):
        a2 = 0
        while b4 % b5 = = 0:
            b4
            a2 += 1
        return b4, a2
    def fonk5(b1, b4, b13, b6):
        if fonk1(b1, b13, b4) == 1:
            return False
        for i in range(b6):
            if fonk1(b1, b13 * (b5 ** i), b4) == b4 - 1:
                return False
        return True
    b13, b6 = fonk4(b4 - 1)
    for b12 in range(b3):
        b1 = random.randint(b5, b4 - b5)
        if fonk5(b1, b4, b13, b6):
            return False
    return True
def fonk6(a5):
    while True:
        b7 = fonk2(a5)
        if fonk3(b7):
            return b7
def fonk7(a, b8):
    while b8:
        a, b8 = b8, a % b8
    return a
def fonk8(a, b8):
    old_r, b9 = a, b8
    old_s, b6 = 1, 0
    old_t, b10 = 0, 1
    while b9 != 0:
        b11 = old_r
        old_r, b9 = b9, old_r - b11 * b9
        old_s, b6 = b6, old_s - b11 * b6
        old_t, b10 = b10, old_t - b11 * b10
    return old_r, old_s, old_t
def fonk9(a3, b18):
    gcd, b14, b12 = fonk8(a3, b18)
    return b14 % b18
def fonk10(b4):
    def fonk11(b14):
        return (b14 * b14 + 1) % b4
    b14, b15, b13 = b5, b5, 1
    while b13 = = 1:
        b14 = fonk11(b14)
        b15 = fonk11(fonk11(b15))
        b13 = fonk7(abs(b14 - b15), b4)
    return b13
def fonk12(b4, a3, b20):
    b16 = fonk10(b4)
    b17 = b4
    b18 = (b16 - 1) * (b17 - 1)
    b13 = fonk9(a3, b18)
    return b16, b17, b13
if b19 = = '__main__':
    a3 = 65537
    a4 = 123456789
    a5 = 10
    b16 = fonk6(a5)
    b17 = fonk6(a5)
    b4 = b16 * b17
    b18 = (b16 - 1) * (b17 - 1)
    b13 = fonk9(a3, b18)
    b20 = fonk1(a4, a3, b4)
    print("Initial values:")
    print("a3:", a3)
    print("b4:", b4)
    b16, b17, b13 = fonk12(b4, a3, b20)
    print("Simple attack results:")
    print("Primes:", b16, b17)
    print("Decryption a2:", b13)