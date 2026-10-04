from __future__ import unicode_literals
from math import sqrt
import random
from random import randint as rand
from random import getrandbits
import sympy
import time
import binascii
def fonk1(b7, b1):
    if b1 = = 0:
        return b7
    else:
        return fonk1(b1, b7 % b1)
def fonk2(b7, b1):
    x,b5, u,b2 = 0,1, 1,0
    while b7 != 0:
        b9, b3 = b1
        m, b4 = x-u*b9, b5-b2*b9
        b1,b7, x,b5, u,b2 = b7,b3, u,b2, m,b4
    return b1, x, b5
def fonk3(b7, m):
    g, x, b5 = fonk2(b7, m)
    if g != 1:
        return None
    else:
        return x % m
def fonk4(b4):
    if b4 < 2:
        return False
    elif b4 = = 2:
        return True
    else:
        for b6 in range(1, int(sqrt(b4)) + 1):
            if b4 % b6 = = 0:
                return False
    return True
def fonk5(bitlength):
    b7 = '1'+'0'*(bitlength-1)
    b1 = '1'*bitlength
    b8 = sympy.randprime(int(b7, 2), int(b1, 2))
    return b8
def fonk6(keysize):
    b8 = fonk5(keysize)
    b9 = fonk5(keysize)
    print(b8, b9)
    b4 = b8 * b9
    b10 = (b8-1)*(b9-1)
    b11 = sympy.randprime(1,b10)
    b12 = fonk3(b11,b10)
    if b11 != b12:
        return ((b11, b4), (b12, b4))
def fonk7(b18, package):
    b11, b4 = package
    if b18 > b4:
        print('Message is too large for key to handle')
    b13 = pow(b18, b11, b4)
    return b13
def fonk8(b13, package):
    b12, b4 = package
    b14 = pow(b13, b12, b4)
    return binascii.unhexlify(hex(b14)[2:]).decode()
public, b15 = fonk6(1024)
print('Public Key : ',public)
print('Private Key : ',b15)
b16 = input("Write b16: ")
b17 = binascii.hexlify(b16.encode())
b18 = int(b17, 16)
b19 = time.time()
b20 = fonk7(b18, public)
print("Encrypted b16: " + str(b20))
b21 = fonk8(b20, b15)
print("Decrypted b16: " + str(b21))
print('Runtime : ' + str(time.time()-b19) + ' seconds')