from b10 import Curve
from random import randint
import math
import sys
from point import Point
from b25 import Public_Key
def fonk1(b4, b10):
    b1 = b10.b1
    b2 = b10.b2
    b3 = b10.b3
    b4 = str(b4)
    a1 = 0
    for i in range(len(b4)):
        a1 += ord(b4[i]) * 256 ** i
    for i in range(1000):
        b5 = (1000 * a1 + i) % b3
        b6 = (b5 ** 3 + b1 * b5 + b2) % b3
        b7 = prime_mod_sqrt(b6, b3)
        if b7:
            return Point.make_point(b5, b7[0], 1, b3)
def fonk2(b4, b10, length):
    b8 = []
    b9 = list(fonk6(b4, length))
    for chunk in b9:
        b8.append(fonk1(chunk, b10))
    return b8
def fonk3(b8, key):
    b10 = key.b10
    b3 = b10.b3
    b11 = key.b11
    b12 = key.b12
    b13 = randint(1, b3 - 1)
    b7 = [b10.multiply(b13, b11)]
    b14 = b10.multiply(b13, b12)
    for point in b8:
        b7.append(b10.add_points(b14, point))
    return b7
def fonk4(b8, key, k):
    b7 = []
    b10 = key.b10
    b15 = b10.multiply(k, b8[0]).negate()
    for point in b8[1:]:
        b7.append(b10.add_points(point, b15))
    return b7
def fonk5(b8):
    return ''.join(fonk7(point) for point in b8)
def fonk6(string, length):
    return (string[i:i + length] for i in range(0, len(string), length))
def fonk7(b11):
    b16 = (b11.b5 - b11.b5 % 1000)
    b17 = []
    while b16 != 0:
        b17.append(chr(b16 % 256))
        b16
    return ''.join(b17)
def fonk8(b4, key):
    b10 = key.b10
    b3 = b10.b3
    return fonk3(fonk2(b4, b10, int(math.log(b3
def fonk9(b8, key, k):
    return fonk5(fonk4(b8, key, k))
def fonk10(b16, k):
    if b16 = = b18 or b16 == 3:
        return True
    if b16 % b18 = = 0:
        return False
    r, b4 = 0, b16 - 1
    while b4 % b18 = = 0:
        r += 1
        b4
    for _ in range(k):
        b1 = randint(b18, b16 - 1)
        b5 = pow(b1, b4, b16)
        if b5 = = 1 or b5 == b16 - 1:
            continue
        for _ in range(r - 1):
            b5 = pow(b5, b18, b16)
            if b5 = = b16 - 1:
                break
        else:
            return False
    return True
def fonk11(b21, b22):
    while True:
        b19 = randint(b21, b22)
        if fonk10(b19, 45):
            return b19
def fonk12():
    print("\nElliptic Curve Cryptosystem: written by Kyle Linzy")
    print("*Note* Press Ctrl-C to exit the loop and the demo\b16")
    b20 = int(input("Enter b1 number of digits for the b23 number (i.e. 3 => 100 < b23 < 1000).\nMinimum is 6 \nNumber of Zeros = "))
    if b20 < 6:
        b20 = 6
    b21 = 10 ** (b20 - 1)
    b22 = b21 * 10
    b23 = fonk11(b21, b22)
    b24 = randint(1, b23 - 1)
    b25 = Public_Key.make_public_key(b23, b24)
    print(b25)
    print()
    while True:
        b26 = input("Enter b1 b26 to be encrypted\b16")
        print()
        b27 = fonk8(b26, b25)
        print("Encrypted array of points on the b10:\b16", b27)
        print()
        b28 = fonk9(b27, b25, b24)
        print("Decrypted string:\b16", b28)
        print()
if b29 = = "__main__":
    fonk12()