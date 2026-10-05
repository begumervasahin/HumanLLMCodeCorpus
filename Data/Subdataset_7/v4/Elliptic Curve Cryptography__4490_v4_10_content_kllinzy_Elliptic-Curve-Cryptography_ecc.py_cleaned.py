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
    b9 = list(fonk6(b4, length))
    for i in range(len(b9)):
        b8.append(fonk1(b9[i], b10))
    return b8
def fonk3(b4, key):
    b10 = key.b10
    b3 = b10.b3
    return fonk9(fonk2(b4, b10, int(math.log(b3
def fonk4(b8, key, k):
    return fonk7(fonk10(b8, key, k))
def fonk5(low, high):
    a2 = 0
    while True:
        a2 = randint(low, high)
        if fonk11(a2, 45):
            break
    return a2
def fonk6(string, length):
    return (string[i:i+length] for i in range(0, len(string), length))
def fonk7(b8):
    b11 = []
    for i in range(len(b8)):
        b11.append(fonk8(b8[i]))
    return ''.join(b11)
def fonk8(b13):
    b12 = (b13.b5 - b13.b5 % 1000)
    b11 = []
    while b12 != 0:
        b11.append(chr(b12 % 256))
        b12
    return ''.join(b11)
def fonk9(b8, key):
    b10 = key.b10
    b3 = b10.b3
    b13 = key.b13
    b14 = key.b14
    b9 = randint(1, b3 - 1)
    b7 = [b10.multiply(b9, b13)]
    b15 = b10.multiply(b9, b14)
    for i in range(len(b8)):
        b7.append(b10.add_points(b15, b8[i]))
    return b7
def fonk10(b8, key, k):
    b7 = []
    b10 = key.b10
    b16 = b10.multiply(k, b8[0]).negate()
    for i in range(1, len(b8)):
        b17 = b10.add_points(b8[i], b16)
        b7.append(b17)
    return b7
def fonk11(b12, k):
    if b12 = = b18 or b12 == 3:
        return True
    if b12 % b18 = = 0:
        return False
    r, b4 = 0, b12 - 1
    while b4 % b18 = = 0:
        r += 1
        b4
    for _ in range(k):
        b1 = randint(b18, b12 - 1)
        b5 = pow(b1, b4, b12)
        if b5 = = 1 or b5 == b12 - 1:
            continue
        for _ in range(r - 1):
            b5 = pow(b5, b18, b12)
            if b5 = = b12 - 1:
                break
        else:
            return False
    return True