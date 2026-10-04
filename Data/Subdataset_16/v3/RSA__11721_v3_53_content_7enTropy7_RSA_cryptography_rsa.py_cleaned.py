from __future__ import unicode_literals
from math import sqrt
import sympy
import time
import binascii
def fonk1(a, b1):
    while b1 != 0:
        a, b1 = b1, a % b1
    return a
def fonk2(a, b1):
    x, b5, u, b2 = 0, 1, 1, 0
    while a != 0:
        b9, b3 = b1
        m, b4 = x - u * b9, b5 - b2 * b9
        b1, a, x, b5, u, b2 = a, b3, u, b2, m, b4
    return b1, x, b5
def fonk3(a, m):
    g, x, b5 = fonk2(a, m)
    if g != 1:
        raise ValueError('Modular inverse does not exist')
    return x % m
def fonk4(bitlength):
    b6 = 1 << (bitlength - 1)
    b7 = (1 << bitlength) - 1
    return sympy.randprime(b6, b7)
def fonk5(a1):
    b8 = fonk4(a1)
    b9 = fonk4(a1)
    b4 = b8 * b9
    b10 = (b8 - 1) * (b9 - 1)
    b11 = sympy.randprime(1, b10)
    b12 = fonk3(b11, b10)
    return (b11, b4), (b12, b4)
def fonk6(b13, public_key):
    b11, b4 = public_key
    if b13 > b4:
        raise ValueError('Message is too large for key to handle')
    return pow(b13, b11, b4)
def fonk7(ciphertext, b14):
    b12, b4 = b14
    b13 = pow(ciphertext, b12, b4)
    return binascii.unhexlify(hex(b13)[2:]).decode()
def fonk8():
    a1 = 1024
    public_key, b14 = fonk5(a1)
    print('Public Key:', public_key)
    print('Private Key:', b14)
    b15 = input("Write b15: ")
    b16 = binascii.hexlify(b15.encode())
    b13 = int(b16, 16)
    b17 = time.time()
    b18 = fonk6(b13, public_key)
    print("Encrypted b15:", b18)
    b19 = fonk7(b18, b14)
    print("Decrypted b15:", b19)
    print('Runtime:', time.time() - b17, 'seconds')
if b20 = = "__main__":
    fonk8()