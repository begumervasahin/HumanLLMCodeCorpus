from b10 import Curve
from random import randint
import math
from point import Point
from public_key import Public_Key
def fonk1(b4, b10):
    b1 = b10.b1
    b2 = b10.b2
    b3 = b10.b3
    b4 = str(b4)
    a1 = 0
    for i in range(len(b4)):
        a1 += ord(b4[i]) * 256 ** i
    for i in range(1000):
        b5 = 1000 * a1 + i % b3
        b6 = (b5 ** 3 + b1 * b5 + b2) % b3
        b7 = prime_mod_sqrt(b6, b3)
        if len(b7) != 0:
            return Point.make_point(b5, b7[0], 1, b3)
def fonk2(b4, b10, length):
    b8 = []
    b9 = list(chunkstring(b4, length))
    for i in range(len(b9)):
        b8.append(fonk1(b9[i], b10))
    return b8
def fonk3(b4, key):
    b10 = key.b10
    b3 = b10.b3
    return encrypt_long(fonk2(b4, b10, int(math.log(b3
def fonk4(b8, key, k):
    return decode_string(decrypt_long(b8, key, k))
def fonk5(low, high):
    a2 = 0
    while True:
        a2 = randint(low, high)
        if fonk6(a2, 45):
            break
    return a2
def fonk6(b11, k):
    if b11 = = b12 or b11 == 3:
        return True
    if b11 % b12 = = 0:
        return False
