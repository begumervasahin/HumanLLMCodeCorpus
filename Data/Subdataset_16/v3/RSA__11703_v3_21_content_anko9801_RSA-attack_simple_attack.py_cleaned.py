import random
def fonk1(b1, exponent, modulus):
    a1 = 1
    while exponent > 0:
        if exponent & 1:
            a1 = (a1 * b1) % modulus
        b1 = (b1 * b1) % modulus
        exponent >>= 1
    return a1
def fonk2(bit_length):
    a2 = 1
    for b13 in range(bit_length - b5):
        a2 = a2 * b5 + random.randint(0, 1)
    return a2 * b5 + 1
def fonk3(b3, b2 = 100):
    if b3 = = b5:
        return True
    if b3 = = 1 or b3 % b5 == 0:
        return False
    b15, b4 = b3 - 1, 0
    while b15 % b5 = = 0:
        b15
        b4 += 1
    for b13 in range(b2):
        b6 = random.randint(b5, b3 - b5)
        b7 = fonk1(b6, b15, b3)
        if b7 = = 1 or b7 == b3 - 1:
            continue
        for b13 in range(b4 - 1):
            b7 = fonk1(b7, b5, b3)
            if b7 = = b3 - 1:
                break
        else:
            return False
    return True
def fonk4(bit_length):
    while True:
        b8 = fonk2(bit_length)
        if fonk3(b8):
            return b8
def fonk5(b7, b9):
    while b9:
        b7, b9 = b9, b7 % b9
    return b7
def fonk6(b7, b9):
    old_r, b10 = b7, b9
    old_s, b4 = 1, 0
    old_t, b11 = 0, 1
    while b10 != 0:
        b12 = old_r
        old_r, b10 = b10, old_r - b12 * b10
        old_s, b4 = b4, old_s - b12 * b4
        old_t, b11 = b11, old_t - b12 * b11
    return old_r, old_s, old_t
def fonk7(a3, b18):
    gcd, b7, b13 = fonk6(a3, b18)
    return b7 % b18
def fonk8(b3, b14 = b5, y_start=b5):
    b7, b9, b15 = b14, y_start, 1
    while b15 = = 1:
        b7 = (b7 * b7 + 1) % b3
        b9 = (b9 * b9 + 1) % b3
        b9 = (b9 * b9 + 1) % b3
        b15 = fonk5(abs(b7 - b9), b3)
    return b15
def fonk9(b3, a3, b20):
    b16 = fonk8(b3)
    b17 = b3
    b18 = (b16 - 1) * (b17 - 1)
    b15 = fonk7(a3, b18)
    return b16, b17, b15
if b19 = = '__main__':
    a3 = 65537
    a4 = 123456789
    b16 = fonk4(10)
    b17 = fonk4(10)
    b3 = b16 * b17
    b18 = (b16 - 1) * (b17 - 1)
    b15 = fonk7(a3, b18)
    b20 = fonk1(a4, a3, b3)
    print("Simple attack")
    print("Public key (a3, b3):", a3, b3)
    b16, b17, b15 = fonk9(b3, a3, b20)
    print("Attack complete!")
    print("Primes (b16, b17):", b16, b17)
    print("Private key (b15):", b15)