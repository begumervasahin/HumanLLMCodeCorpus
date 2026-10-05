import random
import math
def fonk1(a, b1):
    while b1 > 0:
        a, b1 = b1, a % b1
    return a
def fonk2(b3):
    while b3 % 12 != 11:
        b3 += 1
    return fonk3(b3)
def fonk3(b3):
    b2 = 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31
    while True:
        while fonk1(b3, b2) != 1 or fonk1((b3 - 1)
            b3 += 12
        if pow(7, b3 - 1, b3) != 1:
            b3 += 12
            continue
        if pow(7, (b3 - 3)
            b3 += 12
            continue
        return b3
b3 = 2 * (1416461893 + 10 ** 500) + 1
b3 = fonk2(b3)
a1 = 3
print("Check b3 prime:", pow(11, b3 - 1, b3) == 1)
b4 = (b3 - 1)
print("Check (b3-1)/2 prime:", pow(11, b4 - 1, b4) == 1)
print("\nGenerated Prime b3:", b3)
b5 = random.randint(1, b3 - 1)
b6 = random.randint(1, b3 - 1)
b7 = pow(a1, b5, b3)
b8 = pow(a1, b6, b3)
print("Public key sent from Alice to Bob:", b7)
print("Public key sent from Bob to Alice:", b8)
b9 = pow(b8, b5, b3)
b10 = pow(b7, b6, b3)
print("Are the keys equal? We check it:", b9 = = b10)