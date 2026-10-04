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
        x, y, b2 = fonk2(b1, a % b1)
        return y, x - (a
def fonk3(b9, b10):
    b3 = b9 * b10
    b4 = (b9 - 1) * (b10 - 1)
    a1 = 65537
    if fonk1(a1, b4) != 1:
        raise ValueError("Chosen a1 is not coprime with b4, try a different a1")
    b5 = fonk2(a1, b4)[0]
    b5 = b5 % b4
    if b5 < 0:
        b5 += b4
    return b3, a1, b5
def fonk4(b7, exp, mod):
    a2 = 1
    while exp > 0:
        if exp % b6 = = 1:
            a2 = (a2 * b7) % mod
        b7 = (b7 * b7) % mod
        exp
    return a2
def fonk5(b14, a1, b3):
    print("[*] Encrypting...")
    return fonk4(b14, a1, b3)
def fonk6(b11, b5, b3):
    print("[*] Decrypting...")
    return fonk4(b11, b5, b3)
def fonk7(text):
    return int.from_bytes(text.encode(), 'big')
def fonk8(num):
    return num.to_bytes((num.bit_length() + 7)
def fonk9(b14):
    b8 = fonk7(b14)
    print('[*] Message as number:', b8)
    b9 = number.getPrime(256, os.urandom)
    print("[*] Prime b9:", b9)
    b10 = number.getPrime(256, os.urandom)
    print("[*] Prime b10:", b10)
    b3, a1, b5 = fonk3(b9, b10)
    print("[*] RSA parameters b3:", b3, "a1:", a1, "b5:", b5)
    b11 = fonk5(b8, a1, b3)
    print("[*] Encrypted b14 as number:", b11)
    b12 = fonk6(b11, b5, b3)
    a2 = fonk8(b12)
    print("[*] Decrypted b14:", a2)
if b13 = = "__main__":
    b14 = "Hi, this is RSA!"
    fonk9(b14)