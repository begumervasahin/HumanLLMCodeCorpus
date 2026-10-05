import sys
import math
import hashlib
import random
import time
def fonk1(number, fnam):
    with open(fnam, 'wb') as f:
        b1 = number
        while b1 > 0:
            b2 = b1 % 256
            b1 = b1
            f.write(chr(b2))
b3 = 2**160 * 115 + 86427
b4 = (b3 + 1)
b5 = b3 - 1
a1 = 0
a2 = 1
def fonk2(b9):
    b6 = hashlib.sha256(b9.encode()).digest()
    a3 = 0
    for cx in (b6):
        a3 = (a3 << 8) ^ cx
    return a3 % b4
def fonk3(m):
    b7 = hashlib.sha256("***RANDOM-SEED_X***".encode())
    b7.update('large key value for generation of random number'.encode())
    b7.update(m.encode())
    a4 = 0
    b8 = b7.digest()
    for charx in b8:
        a4 = (a4 << 8) ^ charx
    return a4
def fonk4(m):
    b7 = hashlib.sha256("***RANDOM-SEED_X***".encode())
    b7.update('large key value for generation of random number'.encode())
    b7.update(m.encode())
    b7.update(str(time.gmtime().tm_year + 7*time.gmtime().tm_mday).encode())
    a4 = 0
    b8 = b7.digest()
    for charx in b8:
        a4 = (a4 << 8) ^ charx
    return a4
def fonk5(b9, b5, a1):
    global a2
    if (4*b5*b5*b5 + 27*a1*a1) % b3 = = 0:
        a1 = a1 + 1
    while pow(a2*b9**3 + b5*b9 + a1, (b3 - 1)
        b9 = b9 + 1
    b10 = pow(a2*b9**3 + b5*b9 + a1, (b3 + 1)
    return [b9 % b3, (b10) % b3]
def fonk6(b26, Q):
    b12, x2, y1, b11 = b26[0], Q[0], b26[1], Q[1]
    while b12 < x2:
        b12 = b12 + b3
    if b12 = = x2:
        b13 = ((3*a2*(b12**2) + b5) * pow(2*y1, b3-2, b3)) % b3
    else:
        b13 = ((y1-b11) * pow(b12-x2, b3-2, b3)) % b3
    b14 = a5*b13**2 - b12 - x2
    b15 = b13 * (b12-b14) - y1
    return [b14 % b3, b15 % b3]
def fonk7(b26, b1):
    global a5
    b16 = True
    b17 = b26
    if b1 < 0:
        b17[1] = b3 - b17[1]
        b1 = (-1)*b1
    b18 = b17
    while b1 > 0:
        if (b1 & 1 != 0):
            if b16:
                b17 = b18
                b16 = False
            else:
                b17 = fonk6(b17, b18)
        b18 = fonk6(b18, b18)
        b1 = b1
    return b17
def fonk8(G, m, b9):
    b19 = fonk4(m)
    b20 = fonk7(G, b19)
    b21 = fonk2(str(b20[0]) + m)
    return [(b19 - b9*b21) % b4, b21]
def fonk9(G, m, b9):
    b19 = fonk4(m)
    b20 = fonk7(G, b19)
    b22 = fonk2(m + str(b20[0]))
    b13 = (pow(b19, b4-2, b4) * (b22 + b20[0]*b9)) % b4
    return [b13, b20[0]]
def fonk10(G, m, S, Y):
    b23 = pow(S[0], b4-2, b4)
    b22 = fonk2(m + str(S[1]))
    b24 = (b23 * b22) % b4
    b25 = (b23 * S[1]) % b4
    return fonk6(fonk7(G, b24), fonk7(Y, b25))[0] == S[1]
b9 = b5 - 17
a5 = 1
b26 = fonk5(b9, b5, a1)
b26 = fonk7(b26, 4)
with open(sys.argv[1], 'r') as f:
    b27 = f.read()
b9 = 2 * fonk3(sys.argv[1]) + 1
b10 = fonk7(b26, b9)
fonk1(b10[0], 'y0')
fonk1(b10[1], 'y1')
b28 = fonk9(b26, b27, b9)
print("Verify:", fonk10(b26, b27, b28, b10))
fonk1(b28[0], 's0')
fonk1(b28[1], 's1')
print("test Schnorr", fonk2(str(fonk6(fonk7(b26, b28[0]), fonk7(b10, b28[1]))[0]) + b27) == b28[1])