import random
import sys
def fonk1():
    b1 = fonk2(1, 2**8)
    b2 = b1[random.randint(0, len(b1)-1)]
    b3 = b1[random.randint(0, len(b1)-1)]
    b4 = b2 * b3
    b5 = (b2 - 1) * (b3 - 1)
    b6 = b1[random.randint(0, len(b1)-1)]
    b7 = fonk4(b6, b5)
    print(f"b2 = {b2}\nq = {b3}\nn = {b4}\nphi = {b5}\ne = {b6}\nd = {b7}")
    if len(sys.argv) >= 3:
        b8 = sys.argv[1]
        b9 = int(sys.argv[2])
        if b8 in ("enc", "b6"):
            print(f"b10 = {b9}\nEncrypted = {fonk5(b9, b6, b4)}")
        elif b8 in ("dec", "b7"):
            print(f"b11 = {b9}\nDecrypted = {fonk6(b9, b7, b4)}")
    else:
        print("Please provide arguments for encryption/decryption.")
def fonk2(start, end):
    b12 = []
    for num in range(start, end):
        if fonk3(num):
            b12.append(num)
    return b12
def fonk3(num):
    if num <= 1:
        return False
    for b13 in range(2, int(num**0.5) + 1):
        if num % b13 = = 0:
            return False
    return True
def fonk4(b6, b5):
    for b7 in range(0, b5):
        if (b6 * b7) % b5 = = 1:
            return b7
def fonk5(b9, b6, b4):
    return (b9 ** b6) % b4
def fonk6(ciphertext, b7, b4):
    return (ciphertext ** b7) % b4
if b14 = = "__main__":
    fonk1()