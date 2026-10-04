import random
def fonk1(b2, exponent, modulus):
    a1 = b1
    while exponent > 0:
        if exponent & b1 = = b1:
            a1 = (a1 * b2) % modulus
        b2 = (b2 * b2) % modulus
        exponent >>= b1
    return a1
def fonk2(bit_length):
    b3 = [random.randint(0, b1) for b14 in range(bit_length - b6)]
    a2 = b1
    for bit in b3:
        a2 = a2 * b6 + bit
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
    b8 = [random.randint(b1, b5 - b1) for b14 in range(b4)]
    for a in b8:
        if fonk1(a, b7, b5) != b1:
            if all(fonk1(a, (b6 ** b11) * b7, b5) != b5 - b1 for b11 in range(a3)):
                return False
    return True
def fonk4(bit_length):
    while True:
        b9 = fonk2(bit_length)
        if fonk3(b9):
            return b9
def fonk5(b16, b10):
    while b10:
        b16, b10 = b10, b16 % b10
    return b16
def fonk6(b16, b10):
    old_r, b11 = b16, b10
    old_s, a3 = b1, 0
    old_t, b12 = 0, b1
    while b11 != 0:
        b13 = old_r
        old_r, b11 = b11, old_r - b13 * b11
        old_s, a3 = a3, old_s - b13 * a3
        old_t, b12 = b12, old_t - b13 * b12
    return old_r, old_s, old_t
def fonk7(a4, b19):
    gcd, b16, b14 = fonk6(a4, b19)
    return b16 % b19
def fonk8(b5, b15 = b6, y_start=b6):
    b16, b10, b7 = b15, y_start, b1
    while b7 = = b1:
        b16 = (b16 * b16 + b1) % b5
        b10 = (b10 * b10 + b1) % b5
        b10 = (b10 * b10 + b1) % b5
        b7 = fonk5(abs(b16 - b10), b5)
    return b7
def fonk9(b5, a4, b21):
    b17 = fonk8(b5)
    b18 = b5
    b19 = (b17 - b1) * (b18 - b1)
    b7 = fonk7(a4, b19)
    return b17, b18, b7
if b20 = = '__main__':
    a4 = 65537
    a5 = 123456789
    b17 = fonk4(10)
    b18 = fonk4(10)
    b5 = b17 * b18
    b19 = (b17 - b1) * (b18 - b1)
    b7 = fonk7(a4, b19)
    b21 = fonk1(a5, a4, b5)
    print("Simple attack")
    print("Public key (a4, b5):", a4, b5)
    b17, b18, b7 = fonk9(b5, a4, b21)
    print("Attack complete!")
    print("Primes (b17, b18):", b17, b18)
    print("Private key (b7):", b7)