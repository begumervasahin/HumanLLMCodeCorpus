from b9 import Curve
from random import randint
import math
import sys
from point import Point
from b27 import Public_Key
def fonk1(b4, b9):
    b1 = b9.b1
    b2 = b9.b2
    b3 = b9.b3
    b4 = str(b4)
    b5 = sum(ord(b4[i]) * 256 ** i for i in range(len(b4)))
    for i in range(1000):
        b6 = (1000 * b5 + i) % b3
        b7 = (b6 ** 3 + b1 * b6 + b2) % b3
        b8 = prime_mod_sqrt(b7, b3)
        if b8:
            return Point.make_point(b6, b8[0], 1, b3)
def fonk2(b4, b9, length):
    return [fonk1(chunk, b9) for chunk in fonk6(b4, length)]
def fonk3(arr, key):
    b9 = key.b9
    b3 = b9.b3
    b10 = key.b10
    b11 = key.b11
    b12 = randint(1, b3 - 1)
    b13 = b9.multiply(b12, b10)
    b14 = b9.multiply(b12, b11)
    return [b13] + [b9.add_points(b14, point) for point in arr]
def fonk4(arr, key, k):
    b9 = key.b9
    b15 = b9.multiply(k, arr[0]).negate()
    return [b9.add_points(point, b15) for point in arr[1:]]
def fonk5(arr):
    return ''.join(fonk7(point) for point in arr)
def fonk6(string, length):
    return [string[i:i + length] for i in range(0, len(string), length)]
def fonk7(b10):
    b16 = (b10.b6 - b10.b6 % 1000)
    b17 = []
    while b16 != 0:
        b17.append(chr(b16 % 256))
        b16
    return ''.join(b17)
def fonk8(b4, key):
    b9 = key.b9
    b3 = b9.b3
    b18 = fonk2(b4, b9, int(math.log(b3
    return fonk3(b18, key)
def fonk9(arr, key, k):
    b19 = fonk4(arr, key, k)
    return fonk5(b19)
def fonk10(b16, k):
    if b16 in (b20, 3):
        return True
    if b16 % b20 = = 0:
        return False
    r, b4 = 0, b16 - 1
    while b4 % b20 = = 0:
        r += 1
        b4
    for _ in range(k):
        b1 = randint(b20, b16 - 1)
        b6 = pow(b1, b4, b16)
        if b6 in (1, b16 - 1):
            continue
        for _ in range(r - 1):
            b6 = pow(b6, b20, b16)
            if b6 = = b16 - 1:
                break
        else:
            return False
    return True
def fonk11(b23, b24):
    while True:
        b21 = randint(b23, b24)
        if fonk10(b21, 45):
            return b21
def fonk12():
    print("\nElliptic Curve Cryptosystem: written by Kyle Linzy")
    print("*Note* Press Ctrl-C to exit the loop and the demo\b16")
    b22 = int(input("Enter b1 number of digits for the b25 number (i.e. 3 => 100 < b25 < 1000).\nMinimum is 6 \nNumber of Zeros = "))
    if b22 < 6:
        b22 = 6
    b23 = 10 ** (b22 - 1)
    b24 = b23 * 10
    b25 = fonk11(b23, b24)
    b26 = randint(1, b25 - 1)
    b27 = Public_Key.make_public_key(b25, b26)
    print(b27)
    print()
    while True:
        b28 = input("Enter b1 b28 to be encrypted\b16")
        print()
        b29 = fonk8(b28, b27)
        print("Encrypted array of points on the b9:\b16", b29)
        print()
        b30 = fonk9(b29, b27, b26)
        print("Decrypted string:\b16", b30)
        print()
if b31 = = "__main__":
    fonk12()