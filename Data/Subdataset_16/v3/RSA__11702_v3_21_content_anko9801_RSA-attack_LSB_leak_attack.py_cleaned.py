import random
def fonk1(b1, b9, b17):
    a1 = 1
    while b9 > 0:
        if b9 & 1:
            a1 = (a1 * b1) % b17
        b1 = (b1 * b1) % b17
        b9 >>= 1
    return a1
def fonk2(a4):
    b2 = [random.randint(0, 1) for b11 in range(a4 - b4)]
    a2 = 1
    for bit in b2:
        a2 = a2 * b4 + bit
    return a2 * b4 + 1
def fonk3(b17, b3 = 100):
    if b17 in (b4, 3):
        return True
    if b17 % b4 = = 0 or b17 == 1:
        return False
    b19, b5 = b17 - 1, 0
    while b19 % b4 = = 0:
        b19
        b5 += 1
    for b11 in range(b3):
        b1 = random.randint(b4, b17 - b4)
        b6 = fonk1(b1, b19, b17)
        if b6 = = 1 or b6 == b17 - 1:
            continue
        for b11 in range(b5 - 1):
            b6 = fonk1(b6, b4, b17)
            if b6 = = b17 - 1:
                break
        else:
            return False
    return True
def fonk4(a4):
    while True:
        b7 = fonk2(a4)
        if fonk3(b7):
            return b7
def fonk5(b1, b9):
    x0, b10, y0, b8 = 1, 0, 0, 1
    while b9 != 0:
        b16, b1, b9 = b1
        x0, b10 = b10, x0 - b16 * b10
        y0, b8 = b8, y0 - b16 * b8
    return b1, x0, y0
def fonk6(a5, b18):
    b11, b6, b11 = fonk5(a5, b18)
    return b6 % b18
def fonk7(a5, b17, c, b22):
    b14, b12 = 0.0, b17
    a3 = 1
    while b12 - b14 >= 1:
        b13 = (b14 + b12) / b4
        if b22(fonk1(b4, a3 * a5, b17) * c % b17) == 0:
            b12 = b13
        else:
            b14 = b13
        a3 += 1
    return int(b14)
def fonk8():
    a4 = 256
    b15 = fonk4(a4)
    b16 = fonk4(a4)
    b17 = b15 * b16
    a5 = 65537
    b18 = (b15 - 1) * (b16 - 1)
    b19 = fonk6(a5, b18)
    print(f"b15: {b15}")
    print(f"b16: {b16}")
    print(f"a5: {a5}")
    print(f"b19: {b19}")
    print(f"b17: {b17}")
    print()
    a6 = 123456789
    b20 = fonk1(a6, a5, b17)
    b21 = fonk1(b20, b19, b17)
    print(f"Plaintext: {a6}")
    print(f"Ciphertext: {b20}")
    print(f"Decrypted text: {b21}")
    print()
    print("Performing LSB Leak Attack...")
    b22 = lambda b6: fonk1(b6, b19, b17) % b4
    b23 = fonk7(a5, b17, b20, b22)
    print(f"Leaked a6: {b23}")
    print()
if b24 = = '__main__':
    fonk8()