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
b2 = 2**160 * 115 + 86427
b3 = (b2 + 1)
b4 = b2 - 1
a1 = 0
a2 = 1
a3 = 1
def fonk2(b8):
    b5 = hashlib.sha256(b8.encode()).b5()
    a4 = 0
    for b1 in b5:
        a4 = (a4 << 8) ^ b1
    return a4 % b3
def fonk3(seed):
    b6 = hashlib.sha256("***RANDOM-SEED_X***".encode())
    b6.update('large key value for generation of random number'.encode())
    b6.update(seed.encode())
    b7 = int.from_bytes(b6.b5(), 'big')
    return b7
def fonk4(seed):
    b6 = hashlib.sha256("***RANDOM-SEED_X***".encode())
    b6.update('large key value for generation of random number'.encode())
    b6.update(seed.encode())
    b6.update(str(time.gmtime().tm_year + 7*time.gmtime().tm_mday).encode())
    b7 = int.from_bytes(b6.b5(), 'big')
    return b7
def fonk5(b8, b4, a1):
    global a2
    if (4*b4*b4*b4 + 27*a1*a1) % b2 = = 0:
        a1 = a1 + 1
    while pow(a2*b8**3 + b4*b8 + a1, (b2 - 1)
        b8 = b8 + 1
    b9 = pow(a2*b8**3 + b4*b8 + a1, (b2 + 1)
    return [b8 % b2, b9 % b2]
def fonk6(b26, Q):
    b11, x2, y1, b10 = b26[0], Q[0], b26[1], Q[1]
    while b11 < x2:
        b11 = b11 + b2
    if b11 = = x2:
        b12 = ((3*a2*(b11**2) + b4) * pow(2*y1, b2-2, b2)) % b2
    else:
        b12 = ((y1 - b10) * pow(b11 - x2, b2-2, b2)) % b2
    b13 = a3 * b12**2 - b11 - x2
    b14 = b12 * (b11 - b13) - y1
    return [b13 % b2, b14 % b2]
def fonk7(b26, b17):
    global a3
    b15 = True
    b16 = b26
    if b17 < 0:
        b16[1] = b2 - b16[1]
        b17 = (-1) * b17
    b18 = b16
    while b17 > 0:
        if b17 & 1 != 0:
            if b15:
                b16 = b18
                b15 = False
            else:
                b16 = fonk6(b16, b18)
        b18 = fonk6(b18, b18)
        b17
    return b16
def fonk8(G, b27, b8):
    b19 = fonk4(b27)
    b20 = fonk7(G, b19)
    b21 = fonk2(str(b20[0]) + b27)
    return [(b19 - b8*b21) % b3, b21]
def fonk9(G, b27, b8):
    b19 = fonk4(b27)
    b20 = fonk7(G, b19)
    b22 = fonk2(b27 + str(b20[0]))
    b12 = (pow(b19, b3-2, b3) * (b22 + b20[0]*b8)) % b3
    return [b12, b20[0]]
def fonk10(G, b27, S, Y):
    b23 = pow(S[0], b3-2, b3)
    b22 = fonk2(b27 + str(S[1]))
    b24 = (b23 * b22) % b3
    b25 = (b23 * S[1]) % b3
    return fonk6(fonk7(G, b24), fonk7(Y, b25))[0] == S[1]
b8 = b4 - 17
b26 = fonk5(b8, b4, a1)
b26 = fonk7(b26, 4)
with open(sys.argv[1], 'r') as f:
    b27 = f.read()
b8 = 2 * fonk3(sys.argv[1]) + 1
b9 = fonk7(b26, b8)
fonk1(b9[0], 'y0')
fonk1(b9[1], 'y1')
b28 = fonk9(b26, b27, b8)
print("Verify:", fonk10(b26, b27, b28, b9))
fonk1(b28[0], 's0')
fonk1(b28[1], 's1')
print("Test Schnorr:", fonk2(str(fonk6(fonk7(b26, b28[0]), fonk7(b9, b28[1]))[0]) + b27) == b28[1])