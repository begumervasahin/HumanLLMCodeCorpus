import random
import math
def fonk1(p, b6):
    b1 = p * b6
    b2 = (p - 1) * (b6 - 1)
    b3 = fonk2(b2, b1)
    b4 = fonk3(b3, b2)
    return b1, b3, b4
def fonk2(b2, b1):
    b5 = [b3 for b3 in range(2, b2) if math.gcd(b3, b2) == 1 and math.gcd(b3, b1) == 1]
    return random.choice(b5)
def fonk3(b3, b2):
    for b4 in range(1, b2):
        if (b4 * b3) % b2 = = 1:
            return b4
    return None
def fonk4(b3, b1, a1):
    return pow(a1, b3, b1)
def fonk5(b4, b1, b7):
    return pow(b7, b4, b1)
def fonk6():
    p, b6 = 1733, 1301
    b1, b3, b4 = fonk1(p, b6)
    print(f"Public key (b3, b1): ({b3}, {b1})")
    print(f"Private key (b4, b1): ({b4}, {b1})")
    a1 = 2999
    print(f"Original message: {a1}")
    b7 = fonk4(b3, b1, a1)
    print(f"Encrypted message: {b7}")
    b8 = fonk5(b4, b1, b7)
    print(f"Decrypted message: {b8}")
if b9 = = "__main__":
    fonk6()