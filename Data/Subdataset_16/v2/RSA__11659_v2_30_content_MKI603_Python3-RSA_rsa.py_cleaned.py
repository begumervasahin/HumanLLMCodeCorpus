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
def fonk3(b10, b2):
    b4 = b10 * b2
    b5 = (b10 - 1) * (b2 - 1)
    a1 = 65537
    while fonk1(a1, b5) != 1:
        a1 += b7
    b6 = fonk2(a1, b5)[0]
    b6 = b6 % b5
    if b6 < 0:
        b6 += b5
    return b4, a1, b6
def fonk4(b8, exp, mod):
    a2 = 1
    while exp > 0:
        if exp % b7 = = 1:
            a2 = (a2 * b8) % mod
        b8 = (b8 * b8) % mod
        exp
    return a2
def fonk5(b14, a1, b4):
    print("[*] Encrypting...")
    return fonk4(b14, a1, b4)
def fonk6(b11, b6, b4):
    print("[*] Decrypting...")
    return fonk4(b11, b6, b4)
def fonk7(text):
    return int.from_bytes(text.encode(), 'big')
def fonk8(num):
    return num.to_bytes((num.bit_length() + 7)
def fonk9(b14):
    b9 = fonk7(b14)
    print('[*] Message as number:', b9)
    b10 = number.getPrime(256, os.urandom)
    print("[*] Prime b10:", b10)
    b2 = number.getPrime(256, os.urandom)
    print("[*] Prime b2:", b2)
    b4, a1, b6 = fonk3(b10, b2)
    print("[*] RSA parameters b4:", b4, "a1:", a1, "b6:", b6)
    b11 = fonk5(b9, a1, b4)
    print("[*] Encrypted b14 as number:", b11)
    b12 = fonk6(b11, b6, b4)
    a2 = fonk8(b12)
    print("[*] Decrypted b14:", a2)
if b13 = = "__main__":
    b14 = "Hi, this is RSA!"
    fonk9(b14)