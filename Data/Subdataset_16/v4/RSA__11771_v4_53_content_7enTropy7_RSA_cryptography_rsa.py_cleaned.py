from math import sqrt
import random
import sympy
import time
import binascii
def fonk1(b5, b1):
    while b1:
        b5, b1 = b1, b5 % b1
    return b5
def fonk2(b5, b1):
    x, b6, u, b2 = 0, 1, 1, 0
    while b5 != 0:
        b9, b3 = b1
        m, b4 = x - u * b9, b6 - b2 * b9
        b1, b5 = b5, b3
        x, b6, u, b2 = u, b2, m, b4
    return b1, x, b6
def fonk3(b5, m):
    g, x, b6 = fonk2(b5, m)
    if g != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m
def fonk4(b4):
    if b4 < 2:
        return False
    for b7 in range(2, int(sqrt(b4)) + 1):
        if b4 % b7 = = 0:
            return False
    return True
def fonk5(bitlength):
    b5 = 1 << (bitlength - 1)
    b1 = (1 << bitlength) - 1
    return sympy.randprime(b5, b1)
def fonk6(keysize):
    b8 = fonk5(keysize)
    b9 = fonk5(keysize)
    print(f"Generated primes b8: {b8}, b9: {b9}")
    b4 = b8 * b9
    b10 = (b8 - 1) * (b9 - 1)
    b11 = sympy.randprime(1, b10)
    b12 = fonk3(b11, b10)
    print(f"Generated public key (b11, b4): ({b11}, {b4})")
    print(f"Generated private key (b12, b4): ({b12}, {b4})")
    return (b11, b4), (b12, b4)
def fonk7(b17, public_key):
    b11, b4 = public_key
    if b17 > b4:
        raise ValueError("Message is too large for the key to handle")
    return pow(b17, b11, b4)
def fonk8(ciphertext, b14):
    b12, b4 = b14
    b13 = pow(ciphertext, b12, b4)
    return binascii.unhexlify(hex(b13)[2:]).decode()
def fonk9():
    public_key, b14 = fonk6(1024)
    b15 = input("Write b15: ")
    b16 = binascii.hexlify(b15.encode())
    b17 = int(b16, 16)
    b18 = time.time()
    b19 = fonk7(b17, public_key)
    print(f"Encrypted message: {b19}")
    b13 = fonk8(b19, b14)
    print(f"Decrypted message: {b13}")
    print(f'Runtime: {time.time() - b18} seconds')
if b20 = = "__main__":
    fonk9()