import random
def fonk1(b2, b12, b5):
    a1 = b1
    while b12 > 0:
        if b12 & b1 = = b1:
            a1 = (a1 * b2) % b5
        b2 = (b2 * b2) % b5
        b12 >>= b1
    return a1
def fonk2(a6):
    b3 = [random.randint(0, b1) for b13 in range(a6 - b6)]
    a2 = b1
    for b12 in b3:
        a2 = a2 * b6 + int(b12)
    return a2 * b6 + b1
def fonk3(b5, b4 = 100):
    if b5 = = b1:
        return False
    if b5 = = b6:
        return True
    if b5 % b6 = = 0:
        return False
    b7 = b5 - b1
    a3 = 0
    while b7 % b6 = = 0:
        b7
        a3 += b1
    def fonk4(b2, b7, b5, a3):
        if fonk1(b2, b7, b5) == b1:
            return False
        for i in range(a3):
            if fonk1(b2, b7 * (b6 ** i), b5) == b5 - b1:
                return False
        return True
    for b13 in range(b4):
        b2 = random.randint(b6, b5 - b6)
        if fonk4(b2, b7, b5, a3):
            return False
    return True
def fonk5(a6):
    while True:
        b8 = fonk2(a6)
        if fonk3(b8):
            return b8
def fonk6(b14, b9):
    while b9 != 0:
        b14, b9 = b9, b14 % b9
    return b14
def fonk7(b2, b12):
    x0, b10 = b1, 0
    y0, b11 = 0, b1
    while b12 != 0:
        b16, b2, b12 = b2
        x0, b10 = b10, x0 - b16 * b10
        y0, b11 = b11, y0 - b16 * b11
    return b2, x0, y0
def fonk8(a4, b17):
    b13, b14, b13 = fonk7(a4, b17)
    return b14 % b17
def fonk9(b5):
    def fonk10(b14):
        return (b14 * b14 + b1) % b5
    b14, b9, b7 = b6, b6, b1
    while b7 = = b1:
        b14 = fonk10(b14)
        b9 = fonk10(fonk10(b9))
        b7 = fonk6(abs(b14 - b9), b5)
    return b7
def fonk11(b5, a4, b19):
    b15 = fonk9(b5)
    b16 = b5
    b17 = (b15 - b1) * (b16 - b1)
    b7 = fonk8(a4, b17)
    return b15, b16, b7
if b18 = = '__main__':
    a4 = 65537
    a5 = 123456789
    a6 = 10
    b15 = fonk5(a6)
    b16 = fonk5(a6)
    b5 = b15 * b16
    b17 = (b15 - b1) * (b16 - b1)
    b7 = fonk8(a4, b17)
    b19 = fonk1(a5, a4, b5)
    print("Initial values:")
    print("a4:", a4)
    print("b5:", b5)
    b15, b16, b7 = fonk11(b5, a4, b19)
    print("Simple attack results:")
    print("Primes:", b15, b16)
    print("Decryption exponent:", b7)