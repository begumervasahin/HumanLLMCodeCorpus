from b7 import Curve
from random import randint
import math
from point import Point
from b27 import Public_Key
def fonk1(b19, b7):
    b20, b, b1 = b7.b20, b7.b, b7.b1
    b2 = sum(ord(b19[i]) * 256 ** i for i in range(len(b19)))
    for i in range(1000):
        b3 = (1000 * b2 + i) % b1
        b4 = (b3 ** 3 + b20 * b3 + b) % b1
        b5 = prime_mod_sqrt(b4, b1)
        if b5:
            return Point.make_point(b3, b5[0], 1, b1)
def fonk2(b19, b7, b15):
    b6 = fonk6(b19, b15)
    return [fonk1(chunk, b7) for chunk in b6]
def fonk3(arr, key):
    b7 = key.b7
    b1, P, b8 = b7.b1, key.P, key.b8
    b9 = randint(1, b1 - 1)
    b10 = b7.multiply(b9, P)
    b11 = b7.multiply(b9, b8)
    return [b10] + [b7.add_points(b11, point) for point in arr]
def fonk4(arr, key, k):
    b7 = key.b7
    b12 = b7.multiply(k, arr[0]).negate()
    return [b7.add_points(point, b12) for point in arr[1:]]
def fonk5(arr):
    return ''.join(fonk7(point) for point in arr)
def fonk6(string, b15):
    return [string[i:i + b15] for i in range(0, len(string), b15)]
def fonk7(P):
    b13 = (P.b3 - P.b3 % 1000)
    b14 = []
    while b13:
        b14.append(chr(b13 % 256))
        b13
    return ''.join(b14)
def fonk8(b19, key):
    b7 = key.b7
    b1 = b7.b1
    b15 = int(math.log(b1
    b16 = fonk2(b19, b7, b15)
    return fonk3(b16, key)
def fonk9(arr, key, k):
    b17 = fonk4(arr, key, k)
    return fonk5(b17)
def fonk10(b13, k):
    if b13 in (b18, 3):
        return True
    if b13 % b18 = = 0:
        return False
    r, b19 = 0, b13 - 1
    while b19 % b18 = = 0:
        r += 1
        b19
    for _ in range(k):
        b20 = randint(b18, b13 - 1)
        b3 = pow(b20, b19, b13)
        if b3 in (1, b13 - 1):
            continue
        for _ in range(r - 1):
            b3 = pow(b3, b18, b13)
            if b3 = = b13 - 1:
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
    print("*Note* Press Ctrl-C to exit the loop and the demo\b13")
    b22 = int(input("Enter b20 number of digits for the b25 number (i.e. 3 => 100 < b25 < 1000).\nMinimum is 6 \nNumber of Zeros = "))
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
        b28 = input("Enter b20 b28 to be encrypted\b13")
        print()
        b29 = fonk8(b28, b27)
        print("Encrypted array of points on the b7:\b13", b29)
        print()
        b30 = fonk9(b29, b27, b26)
        print("Decrypted string:\b13", b30)
        print()
if b31 = = "__main__":
    fonk12()