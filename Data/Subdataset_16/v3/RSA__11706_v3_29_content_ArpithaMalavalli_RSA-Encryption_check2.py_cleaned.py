import random
b1 = {chr(b7 + 97): b7 for b7 in range(26)}
b2 = {b7: chr(b7 + 97) for b7 in range(26)}
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
    return (b6 + C) % C
def fonk2(b15):
    if b15 <= 1:
        return False
    for b7 in range(b5, int(b15 ** 0.5) + 1):
        if b15 % b7 = = 0:
            return False
    return True
def fonk3(a, b8):
    while b8 != 0:
        a, b8 = b8, a % b8
    return a
def fonk4(b15, b16):
    b9 = [b7 for b7 in range(b5, b16) if fonk3(b7, b16) == 1]
    b10 = random.choice(b9)
    return (b15, b10)
def fonk5(b15, b16, b10):
    a1 = 1
    while (a1 * b16 + 1) % b10 != 0:
        a1 += 1
    b11 = (a1 * b16 + 1)
    return (b15, b11)
def fonk6(start, end):
    return [b7 for b7 in range(start, end) if fonk2(b7)]
def fonk7():
    b12 = fonk6(10, 100)
    b13 = random.choice(b12)
    b12.remove(b13)
    b14 = random.choice(b12)
    print("b13 = ", b13)
    print("b14 = ", b14)
    b15 = b13 * b14
    b16 = (b13 - 1) * (b14 - 1)
    b17 = fonk4(b15, b16)
    print("Public key (b15, b10):", b17)
    b18 = fonk5(b15, b16, b17[1])
    print("Private key (b15, b11):", b18)
    b19 = input("Enter what has to be encrypted: ")
    a2 = 1099
    print("Original message:", a2)
    b20 = fonk1(a2, b17[1], b15)
    b21 = fonk1(b20, b18[1], b15)
    print("Encrypted message:", b20)
    print("Decrypted message:", b21)
    a3 = 0
    for b7, ch in enumerate(b19[::-1]):
        a3 += b1[ch] * (26 ** b7)
    print("Encoded message:", a3)
    b20 = fonk1(a3, b17[1], b15)
    b21 = fonk1(b20, b18[1], b15)
    b22 = ""
    while b21 > 0:
        b23 = b21 % 26
        b22 += b2[b23]
        b21
    print("The decrypted message is:", b22[::-1])
if b24 = = "__main__":
    fonk7()