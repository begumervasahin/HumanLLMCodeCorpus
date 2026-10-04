import random
import math
def fonk1(p, b6):
    b1 = p * b6
    b2 = (p - 1) * (b6 - 1)
    b3 = []
    for b4 in range(2, b2):
        print("Finding possible relative primes...", int((b4 / b2) * 100), "%")
        if math.gcd(b4, b1) == 1 and math.gcd(b4, b2) == 1:
            b3.append(b4)
    b4 = random.choice(b3)
    b5 = fonk2(b4, b2)
    return b1, b4, b5
def fonk2(b4, b2):
    for b5 in range(1, b2):
        if (b5 * b4) % b2 = = 1:
            return b5
    return None
def fonk3(b4, b1, a1):
    return pow(a1, b4, b1)
def fonk4(b5, b1, b7):
    return pow(b7, b5, b1)
def fonk5():
    p, b6 = 1733, 1301
    b1, b4, b5 = fonk1(p, b6)
    print(f"Public key (b4, b1): ({b4}, {b1})")
    print(f"Private key (b5, b1): ({b5}, {b1})")
    a1 = 2999
    print(f"Original message: {a1}")
    b7 = fonk3(b4, b1, a1)
    print(f"Encrypted message: {b7}")
    b8 = fonk4(b5, b1, b7)
    print(f"Decrypted message: {b8}")
if b9 = = "__main__":
    fonk5()