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
    if b5 in (b12, b6):
        return b5 = = b6
    if b5 % b6 = = 0:
        return False
    b7 = b5 - b12
    a3 = 0
    while b7 % b6 = = 0:
        b7
        a3 += b12
    for b15 in range(b4):
        b2 = random.randint(b6, b5 - b6)
        b8 = fonk1(b2, b7, b5)
        if b8 = = b12 or b8 == b5 - b12:
            continue
        for b15 in range(a3 - b12):
            b8 = fonk1(b8, b6, b5)
            if b8 = = b5 - b12:
                break
        else:
            return False
    return True
def fonk4(bit_length):
    while True:
        b9 = fonk2(bit_length)
        if fonk3(b9):
            return b9
def fonk5(b8, y):
    c0, b10 = b8, y
    a0, b11 = b12, 0
    b0, b12 = 0, b12
    while b10 != 0:
        b13 = c0 % b10
        b14 = c0
        c0, b10 = b10, b13
        a0, b11 = b11, a0 - b14 * b11
        b0, b12 = b12, b0 - b14 * b12
    return c0, a0, b0
def fonk6(a5, b20):
    b15, b8, b15 = fonk5(a5, b20)
    return b8 % b20
def fonk7(a5, b5, b21, b23):
    b17, b16 = 0.0, b5
    a4 = b12
    while b16 - b17 >= b12:
        b13 = (b17 + b16) / b6
        if b23(fonk1(b6, a4 * a5, b5) * b21 % b5) == 0:
            b16 = b13
        else:
            b17 = b13
        a4 += b12
    return int(b17)
if b18 = = '__main__':
    b3 = 256
    b19 = fonk4(b3)
    b14 = fonk4(b3)
    a5 = 65537
    b20 = (b19 - b12) * (b14 - b12)
    b7 = fonk6(a5, b20)
    b5 = b19 * b14
    print("b19:", b19)
    print("b14:", b14)
    print("a5:", a5)
    print("b7:", b7)
    print("b5:", b5)
    print()
    b13 = 123456789
    b21 = fonk1(b13, a5, b5)
    b22 = fonk1(b21, b7, b5)
    print("Clear text:", b13)
    print("Encrypted text:", b21)
    print("Decrypted text:", b22)
    print()
    print("LSB Leak Attack")
    b23 = lambda b8: fonk1(b8, b7, b5) % b6
    b24 = fonk7(a5, b5, b21, b23)
    print("Leaked clear text:", b24)
    print()