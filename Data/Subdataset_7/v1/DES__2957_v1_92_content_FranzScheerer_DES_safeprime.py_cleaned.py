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
print("Check b3:", pow(11, b3 - 1, b3) == 1)
b4 = (b3 - 1)
print("Check (b3-1)/2:", pow(11, b4 - 1, b4) == 1)
print("\nPrime b3:", b3)
a2 = 2134143854854758971
a3 = 2994143854854754312412
b5 = pow(a1, a2, b3)
b6 = pow(a1, a3, b3)
print("Public key sent from Alice to Bob:", b5)
print("Public key sent from Bob to Alice:", b6)
b7 = pow(b6, a2, b3)
b8 = pow(b5, a3, b3)
print("Are the keys equal? We check it:", b7 = = b8)