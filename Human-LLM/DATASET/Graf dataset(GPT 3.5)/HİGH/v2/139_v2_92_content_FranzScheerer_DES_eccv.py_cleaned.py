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
    for v in range(256):
        fonk1()
    b5 = (b5 + 2) % 256
    b1 = 0
def fonk4(a6):
    global b1, b3, b4, b5, b2
    if b1 = = 240:
        fonk3()
    b2[b1], b2[240 + a6] = b2[240 + a6], b2[b1]
    b1 = b1 + 1
def fonk5(b6):
    fonk4(b6 % 16)
    fonk4(b6
def fonk6(a5, outlen):
    global b1, b3, b4, b5, b2
    if b1 != 0:
        fonk3()
    for v in range(outlen):
        a5.append(fonk2())
def fonk7(b14, b6):
    while b6 > 0:
        b14, b6 = b6, b14 % b6
    return b14
def fonk8(b7):
    while b7 % 12 != 11:
        b7 = b7 + 1
    return fonk9(b7)
def fonk9(b7):
    b8 = 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 * 41 * 43 * 47
    while True:
        while fonk7(b7, b8) != 1 or fonk7((b7+1)
            b7 = b7 + 12
        if (pow(7, b7-1, b7) != 1 or pow(7, (b7+1)
            b7 = b7 + 12
            continue
        return b7
def fonk10(fnam):
    b9 = open(fnam, 'rb')
    a1 = 0
    b10 = b9.read()
    for i in range(len(b10)):
        a1 = (a1 << 8) ^ ord(b10[len(b10)-i-1])
    b9.close()
    return a1
def fonk11(a6):
    a2 = 0
    for c in a6:
        if ord(c) < 58 and ord(c) >= 48:
            a2 = (a2 << 4) + ord(c) - 48
        elif ord(c) <= ord('b9') and ord(c) >= ord('b14'):
            a2 = (a2 << 4) + ord(c) - 87
        elif ord(c) <= ord('F') and ord(c) >= ord('A'):
            a2 = (a2 << 4) + ord(c) - 55
    return a2
def fonk12(b6, b14):
    b11 = b14
    a3 = 0
    a4 = 1
    while b6 != 1:
        b12 = b14
        b13 = b6
        b6 = b14 % b6
        b14 = b13
        b15 = a4
        a4 = a3 - b12 * a4
        a3 = b15
    if a4 < 0:
        a4 = a4 + b11
    return a4
def fonk13(a6):
    global b1, b3, b4, b5, b2
    b3 = b4 = b1 = 0
    b5 = 1
    b2 = list(range(256))
    for c in a6:
        fonk5(ord(c))
    a2 = []
    fonk6(a2, 32)
    a5 = 0
    for bx in a2:
        a5 = (a5 << 8) + bx
    return a5 % b33
def fonk14(b35, Q):
    b16 = b35[0]
    b17 = Q[0]
    b18 = b35[1]
    b19 = Q[1]
    if b16 = = b17:
        a3 = ((3 * (b16**2) + b14) * fonk12(2 * b18, b30)) % b30
    else:
        if b16 < b17:
            b16 = b16 + b30
        a3 = ((b18 - b19) * fonk12(b16 - b17, b30)) % b30
    b20 = a3**2 - b16 - b17
    b21 = a3 * (b16 - b20) - b18
    return [b20 % b30, b21 % b30]
def fonk15(b35, a1):
    b22 = True
    b23 = b35
    if a1 < 0:
        b23[1] = b30 - b23[1]
        a1 = (-1) * a1
    b24 = b23
    while a1 > 0:
        if (a1 % 2 != 0):
            if b22:
                b23 = b24
                b22 = False
            else:
                b23 = fonk14(b23, b24)
        b24 = fonk14(b24, b24)
        a1 = a1
    return b23
def fonk16(G, a3, Y, b25, b11):
    return b25 = = fonk13(str(fonk14(fonk15(G, a3), fonk15(Y, b25))[0]) + b11)
def fonk17(G, b11, S, Y):
    b26 = fonk12(S[0], b32)
    b27 = fonk13(b11 + str(S[1]))
    b28 = (b26 * b27) % b32
    b29 = (b26 * S[1]) % b32
    return fonk14(fonk15(G, b28), fonk15(Y, b29))[0] == S[1]
b30 = fonk8(12 * 2**141)
print("A b30 greater than 12 times 2^141 \b31 = ", b30)
b14 = 0
b6 = b30 - 3
b32 = (b30 + 1)
b33 = b32
a6 = 1
while pow(a6**3 + b14*a6 + b6, (b30 - 1)
    a6 = a6 + 1
b34 = pow(a6**3 + b14*a6 + b6, (b30 + 1)
b35 = [a6 % b30, b34 % b30]
b35 = fonk15(b35, 12)
b36 = sys.argv[1]
b34 = [7743078162825626208847856060554090836324463, 7535129688736902967896532855534019525412438]
b37 = [fonk10('s0'), fonk10('s1')]
print("Public key: X: ", b34[0] % b30)
print("Public key: Y: ", b34[1] % b30)
print("Signature X: ", b37[0])
print("Signature Y: ", b37[1])
print("")
print("The verification of signature: ", fonk16(b35, b37[0], b34, b37[1], b36))