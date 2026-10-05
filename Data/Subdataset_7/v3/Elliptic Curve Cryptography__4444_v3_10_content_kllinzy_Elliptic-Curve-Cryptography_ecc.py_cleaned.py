
from b15 import Curve
from point import Point
from public_key import Public_Key
from random import randint
import math
def fonk1(string, b15, b11):
    b1 = []
    b2 = fonk3(string, b11)
    for chunk in b2:
        b1.append(fonk2(chunk, b15))
    return b1
def fonk2(chunk, b15):
    a, b, b3 = b15.a, b15.b, b15.b3
    b4 = string_to_int(chunk)
    for i in range(1000):
        b5 = 1000 * b4 + i % b3
        b6 = (b5 ** 3 + a * b5 + b) % b3
        b7 = prime_mod_sqrt(b6, b3)
        if len(b7) != 0:
            return Point.make_point(b5, b7[0], 1, b3)
def fonk3(string, length):
    return [string[i:i+length] for i in range(0, len(string), length)]
def fonk4(b1):
    b8 = []
    for point in b1:
        b8.append(fonk5(point))
    return ''.join(b8)
def fonk5(point):
    b9 = (point.b5 - point.b5 % 1000)
    b10 = []
    while b9 != 0:
        b10.append(chr(b9 % 256))
        b9
    return ''.join(b10[::-1])
def fonk6(string, key):
    b15, b3 = key.b15, key.b15.b3
    b11 = int(math.log(b3
    b12 = fonk1(string, b15, b11)
    return fonk7(b12, key)
def fonk7(b1, key):
    b15, b3 = key.b15, key.b15.b3
    b13 = randint(1, b3 - 1)
    b7 = [b15.multiply(b13, key.P)]
    b14 = b15.multiply(b13, key.Q)
    for point in b1:
        b7.append(b15.add_points(b14, point))
    return b7
def fonk8(b1, key, k):
    b15 = key.b15
    b16 = b15.multiply(k, b1[0]).negate()
    b17 = []
    for point in b1[1:]:
        b18 = b15.add_points(point, b16)
        b17.append(b18)
    return b17
def fonk9(low, high):
    while True:
        b19 = randint(low, high)
        if miller_rabin(b19, 45):
            return b19
