import sys
import hashlib
import random
import time
def fonk1(number, filename):
    with open(filename, 'wb') as file:
        while number > 0:
            b1 = number % 256
            number
            file.write(b1.to_bytes(1, 'big'))
b2 = 2 ** 160 * 115 + 86427
b3 = (b2 + 1)
b4 = b2 - 1
a1 = 0
a2 = 1
def fonk2(b25):
    b5 = hashlib.sha256(b25.encode()).b5()
    a3 = 0
    for b1 in b5:
        a3 = (a3 << 8) ^ b1
    return a3 % b3
def fonk3(m):
    b6 = hashlib.sha256("***RANDOM-SEED_X***".encode())
    b6.update('large key value for generation of random number'.encode())
    b6.update(m.encode())
    b7 = int.from_bytes(b6.b5(), 'big')
    return b7
def fonk4(m):
    b6 = hashlib.sha256("***RANDOM-SEED_X***".encode())
    b6.update('large key value for generation of random number'.encode())
    b6.update(m.encode())
    b6.update(str(time.gmtime().tm_year + 7 * time.gmtime().tm_mday).encode())
    b7 = int.from_bytes(b6.b5(), 'big')
    return b7
def fonk5(b25, b4, a1):
    global a2
    if (4 * b4 * b4 * b4 + 27 * a1 * a1) % b2 = = 0:
        a1 += 1
    while pow(a2 * b25 ** 3 + b4 * b25 + a1, (b2 - 1)
        b25 += 1
    b8 = pow(a2 * b25 ** 3 + b4 * b25 + a1, (b2 + 1)
    return [b25 % b2, b8 % b2]
def fonk6(b26, Q):
    b10, x2, y1, b9 = b26[0], Q[0], b26[1], Q[1]
    while b10 < x2:
        b10 += b2
    if b10 = = x2:
        b11 = ((3 * a2 * (b10 ** 2) + b4) * pow(2 * y1, b2 - 2, b2)) % b2
    else:
        b11 = ((y1 - b9) * pow(b10 - x2, b2 - 2, b2)) % b2
    b12 = a4 * b11 ** 2 - b10 - x2
    b13 = b11 * (b10 - b12) - y1
    return [b12 % b2, b13 % b2]
def fonk7(b26, b16):
    global a4
    b14 = True
    b15 = b26
    if b16 < 0:
        b15[1] = b2 - b15[1]
        b16 = -b16
    b17 = b15
    while b16 > 0:
        if b16 & 1 != 0:
            if b14:
                b15 = b17
                b14 = False
            else:
                b15 = fonk6(b15, b17)
        b17 = fonk6(b17, b17)
        b16
    return b15
def fonk8(G, b27, b25):
    b18 = fonk4(b27)
    b19 = fonk7(G, b18)
    b20 = fonk2(str(b19[0]) + b27)
    return [(b18 - b25 * b20) % b3, b20]
def fonk9(G, b27, b25):
    b18 = fonk4(b27)
    b19 = fonk7(G, b18)
    b21 = fonk2(b27 + str(b19[0]))
    b11 = (pow(b18, b3 - 2, b3) * (b21 + b19[0] * b25)) % b3
    return [b11, b19[0]]
def fonk10(G, b27, S, Y):
    b22 = pow(S[0], b3 - 2, b3)
    b21 = fonk2(b27 + str(S[1]))
    b23 = (b22 * b21) % b3
    b24 = (b22 * S[1]) % b3
    return fonk6(fonk7(G, b23), fonk7(Y, b24))[0] == S[1]
b25 = b4 - 17
a4 = 1
b26 = fonk5(b25, b4, a1)
b26 = fonk7(b26, 4)
with open(sys.argv[1], 'r') as f:
    b27 = f.read()
b25 = 2 * fonk3(sys.argv[1]) + 1
b8 = fonk7(b26, b25)
fonk1(b8[0], 'y0')
fonk1(b8[1], 'y1')
b28 = fonk9(b26, b27, b25)
print("Verify:", fonk10(b26, b27, b28, b8))
fonk1(b28[0], 's0')
fonk1(b28[1], 's1')
print("Test Schnorr:", fonk2(str(fonk6(fonk7(b26, b28[0]), fonk7(b8, b28[1]))[0]) + b27) == b28[1])