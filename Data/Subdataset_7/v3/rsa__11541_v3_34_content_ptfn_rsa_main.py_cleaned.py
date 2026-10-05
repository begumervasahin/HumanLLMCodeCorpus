import random
import sys
def fonk1():
    b1 = fonk2(1, 2**8)
    b2 = fonk2(1, 2**8)
    b3 = b1 * b2
    b4 = (b1 - 1) * (b2 - 1)
    b5 = fonk3(b4)
    b6 = fonk6(b5, b4)
    print(f"b1 = {b1}\nq = {b2}\nn = {b3}\nphi = {b4}\ne = {b5}\nd = {b6}")
    if len(sys.argv) >= 3:
        b7 = sys.argv[1]
        b8 = int(sys.argv[2])
        if b7 in ("enc", "b5"):
            print(f"b9 = {b8}\nEncrypted = {fonk8(b8, b5, b3)}")
        elif b7 in ("dec", "b6"):
            print(f"b10 = {b8}\nDecrypted = {fonk9(b8, b6, b3)}")
    else:
        print("Please provide arguments for encryption/decryption.")
def fonk2(start, end):
    while True:
        b11 = random.randint(start, end)
        if fonk4(b11):
            return b11
def fonk3(b4):
    while True:
        b5 = random.randint(2, b4 - 1)
        if fonk5(b5, b4) == 1:
            return b5
def fonk4(b11):
    if b11 <= 1:
        return False
    for b12 in range(2, int(b11**0.5) + 1):
        if b11 % b12 = = 0:
            return False
    return True
def fonk5(b14, b13):
    while b13 != 0:
        b14, b13 = b13, b14 % b13
    return b14
def fonk6(b5, b4):
    b6 = fonk7(b5, b4)[1]
    return b6 % b4
def fonk7(b14, b13):
    if b14 = = 0:
        return b13, 0, 1
    else:
        gcd, x, b15 = fonk7(b13 % b14, b14)
        return gcd, b15 - (b13
def fonk8(b8, b5, b3):
    return pow(b8, b5, b3)
def fonk9(ciphertext, b6, b3):
    return pow(ciphertext, b6, b3)
if b16 = = "__main__":
    fonk1()