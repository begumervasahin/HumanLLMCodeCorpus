import math
from Crypto.Util import number
import os
def fonk1(a, b1):
    while b1:
        a, b1 = b1, a % b1
    return a
def fonk2(a, b1):
    if b1 = = 0:
        return 1, 0, a
    else:
        x, b3, b2 = fonk2(b1, a % b1)
        x, b3 = b3, x - (a
        return x, b3, b2
def fonk3(b13, b14):
    b4 = b13 * b14
    b5 = (b13 - 1) * (b14 - 1)
    a1 = b8
    while fonk1(a1, b5) != 1:
        a1 += 1
    b7, b6, b6 = fonk2(a1, b5)
    b7 = b7 % b5
    if b7 < 0:
        b7 += b5
    return b4, b5, a1, b7
def fonk4(b9, exp, mod):
    a2 = 1
    while exp > 0:
        if exp % b8 = = 1:
            a2 = (a2 * b9) % mod
        b9 = (b9 * b9) % mod
        exp
    return a2
def fonk5(b18, a1, b4):
    print("[*] Encrypting...")
    return fonk4(b18, a1, b4)
def fonk6(b15, b7, b4):
    print("[*] Decrypting...")
    return fonk4(b15, b7, b4)
def fonk7(b11):
    b10 = ''.join(format(ord(char), '08b') for char in b11)
    return int(b10, b8)
def fonk8(num):
    b10 = bin(num)[b8:]
    b10 = b10.zfill((8 - len(b10) % 8) % 8 + len(b10))
    b11 = ''.join(chr(int(b10[i:i+8], b8)) for i in range(0, len(b10), 8))
    return b11
def fonk9(b11):
    b12 = fonk7(b11)
    print('[*] Numeric representation:', b12)
    b13 = number.getPrime(256, os.urandom)
    print("[*] Generated prime b13:", b13)
    b14 = number.getPrime(256, os.urandom)
    print("[*] Generated prime b14:", b14)
    print("[*] Starting key generation...")
    b4, b5, a1, b7 = fonk3(b13, b14)
    b15 = fonk5(b12, a1, b4)
    b16 = fonk6(b15, b7, b4)
    a2 = fonk8(b16)
    print("[*] Decrypted b18:", a2)
if b17 = = "__main__":
    b18 = "Hi, this is RSA!"
    fonk9(b18)