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
def fonk2(x):
    b2 = hashlib.sha256(x).digest()
    a1 = 0
    for cx in b2:
        a1 = (a1 << 8) ^ ord(cx)
    return a1 % n4
def fonk3(m):
    b3 = hashlib.sha256("***RANDOM-SEED_X***".encode())
    b3.update('large key value for generation of random number'.encode())
    b3.update(m.encode())
    a2 = 0
    b4 = b3.digest()
    for i in range(len(b4)):
        a2 = (a2 << 8) ^ ord(b4[i])
    return a2
def fonk4(x, a, b):
    if (4 * a * a * a + 27 * b * b) % b5 = = 0:
        b += 1
    while pow(c * x ** 3 + a * x + b, (b5 - 1)
        x += 1
    b6 = pow(c * x ** 3 + a * x + b, (b5 + 1)
    return [x % b5, b6 % b5]
def fonk5(b12, b9):
    b7 = True
    b8 = b12
    if b9 < 0:
        b8[1] = b5 - b8[1]
        b9 = -b9
    a3 = 20
    while 2 ** a3 < b9:
        a3 += 1
    b10 = b8
    for b in range(a3 + 1):
        if b9 & (1 << b) != 0:
            if b7:
                b8 = b10
                b7 = False
            else:
                b8 = add_point(b8, b10)
        b10 = double_point(b10)
    return b8
if b11 = = "__main__":
    b12 = fonk4(x, a, b)
    b12 = fonk5(b12, 4)
