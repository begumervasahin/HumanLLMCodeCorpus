import random
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
def fonk6(a5, outlen):
    global b1, b3, b4, b5, b2
    if b1 != 0:
        fonk3()
    for _ in range(outlen):
        a5.append(fonk2())
def fonk7(b12, b6):
    while b6 > 0:
        b12, b6 = b6, b12 % b6
    return b12
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
        elif ord(c) <= ord('f') and ord(c) >= ord('b12'):
            a2 = (a2 << 4) + ord(c) - 87
        elif ord(c) <= ord('F') and ord(c) >= ord('a6'):
            a2 = (a2 << 4) + ord(c) - 55
    return a2
def fonk12(b6, b12):
    b9 = b12
    a3 = 0
    a4 = 1
    while b6 != 1:
        b10 = b12
        b11 = b6
        b6 = b12 % b6
        b12 = b11
        b13 = a4
        a4 = a3 - b10 * a4
        a3 = b13
    if a4 < 0:
        a4 += b9
    return a4
def fonk13(a7):
    global b1, b3, b4, b5, b2
    b3 = b4 = b1 = 0
    b5 = 1
    b2 = list(range(256))
    for c in a7:
        fonk5(ord(c))
    a2 = []
    fonk6(a2, 32)
    a5 = 0
    for bx in a2:
        a5 = (a5 << 8) + bx
    return a5 % b31
def fonk14(b33, Q):
    b16, b14 = b33[0], Q[0]
    y1, b15 = b33[1], Q[1]
    if b16 = = b14:
        a3 = ((3 * (b16**2) + a6) * fonk12(2 * y1, b27)) % b27
    else:
        if b16 < b14:
            b16 += b27
        a3 = ((y1 - b15) * fonk12(b16 - b14, b27)) % b27
    b17 = a3**2 - b16 - b14
    b18 = a3 * (b16 - b17) - y1
    return [b17 % b27, b18 % b27]
def fonk15(b33, a1):
    b19 = True
    b20 = b33
    if a1 < 0:
        b20[1] = b27 - b20[1]
        a1 = (-1) * a1
    b21 = b20
    while a1 > 0:
        if (a1 % 2 != 0):
            if b19:
                b20 = b21
                b19 = False
            else:
                b20 = fonk14(b20, b21)
        b21 = fonk14(b21, b21)
        a1 = a1
    return b20
def fonk16(G, a3, b35, b22, b9):
    return b22 = = fonk13(str(fonk14(fonk15(G, a3), fonk15(b35, b22))[0]) + b9)
def fonk17(G, b9, S, b35):
    b23 = fonk12(S[0], b30)
    b24 = fonk13(b9 + str(S[1]))
    b25 = (b23 * b24) % b30
    b26 = (b23 * S[1]) % b30
    return fonk14(fonk15(G, b25), fonk15(b35, b26))[0] == S[1]
b27 = fonk8(12 * 2**141)
print("a6 prime greater than 12 times 2^141 \b28 = ", b27)
a6 = 0
b29 = b27 - 3
b30 = (b27 + 1)
b31 = b30
a7 = 1
while pow(a7**3 + a6*a7 + b29, (b27 - 1)
    a7 += 1
b32 = pow(a7**3 + a6*a7 + b29, (b27 + 1)
b33 = [a7 % b27, b32 % b27]
b33 = fonk15(b33, 12)
b34 = sys.argv[1]
b35 = [7743078162825626208847856060554090836324463, 7535129688736902967896532855534019525412438]
b36 = [fonk10('s0'), fonk10('s1')]
print("Public key: X: ", b35[0] % b27)
print("Public key: b35: ", b35[1] % b27)
print("Signature X: ", b36[0])
print("Signature b35: ", b36[1])
print("")
print("The verification of signature: ", fonk16(b33, b36[0], b35, b36[1], b34))