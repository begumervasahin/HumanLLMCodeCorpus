import random
import math
b1 = {chr(b7+97): b7 for b7 in range(26)}
b2 = {b7: chr(b7+97) for b7 in range(26)}
def fonk1(b3, b4, C):
    if b3 = = 0:
        return 0
    if b4 = = 0:
        return 1
    if b4 % b5 = = 0:
        b6 = fonk1(b3, b4
        b6 = (b6 * b6) % C
    else:
        b6 = b3 % C
        b6 = (b6 * fonk1(b3, b4 - 1, C) % C) % C
    return int((b6 + C) % C)
def fonk2(b17):
    for b7 in range(b5, int(b17 ** 0.5) + 1):
        if b17 % b7 = = 0:
            return False
    return True
def fonk3(a, b8):
    if b8 = = 0:
        return a
    else:
        return fonk3(b8, a % b8)
def fonk4(b17, b18):
    b9 = [b7 for b7 in range(1, b18) if (b17 % b7 != 0 and fonk3(b7, b18) == 1)]
    b10 = random.choice(b9)
    return (b17, b10)
def fonk5(b17, b18, b10):
    b11 = [b7 for b7 in range(1, b18) if (((b7 * b18) + 1) % b10 == 0)]
    b12 = random.choice(b11)
    print("b12 = ", b12)
    b13 = ((b12 * b18) + 1)
    return (b17, b13)
b14 = [b7 for b7 in range(10, 100) if fonk2(b7)]
b15 = random.choice(b14)
b14.remove(b15)
b16 = random.choice(b14)
print("b15 = ", b15)
print("b16 = ", b16)
b17 = b15 * b16
b18 = (b15 - 1) * (b16 - 1)
b19 = fonk4(b17, b18)
print("Public key (b17, b10):", b19)
b20 = fonk5(b17, b18, b19[1])
print("Private key (b17, b13):", b20)
b21 = input("Enter what has to be encrypted: ")
a1 = 1099
print("Original message:\t", a1)
b22 = fonk1(a1, b19[1], b17)
b23 = fonk1(b22, b20[1], b17)
print("Encrypted message:", b22)
print("Decrypted message:", b23)
a1 = 0
b7 = 0
for ch in b21[::-1]:
    a1 += b1[ch] * (26 ** b7)
    b7 += 1
print("Encoded message:", a1)
b22 = fonk1(a1, b19[1], b17)
b23 = fonk1(b22, b20[1], b17)
b24 = ""
while b23 > 0:
    b25 = b23 % 26
    b24 += b2[b25]
    b23
print("The decrypted message is:", b24[::-1])