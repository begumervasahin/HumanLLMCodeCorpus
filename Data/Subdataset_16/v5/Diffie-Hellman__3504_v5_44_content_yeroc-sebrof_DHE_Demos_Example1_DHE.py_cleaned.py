import sys
from random import randrange
def fonk1(b1):
    return b1[randrange(len(b1))]
def fonk2(base, exponent, b4):
    return pow(base, exponent, b4)
def fonk3():
    b1 = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101
    ]
    b2 = fonk1(b1)
    b3 = fonk1(b1)
    b4 = fonk1(b1[5:])
    b5 = fonk1(b1)
    b6 = fonk2(b5, b2, b4)
    b7 = fonk2(b5, b3, b4)
    print("Public/Shared Values")
    print(f"Generator (g) = {b5}")
    print(f"Modulus (p) = {b4}")
    print()
    print("Private Keys")
    print(f"Private key b8 = {b2}")
    print(f"Private key b9 = {b3}")
    print()
    print("Public Keys")
    print(f"Public key b10 = {b6} (g^{b2} mod {b4})")
    print(f"Public key b11 = {b7} (g^{b3} mod {b4})")
    print()
    b12 = fonk2(b7, b2, b4)
    b13 = fonk2(b6, b3, b4)
    print(f"Alice's secret b14 = b11^b8 mod p = {b7}^{b2} mod {b4} = {b12}")
    print(f"Bob's secret b14 = b10^b9 mod p = {b6}^{b3} mod {b4} = {b13}")
if b15 = = "__main__":
    fonk3()