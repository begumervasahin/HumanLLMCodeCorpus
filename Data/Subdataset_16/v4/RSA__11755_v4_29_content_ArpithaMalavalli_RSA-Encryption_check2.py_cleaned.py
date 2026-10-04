import random
def fonk1(b1, b2, C):
    if b1 = = 0:
        return 0
    if b2 = = 0:
        return 1
    if b2 % b3 = = 0:
        b4 = fonk1(b1, b2
        b4 = (b4 * b4) % C
    else:
        b4 = b1 % C
        b4 = (b4 * fonk1(b1, b2 - 1, C) % C) % C
    return (int)((b4 + C) % C)
def fonk2(b15):
    if b15 <= 1:
        return False
    for b5 in range(b3, int(b15 ** 0.5) + 1):
        if b15 % b5 = = 0:
            return False
    return True
def fonk3(a, b6):
    if b6 = = 0:
        return a
    else:
        return fonk3(b6, a % b6)
def fonk4(b15, b16):
    b7 = [b5 for b5 in range(1, b16) if (b15 % b5 != 0 and fonk3(b5, b16) == 1)]
    b8 = random.choice(b7)
    return (b15, b8)
def fonk5(b15, b16, b8):
    b9 = [b5 for b5 in range(1, b16) if (((b5 * b16) + 1) % b8 == 0)]
    b10 = random.choice(b9)
    b11 = ((b10 * b16) + 1)
    return (b15, b11)
b12 = [b5 for b5 in range(10, 100) if fonk2(b5)]
b13 = random.choice(b12)
b12.remove(b13)
b14 = random.choice(b12)
b15 = b13 * b14
b16 = (b13 - 1) * (b14 - 1)
b17 = fonk4(b15, b16)
b18 = fonk5(b15, b16, b17[1])
print("Public key (b15, b8):", b17)
print("Private key (b15, b11):", b18)
a1 = 1099
print("Original message:", a1)
b19 = fonk1(a1, b17[1], b15)
b20 = fonk1(b19, b18[1], b15)
print("Encrypted message:", b19)
print("Decrypted message:", b20)