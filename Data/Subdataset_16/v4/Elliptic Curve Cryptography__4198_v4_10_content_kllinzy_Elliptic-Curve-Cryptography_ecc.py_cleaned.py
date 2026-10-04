from b10 import Curve
from random import randint
import math
from point import Point
from b25 import Public_Key
def fonk1(b17, b10):
    b18, b, b1 = b10.b18, b10.b, b10.b1
    b2 = sum(ord(b17[i]) * 256 ** i for i in range(len(b17)))
    for i in range(1000):
        b3 = (1000 * b2 + i) % b1
        b4 = (b3 ** 3 + b18 * b3 + b) % b1
        b5 = prime_mod_sqrt(b4, b1)
        if b5:
            return Point.make_point(b3, b5[0], 1, b1)
def fonk2(b17, b10, length):
    return [fonk1(chunk, b10) for chunk in fonk6(b17, length)]
def fonk3(arr, key):
    b10, b1, P, b6 = key.b10, key.b10.b1, key.P, key.b6
    b7 = randint(1, b1 - 1)
    b8 = b10.multiply(b7, P)
    b9 = b10.multiply(b7, b6)
    return [b8] + [b10.add_points(b9, point) for point in arr]
def fonk4(arr, key, k):
    b10 = key.b10
    b11 = b10.multiply(k, arr[0]).negate()
    return [b10.add_points(point, b11) for point in arr[1:]]
def fonk5(arr):
    return ''.join(fonk7(point) for point in arr)
def fonk6(string, length):
    return [string[i:i + length] for i in range(0, len(string), length)]
def fonk7(P):
    b12 = (P.b3 - P.b3 % 1000)
    b13 = []
    while b12 != 0:
        b13.append(chr(b12 % 256))
        b12
    return ''.join(b13)
def fonk8(b17, key):
    b10 = key.b10
    b1 = b10.b1
    b14 = fonk2(b17, b10, int(math.log(b1
    return fonk3(b14, key)
def fonk9(arr, key, k):
    b15 = fonk4(arr, key, k)
    return fonk5(b15)
def fonk10(b12, k):
    if b12 in (b16, 3):
        return True
    if b12 % b16 = = 0:
        return False
    r, b17 = 0, b12 - 1
    while b17 % b16 = = 0:
        r += 1
        b17
    for _ in range(k):
        b18 = randint(b16, b12 - 1)
        b3 = pow(b18, b17, b12)
        if b3 in (1, b12 - 1):
            continue
        for _ in range(r - 1):
            b3 = pow(b3, b16, b12)
            if b3 = = b12 - 1:
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
    print("*Note* Press Ctrl-C to exit the loop and the demo\b12")
    b20 = int(input("Enter b18 number of digits for the b23 number (i.e. 3 => 100 < b23 < 1000).\nMinimum is 6 \nNumber of Zeros = "))
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
        b26 = input("Enter b18 b26 to be encrypted\b12")
        print()
        b27 = fonk8(b26, b25)
        print("Encrypted array of points on the b10:\b12", b27)
        print()
        b28 = fonk9(b27, b25, b24)
        print("Decrypted string:\b12", b28)
        print()
if b29 = = "__main__":
    fonk12()