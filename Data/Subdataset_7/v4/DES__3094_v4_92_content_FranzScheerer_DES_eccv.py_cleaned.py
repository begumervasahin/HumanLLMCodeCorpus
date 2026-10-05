import random
import math
import hashlib
import sys
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
    global b1, b3, b4, b5, b2
    if b1 = = 240:
        fonk3()
    b2[b1], b2[240 + a7] = b2[240 + a7], b2[b1]
    b1 += 1
def fonk5(b6):
    fonk4(b6 % 16)
    fonk4(b6
def fonk6(a6, outlen):
    global b1, b3, b4, b5, b2
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
        if (pow(7, p - 1, p) != 1 or pow(7, (p + 1)
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
        if ord(c) < 58 and ord(c) >= 48:
            a2 = (a2 << 4) + ord(c) - 48
        elif ord(c) <= ord('f') and ord(c) >= ord('a3'):
            a2 = (a2 << 4) + ord(c) - 87
        elif ord(c) <= ord('F') and ord(c) >= ord('A'):
            a2 = (a2 << 4) + ord(c) - 55
    return a2
b9 = fonk8(12 * 2**141)
print("A b9 greater than 12 times 2^141 \b10 = ", b9)
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
    global b1, b3, b4, b5, b2
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
def fonk14(b32, Q):
    b17 = b32[0]
    b18 = Q[0]
    b19 = b32[1]
    b20 = Q[1]
    if b17 = = b18:
        a4 = ((3 * (b17**2) + a3) * fonk12(2 * b19, b9)) % b9
    else:
        if b17 < b18:
            b17 += b9
        a4 = ((b19 - b20) * fonk12(b17 - b18, b9)) % b9
    b21 = a4**2 - b17 - b18
    b22 = a4 * (b17 - b21) - b19
    return [b21 % b9, b22 % b9]
def fonk15(b32, a1):
    b23 = True
    b24 = b32
    if a1 < 0:
        b24[1] = b9 - b24[1]
        a1 = (-1) * a1
    b25 = b24
    while a1 > 0:
        if (a1 % 2 != 0):
            if b23:
                b24 = b25
                b23 = False
            else:
                b24 = fonk14(b24, b25)
        b25 = fonk14(b25, b25)
        a1 = a1
    return b24
def fonk16(G, a4, b34, b26, b13):
    return b26 = = fonk13(str(fonk14(fonk15(G, a4), fonk15(b34, b26))[0]) + b13)
def fonk17(G, b13, S, b34):
    b27 = fonk12(S[0], b11)
    b28 = fonk13(b13 + str(S[1]))
    b29 = (b27 * b28) % b11
    b30 = (b27 * S[1]) % b11
    return fonk14(fonk15(G, b29), fonk15(b34, b30))[0] == S[1]
a7 = 1
while pow(a7**3 + a3*a7 + b6, (b9 - 1) / 2, b9) != 1:
    a7 += 1
b31 = pow(a7**3 + a3*a7 + b6, (b9 + 1) / 4, b9)
b32 = [a7 % b9, b31 % b9]
b32 = fonk15(b32, 12)
b33 = sys.argv[1]
b34 = [7743078162825626208847856060554090836324463, 7535129688736902967896532855534019525412438]
b35 = [fonk10('s0'), fonk10('s1')]
print("Public key: X: ", b31[0] % b9)
print("Public key: b34: ", b31[1] % b9)
print("Signature X: ", b35[0])
print("Signature b34: ", b35[1])
print("")
print("The verification of signature: ", fonk16(b32, b35[0], b34, b35[1], b33))