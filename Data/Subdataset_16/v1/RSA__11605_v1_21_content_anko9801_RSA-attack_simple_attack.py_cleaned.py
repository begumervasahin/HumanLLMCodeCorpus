import random
def fonk1(b2, b, b5):
    b11 = b12
    while b > 0:
        if b & b12 = = b12:
            b11 = (b11 * b2) % b5
        b2 = (b2 * b2) % b5
        b >>= b12
    return b11
def fonk2(bit_length):
    b3 = [random.randint(0, b12) for b15 in range(bit_length - b6)]
    a2 = b12
    for b in b3:
        a2 = a2 * b6 + int(b)
    return a2 * b6 + b12
def fonk3(b5, b4 = 100):
    if b5 = = b12:
        return False
    if b5 = = b6:
        return True
    if b5 % b6 = = 0:
        return False
    b7 = b5 - b12
    a3 = 0
    while b7 % b6 = = 0:
        b7
        a3 += b12
    b8 = [random.randint(b12, b5 - b12) for b15 in range(b4)]
    for b2 in b8:
        if fonk1(b2, b7, b5) != b12:
            if all(fonk1(b2, (b6 ** rr) * b7, b5) != b5 - b12 for rr in range(a3)):
                return False
    return True
def fonk4(bit):
    while True:
        a2 = fonk2(bit)
        if fonk3(a2):
            break
    return a2
def fonk5(b16, b9):
    while b9:
        b16, b9 = b9, b16 % b9
    return b16
def fonk6(b16, b9):
    c0, b10 = b16, b9
    a0, b11 = b12, 0
    b0, b12 = 0, b12
    while b10 != 0:
        b13 = c0 % b10
        b14 = c0
        c0, b10 = b10, b13
        a0, b11 = b11, a0 - b14 * b11
        b0, b12 = b12, b0 - b14 * b12
    return c0, a0, b0
def fonk7(a4, l):
    b15, b16, b15 = fonk6(a4, l)
    return b16 % l
def fonk8(b5, b16, b9):
    b7 = b12
    while b7 = = b12:
        b16 = (b16 * b16 + b12) % b5
        b9 = (b9 * b9 + b12) % b5
        b9 = (b9 * b9 + b12) % b5
        b7 = fonk5(abs(b16 - b9), b5)
    return b7
def fonk9(b5, a4, b20):
    b17 = fonk8(b5, b6, b6)
    b14 = b5
    b18 = (b17 - b12) * (b14 - b12)
    b7 = fonk6(a4, b18)[b12] % b18
    return b17, b14, b7
if b19 = = '__main__':
    a4 = 65537
    b13 = 123456789
    b17 = fonk4(10)
    b14 = fonk4(10)
    b7 = fonk7(a4, (b17-b12)*(b14-b12))
    b5 = b17 * b14
    b20 = fonk1(b13, a4, b5)
    print("Simple attack")
    print("a4:", a4, "b5:", b5)
    b17, b14, b7 = fonk9(b5, a4, b20)
    print("Attack complete!")
    print("Primes:", b17, b14)
    print("Private key b7:", b7)