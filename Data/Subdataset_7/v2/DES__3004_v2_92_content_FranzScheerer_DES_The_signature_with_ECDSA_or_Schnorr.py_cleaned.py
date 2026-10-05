import sys
import hashlib
import random
import time
def fonk1(number, fname):
    with open(fname, 'wb') as f:
        while number > 0:
            b1 = number % 256
            number
            f.write(chr(b1))
def fonk2(b22):
    b2 = hashlib.sha256(b22.encode()).digest()
    a1 = 0
    for cx in b2:
        a1 = (a1 << 8) ^ cx
    return a1
def fonk3(m):
    b3 = hashlib.sha256("***RANDOM-SEED_X***".encode())
    b3.update('large key value for generation of random number'.encode())
    b3.update(m.encode())
    a2 = 0
    b4 = b3.digest()
    for i in range(len(b4)):
        a2 = (a2 << 8) ^ ord(b4[i])
    return a2
def fonk4(m):
    b3 = hashlib.sha256("***RANDOM-SEED_X***".encode())
    b3.update('large key value for generation of random number'.encode())
    b3.update(m.encode())
    b3.update(str(time.gmtime().tm_year + time.gmtime().tm_mday).encode())
    a2 = 0
    b4 = b3.digest()
    for i in range(len(b4)):
        a2 = (a2 << 8) ^ ord(b4[i])
    return a2
def fonk5(b22, b19, b):
    if (4 * b19 * b19 * b19 + 27 * b * b) % b5 = = 0:
        b += 1
    while pow(a4 * b22 ** 3 + b19 * b22 + b, (b5 - 1)
        b22 += 1
    b6 = pow(a4 * b22 ** 3 + b19 * b22 + b, (b5 + 1)
    return [b22 % b5, (b6) % b5]
def fonk6(b20, b8):
    b7 = b20
    if b8 < 0:
        b7[1] = b5 - b7[1]
        b8 = -b8
    a3 = 20
    while 2 ** a3 < b8:
        a3 += 1
    b9 = b7
    for b in range(a3 + 1):
        if (b8 & (1 << b) != 0):
            b7 = b9 if b == 0 else add_P(b7, b9)
        b9 = d_point(b9)
    return b7
def fonk7(G, m, b22):
    b10 = fonk4(m)
    b11 = fonk6(G, b10)
    b12 = fonk2(str(b11[0]) + m)
    return [(b10 - b22 * b12) % b18, b12]
def fonk8(G, m, b22):
    b10 = fonk4(m)
    b11 = fonk6(G, b10)
    b13 = fonk2(m + str(b11[0]))
    b14 = (inv(b10, b18) * (b13 + b11[0] * b22)) % b18
    return [b14, b11[0]]
def fonk9(G, m, S, Y):
    b15 = inv(S[0], b18)
    b13 = fonk2(m + str(S[1]))
    b16 = (b15 * b13) % b18
    b17 = (b15 * S[1]) % b18
    return add_P(fonk6(G, b16), fonk6(Y, b17))[0] == S[1]
def fonk10():
    global b5, b18, a4
    b5 = 2 ** 256 - 2 ** 224 + 2 ** 192 + 2 ** 96 - 1
    b18 = (b5 + 1)
    a4 = 1
    b19 = b5 - 1
    b20 = fonk5(b19 - 17, b19, 0)
    with open(sys.argv[1], 'r') as f:
        b21 = f.read()
    b22 = 2 * fonk3(sys.argv[1]) + 1
    b6 = fonk6(b20, b22)
    fonk1(b6[0], 'y0')
    fonk1(b6[1], 'y1')
    b23 = fonk8(b20, b21, b22)
    print("Verify:", fonk9(b20, b21, b23, b6))
    fonk1(b23[0], 's0')
    fonk1(b23[1], 's1')
    print("Test Schnorr:", fonk2(str(add_P(fonk6(b20, b23[0]), fonk6(b6, b23[1]))[0]) + b21) == b23[1])
if b24 = = "__main__":
    fonk10()