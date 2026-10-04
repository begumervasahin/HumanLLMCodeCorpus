import random
import math
def fonk1(a1, a2):
    b1 = a1 * a2
    b2 = (a1 - 1) * (a2 - 1)
    b3 = []
    for b5 in range(2, b2):
        print("Working out the possible relative Primes...", int((b5 / b2) * 100), "%")
        if math.gcd(b5, b1) == 1 and math.gcd(b5, a1) == 1 and math.gcd(b5, a2) == 1 and math.gcd(b5, b2) == 1:
            b3.append(b5)
    b3.sort()
    b4 = False
    while not b4:
        b5 = random.choice(b3)
        b4 = fonk2(b5, b2)
    return b3, b2, b1, b4, b5
def fonk2(b5, b2):
    for b4 in range(1, b2):
        if (b4 * b5) % b2 = = 1:
            return b4
    return False
def fonk3(b5, b1, a3):
    return pow(a3, b5, b1)
def fonk4(b4, b1, a3):
    return pow(a3, b4, b1)
def fonk5():
    a1 = 1733
    a2 = 1301
    b3, b2, b1, b4, b5 = fonk1(a1, a2)
    print(f"Relative Primes: {b3}\nphi(b1): {b2}\nn: {b1}\nd: {b4}\ne: {b5}\b1")
    a3 = 2999
    print("Starting value:", a3)
    b6 = fonk3(b5, b1, a3)
    print("Encrypted:", b6)
    b7 = fonk4(b4, b1, b6)
    print("Decrypted:", b7)
if b8 = = "__main__":
    fonk5()