from math import sqrt
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
        b10, b3 = b1
        m, b4 = x - u * b10, b6 - b2 * b10
        b1, b5 = b5, b3
        x, b6, u, b2 = u, b2, m, b4
    return b1, x, b6
def fonk3(b5, m):
    g, x, b6 = fonk2(b5, m)
    if g != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m
def fonk4(bitlength):
    b7 = 1 << (bitlength - 1)
    b8 = (1 << bitlength) - 1
    return sympy.randprime(b7, b8)
def fonk5(keysize):
    b9 = fonk4(keysize)
    b10 = fonk4(keysize)
    print(f"Generated primes b9: {b9}, b10: {b10}")
    b4 = b9 * b10
    b11 = (b9 - 1) * (b10 - 1)
    b12 = sympy.randprime(1, b11)
    b13 = fonk3(b12, b11)
    print(f"Generated public key (b12, b4): ({b12}, {b4})")
    print(f"Generated private key (b13, b4): ({b13}, {b4})")
    return (b12, b4), (b13, b4)
def fonk6(b18, public_key):
    b12, b4 = public_key
    if b18 > b4:
        raise ValueError("Message is too large for the key to handle")
    return pow(b18, b12, b4)
def fonk7(ciphertext, b15):
    b13, b4 = b15
    b14 = pow(ciphertext, b13, b4)
    return binascii.unhexlify(hex(b14)[2:]).decode()
def fonk8():
    public_key, b15 = fonk5(1024)
    b16 = input("Write b16: ")
    b17 = binascii.hexlify(b16.encode())
    b18 = int(b17, 16)
    b19 = time.time()
    b20 = fonk6(b18, public_key)
    print(f"Encrypted message: {b20}")
    b14 = fonk7(b20, b15)
    print(f"Decrypted message: {b14}")
    print(f'Runtime: {time.time() - b19} seconds')
if b21 = = "__main__":
    fonk8()