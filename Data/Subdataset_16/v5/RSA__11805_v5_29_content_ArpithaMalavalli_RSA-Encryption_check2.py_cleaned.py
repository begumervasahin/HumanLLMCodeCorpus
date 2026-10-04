import random
def fonk1(b1, b2, mod):
    if b1 = = 0:
        return 0
    if b2 = = 0:
        return 1
    if b2 % b3 = = 0:
        b4 = fonk1(b1, b2
        return (b4 * b4) % mod
    else:
        return (b1 * fonk1(b1, b2 - 1, mod)) % mod
def fonk2(b13):
    if b13 <= 1:
        return False
    for b5 in range(b3, int(b13 ** 0.5) + 1):
        if b13 % b5 = = 0:
            return False
    return True
def fonk3(a, b6):
    while b6:
        a, b6 = b6, a % b6
    return a
def fonk4(b13, b14):
    b7 = [b8 for b8 in range(b3, b14) if fonk3(b8, b14) == 1]
    b8 = random.choice(b7)
    return b13, b8
def fonk5(b13, b14, b8):
    a1 = 1
    while (a1 * b14 + 1) % b8 != 0:
        a1 += 1
    b9 = (a1 * b14 + 1)
    return b13, b9
b10 = [b5 for b5 in range(10, 100) if fonk2(b5)]
b11 = random.choice(b10)
b10.remove(b11)
b12 = random.choice(b10)
b13 = b11 * b12
b14 = (b11 - 1) * (b12 - 1)
b15 = fonk4(b13, b14)
b16 = fonk5(b13, b14, b15[1])
print("Public key (b13, b8):", b15)
print("Private key (b13, b9):", b16)
a2 = 1099
print("Original message:", a2)
b17 = fonk1(a2, b15[1], b13)
b18 = fonk1(b17, b16[1], b13)
print("Encrypted message:", b17)
print("Decrypted message:", b18)