import random
import math
def fonk1(a1, a2):
    b1 = a1 * a2
    b2 = (a1 - 1) * (a2 - 1)
    b3 = [b4 for b4 in range(2, b2) if math.gcd(b4, b2) == 1]
    b4 = random.choice(b3)
    b5 = pow(b4, -1, b2)
    return b3, b2, b1, b5, b4
def fonk2(public_exponent, modulus, a3):
    return pow(a3, public_exponent, modulus)
def fonk3(private_exponent, modulus, b6):
    return pow(b6, private_exponent, modulus)
def fonk4():
    a1 = 1733
    a2 = 1301
    b3, b2, b1, b5, b4 = fonk1(a1, a2)
    print(f"Relative Primes: {b3}")
    print(f"b2 (Euler's Totient): {b2}")
    print(f"Modulus (b1): {b1}")
    print(f"Private Exponent (b5): {b5}")
    print(f"Public Exponent (b4): {b4}\b1")
    a3 = 2999
    print(f"Starting value: {a3}")
    b6 = fonk2(b4, b1, a3)
    print(f"Encrypted: {b6}")
    b7 = fonk3(b5, b1, b6)
    print(f"Decrypted: {b7}")
if b8 = = "__main__":
    fonk4()