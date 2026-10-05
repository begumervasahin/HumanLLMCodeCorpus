import random
import math
b1 = b3 = b4 = b5 = 0
b2 = []
def fonk1():
    global b1, b3, b4, b5, b2
    b3 = (b3 + b5) % 256
    b4 = b2[(b4 + b2[b3]) % 256]
    b2[b3], b2[b4] = b2[b4], b2[b3]
def fonk2():
    global b1, b3, b4, b5, b2
    fonk1()
    return b2[b4]
def fonk3():
    global b1, b3, b4, b5, b2
    for _ in range(256):
        fonk1()
    b5 = (b5 + 2) % 256
    b1 = 0
def fonk4(a7):
    global b1, b2
    if b1 = = 240:
        fonk3()
    b2[b1], b2[240 + a7] = b2[240 + a7], b2[b1]
    b1 += 1
def fonk5(b6):
    fonk4(b6 % 16)
    fonk4(b6
def fonk6(a6, outlen):
    global b1
    if b1 != 0:
        fonk3()
    for _ in range(outlen):
        a6.append(fonk2())
def fonk7(a3, b6):
    while b6 > 0:
        a3, b6 = b6, a3 % b6
    return a3
def fonk8(p):
    while p % 12 != 11:
        p += 1
    return fonk9(p)
def fonk9(p):
    b7 = 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 * 41 * 43 * 47
    while True:
        while fonk7(p, b7) != 1 or fonk7((p + 1)
            p += 12
        if pow(7, p - 1, p) != 1 or pow(7, (p + 1)
            p += 12
            continue
        return p
def fonk10(filename):
    with open(filename, 'rb') as f:
        a1 = 0
        b8 = f.read()
        for i in range(len(b8)):
            a1 = (a1 << 8) ^ ord(b8[len(b8) - i - 1])
    return a1
def fonk11(a7):
    a2 = 0
    for c in a7:
        if '0' <= c <= '9':
            a2 = (a2 << 4) + ord(c) - ord('0')
        elif 'a3' <= c <= 'f':
            a2 = (a2 << 4) + ord(c) - ord('a3') + 10
        elif 'A' <= c <= 'F':
            a2 = (a2 << 4) + ord(c) - ord('A') + 10
    return a2
b9 = fonk8(12 * 2**141)
print(f"A b9 greater than 12 times 2^141 \b10 = {b9}")
a3 = 0
b6 = b9 - 3
b11 = (b9 + 1)
b12 = b11
def fonk12(b6, a3):
    b13 = a3
    a4 = 0
    a5 = 1
    while b6 != 1:
        b14 = a3
        b15 = b6
        b6 = a3 % b6
        a3 = b15
        b16 = a5
        a5 = a4 - b14 * a5
        a4 = b16
    if a5 < 0:
        a5 += b13
    return a5
def fonk13(a7):
    global b1, b5, b2
    b3 = b4 = b1 = 0
    b5 = 1
    b2 = list(range(256))
    for c in a7:
        fonk5(ord(c))
    a2 = []
    fonk6(a2, 32)
    a6 = 0
    for bx in a2:
        a6 = (a6 << 8) + bx
    return a6 % b12
def fonk14(b30, Q):
    b18, x2, y1, b17 = b30[0], Q[0], b30[1], Q[1]
    if b18 = = x2:
        a4 = ((3 * (b18**2) + a3) * fonk12(2 * y1, b9)) % b9
    else:
        if b18 < x2:
            b18 += b9
        a4 = ((y1 - b17) * fonk12(b18 - x2, b9)) % b9
    b19 = a4**2 - b18 - x2
    b20 = a4 * (b18 - b19) - y1
    return [b19 % b9, b20 % b9]
def fonk15(b30, a1):
    b23, b21 = b30, True
    if a1 < 0:
        b23[1] = b9 - b23[1]
        a1 = -a1
    b22 = b23
    while a1 > 0:
        if a1 % 2 != 0:
            b23 = b22 if b21 else fonk14(b23, b22)
            b21 = False
        b22 = fonk14(b22, b22)
        a1
    return b23
def fonk16(G, a4, b32, b24, b13):
    return b24 = = fonk13(str(fonk14(fonk15(G, a4), fonk15(b32, b24))[0]) + b13)
def fonk17(G, b13, S, b32):
    b25 = fonk12(S[0], b11)
    b26 = fonk13(b13 + str(S[1]))
    b27 = (b25 * b26) % b11
    b28 = (b25 * S[1]) % b11
    return fonk14(fonk15(G, b27), fonk15(b32, b28))[0] == S[1]
a7 = 1
while pow(a7**3 + a3 * a7 + b6, (b9 - 1) / 2, b9) != 1:
    a7 += 1
b29 = pow(a7**3 + a3 * a7 + b6, (b9 + 1) / 4, b9)
b30 = [a7 % b9, b29 % b9]
b30 = fonk15(b30, 12)
b31 = sys.argv[1]
b32 = [7743078162825626208847856060554090836324463, 7535129688736902967896532855534019525412438]
b33 = [fonk10('s0'), fonk10('s1')]
print("Public key: X:", b29[0] % b9)
print("Public key: b32:", b29[1] % b9)
print("Signature X:", b33[0])
print("Signature b32:", b33[1])
print("")
print("The verification of signature:", fonk16(b30, b33[0], b32, b33[1], b31))