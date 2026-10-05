
from b10 import *
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
        b6 = b5 ** 3 + b1 * b5 + b2 % b3
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
def fonk4(b8):
    b11 = []
    for i in range(len(b8)):
        b11.append(ECdecode(b8[i]))
    return ''.join(b11)
def fonk5(b8, key, k):
    return fonk4(decrypt_long(b8, key, k))
def fonk6(low, high):
    while True:
        b12 = randint(low, high)
        if miller_rabin(b12, 45):
            return b12
