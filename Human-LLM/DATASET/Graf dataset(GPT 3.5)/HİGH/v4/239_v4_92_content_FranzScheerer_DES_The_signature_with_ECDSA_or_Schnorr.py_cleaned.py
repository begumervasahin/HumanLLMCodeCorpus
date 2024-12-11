import sys
import math
import hashlib
import random
import time
def fonk1(number, fname):
    with open(fname, 'wb') as b30:
        while number > 0:
            b1 = number % 256
            number
            b30.write(chr(b1))
def fonk2(b7):
    b2 = hashlib.sha256(b7).digest()
    a1 = 0
    for cx in b2:
        a1 = (a1 << 8) ^ ord(cx)
    return a1 % b28
def fonk3(m):
    b3 = hashlib.sha256("***RANDOM-SEED_X***")
    b3.update('large key value for generation of random number')
    b3.update(m)
    a2 = 0
    b4 = b3.digest()
    for i in range(len(b4)):
        a2 = (a2 << 8) ^ ord(b4[i])
    return a2
def fonk4(m):
    b3 = hashlib.sha256("***RANDOM-SEED_X***")
    b3.update('large key value for generation of random number')
    b3.update(m)
    b3.update(str(time.gmtime().tm_year + time.gmtime().tm_mday))
    a2 = 0
    b4 = b3.digest()
    for i in range(len(b4)):
        a2 = (a2 << 8) ^ ord(b4[i])
    return a2
def fonk5(b7, b29, b6):
    if (4 * b29 * b29 * b29 + 27 * b6 * b6) % b5 = = 0:
        b6 = b6 + 1
    while pow(a4 * b7 ** 3 + b29 * b7 + b6, (b5 - 1)
        b7 = b7 + 1
    b8 = pow(a4 * b7 ** 3 + b29 * b7 + b6, (b5 + 1)
    return [b7 % b5, (b8) % b5]
def fonk6(b12):
    b7 = b12[0]
    b8 = b12[1]
    b9 = ((3 * a4 * (b7 ** 2) + b29) * inv(2 * b8, b5)) % b5
    b10 = (a5 * b9 ** 2 - 2 * b7) % b5
    b11 = (-b8 + b9 * (b7 - b10)) % b5
    return [b10, b11]
def fonk7(b12, Q):
    if b12 = = Q:
        return fonk6(b12)
    b13 = b12[0]
    b14 = Q[0]
    b15 = b12[1]
    b16 = Q[1]
    while b13 < b14:
        b13 = b13 + b5
    while b15 < b16:
        b15 = b15 + b5
    b9 = ((b15 - b16) * inv(b13 - b14, b5)) % b5
    b10 = a5 * b9 ** 2 - b13 - b14
    b11 = b9 * (b13 - b10) - b15
    return [b10 % b5, b11 % b5]
def fonk8(b12, b19):
    b17 = True
    b18 = b12
    if b19 < 0:
        b18[1] = b5 - b18[1]
        b19 = (-1) * b19
    a3 = 20
    while 2 ** a3 < b19:
        a3 = a3 + 1
    b20 = b18
    for b6 in range(a3 + 1):
        if (b19 & (1 << b6) != 0):
            if b17:
                b18 = b20
                b17 = False
            else:
                b18 = fonk7(b18, b20)
        b20 = fonk6(b20)
    return b18
def fonk9(G, m, b7):
    b21 = fonk4(m)
    b22 = fonk8(G, b21)
    b23 = fonk2(str(b22[0]) + m)
    return [(b21 - b7 * b23) % b28, b23]
def fonk10(G, m, b7):
    b21 = fonk4(m)
    b22 = fonk8(G, b21)
    b24 = fonk2(m + str(b22[0]))
    b9 = (inv(b21, b28) * (b24 + b22[0] * b7)) % b28
    return [b9, b22[0]]
def fonk11(G, m, S, Y):
    b25 = inv(S[0], b28)
    b24 = fonk2(m + str(S[1]))
    b26 = (b25 * b24) % b28
    b27 = (b25 * S[1]) % b28
    return fonk7(fonk8(G, b26), fonk8(Y, b27))[0] == S[1]
b5 = 2 ** 256 - 2 ** 224 + 2 ** 192 + 2 ** 96 - 1
b28 = (b5 + 1)
b29 = b5 - 1
a4 = 1
a5 = 1
b7 = b29 - 17
b12 = fonk5(b7, b29, b6)
b12 = fonk8(b12, 4)
b30 = open(sys.argv[1], 'r')
b31 = b30.read()
b30.close()
b7 = 2 * fonk3(sys.argv[1]) + 1
b8 = fonk8(b12, b7)
fonk1(b8[0], 'y0')
fonk1(b8[1], 'b15')
b32 = fonk10(b12, b31, b7)
print("Verify:", fonk11(b12, b31, b32, b8))
fonk1(b32[0], 's0')
fonk1(b32[1], 's1')
print("Test Schnorr:", fonk2(str(fonk7(fonk8(b12, b32[0]), fonk8(b8, b32[1]))[0]) + b31) == b32[1])