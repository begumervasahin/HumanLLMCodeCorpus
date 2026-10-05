import sys
import math
import hashlib
import random
import time
def fonk1(number, fname):
    with open(fname, 'wb') as b27:
        b1 = number
        while b1 > 0:
            b2 = b1 % 256
            b1
            b27.write(chr(b2))
def fonk2(b29):
    a1 = 0
    for a4 in b29:
        a1 = (a1 << 8) ^ ord(a4)
    return a1
def fonk3(b4, b3):
    while b3 > 0:
        b4, b3 = b3, b4 % b3
    return b4
def fonk4(b3, m):
    b9, b8, b4 = 0, 1, m
    while b3 != 1:
        b5 = b4
        b6 = b3
        b3 = b4 % b3
        b4 = b6
        b7 = b8
        b8 = b9 - b5 * b8
        b9 = b7
    if b8 < 0:
        b8 += m
    return b8
def fonk5(b29):
    b10 = hashlib.sha256(b29.encode()).digest()
    a1 = 0
    for cx in b10:
        a1 = (a1 << 8) ^ cx
    return a1
def fonk6(m):
    b11 = hashlib.sha256("***RANDOM-SEED_X***".encode())
    b11.update('large key value for generation of random number'.encode())
    b11.update(m.encode())
    a2 = 0
    b12 = b11.digest()
    for i in range(len(b12)):
        a2 = (a2 << 8) ^ ord(b12[i])
    return a2
def fonk7(m):
    b11 = hashlib.sha256("***RANDOM-SEED_X***".encode())
    b11.update('large key value for generation of random number'.encode())
    b11.update(m.encode())
    b11.update(str(time.gmtime().tm_year + time.gmtime().tm_mday).encode())
    a2 = 0
    b12 = b11.digest()
    for i in range(len(b12)):
        a2 = (a2 << 8) ^ ord(b12[i])
    return a2
def fonk8(b29, b4, b3):
    if (4 * b4 * b4 * b4 + 27 * b3 * b3) % b13 = = 0:
        b3 += 1
    while pow(a4 * b29 ** 3 + b4 * b29 + b3, (b13 - 1)
        b29 += 1
    b14 = pow(a4 * b29 ** 3 + b4 * b29 + b3, (b13 + 1)
    return [b29 % b13, (b14) % b13]
def fonk9(b26, b1):
    b15 = True
    b16 = b26
    if b1 < 0:
        b16[1] = b13 - b16[1]
        b1 = (-1) * b1
    a3 = 20
    while 2 ** a3 < b1:
        a3 += 1
    b17 = b16
    for b3 in range(a3 + 1):
        if (b1 & (1 << b3) != 0):
            if b15:
                b16 = b17
                b15 = False
            else:
                b16 = addP(b16, b17)
        b17 = dpoint(b17)
    return b16
def fonk10(G, m, b29):
    b18 = fonk7(m)
    b19 = fonk9(G, b18)
    b20 = fonk5(str(b19[0]) + m)
    return [(b18 - b29 * b20) % b25, b20]
def fonk11(G, m, b29):
    b18 = fonk7(m)
    b19 = fonk9(G, b18)
    b21 = fonk5(m + str(b19[0]))
    b9 = (fonk4(b18, b25) * (b21 + b19[0] * b29)) % b25
    return [b9, b19[0]]
def fonk12(G, m, S, Y):
    b22 = fonk4(S[0], b25)
    b21 = fonk5(m + str(S[1]))
    b23 = (b22 * b21) % b25
    b24 = (b22 * S[1]) % b25
    return addP(fonk9(G, b23), fonk9(Y, b24))[0] == S[1]
b4 = b13 - 1
a4 = 1
b13 = 2 ** 256 - 2 ** 224 + 2 ** 192 + 2 ** 96 - 1
b25 = (b13 + 1)
b26 = fonk8(b4 - 17, b4, 0)
b27 = open(sys.argv[1], 'r')
b28 = b27.read()
b27.close()
b29 = 2 * fonk6(sys.argv[1]) + 1
b14 = fonk9(b26, b29)
fonk1(b14[0], 'y0')
fonk1(b14[1], 'y1')
b30 = fonk11(b26, b28, b29)
print("Verify:", fonk12(b26, b28, b30, b14))
fonk1(b30[0], 's0')
fonk1(b30[1], 's1')
print("Test Schnoor:", fonk5(str(addP(fonk9(b26, b30[0]), fonk9(b14, b30[1]))[0]) + b28) == b30[1])