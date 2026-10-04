from __future__ import unicode_literals
from math import sqrt
import random
import sympy
import time
import binascii
def fonk1(b6, b1):
    if b1 = = 0:
        return b6
    else:
        return fonk1(b1, b6 % b1)
def fonk2(b6, b1):
    x, b5, u, b2 = 0, 1, 1, 0
    while b6 != 0:
        b8, b3 = b1
        m, b4 = x - u * b8, b5 - b2 * b8
        b1, b6, x, b5, u, b2 = b6, b3, u, b2, m, b4
    return b1, x, b5
def fonk3(b6, m):
    g, x, b5 = fonk2(b6, m)
    if g != 1:
        return None
    else:
        return x % m
def fonk4(bitlength):
    b6 = '1' + '0' * (bitlength - 1)
    b1 = '1' * bitlength
    b7 = sympy.randprime(int(b6, 2), int(b1, 2))
    return b7
def fonk5(keysize):
    b7 = fonk4(keysize)
    b8 = fonk4(keysize)
    b4 = b7 * b8
    b9 = (b7 - 1) * (b8 - 1)
    b10 = sympy.randprime(1, b9)
    b11 = fonk3(b10, b9)
    if b10 != b11:
        return ((b10, b4), (b11, b4))
def fonk6(b17, package):
    b10, b4 = package
    if b17 > b4:
        raise ValueError('Message is too large for key to handle')
    b12 = pow(b17, b10, b4)
    return b12
def fonk7(b12, package):
    b11, b4 = package
    b13 = pow(b12, b11, b4)
    return binascii.unhexlify(hex(b13)[2:]).decode()
public, b14 = fonk5(1024)
print('Public Key : ', public)
print('Private Key : ', b14)
b15 = input("Write b15: ")
b16 = binascii.hexlify(b15.encode())
b17 = int(b16, 16)
b18 = time.time()
b19 = fonk6(b17, public)
print("Encrypted b15: " + str(b19))
b20 = fonk7(b19, b14)
print("Decrypted b15: " + str(b20))
print('Runtime : ' + str(time.time() - b18) + ' seconds')