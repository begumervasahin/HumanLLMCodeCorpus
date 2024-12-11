import random
import sys
def fonk1():
    b1 = fonk2(1, 2**8)
    b2 = b1[random.randint(0, len(b1) - 1)]
    b3 = b1[random.randint(0, len(b1) - 1)]
    b4 = b2 * b3
    b5 = (b2 - 1) * (b3 - 1)
    b6 = b1[random.randint(0, len(b1) - 1)]
    b7 = fonk4(b6, b5)
    print(f"b2 = {b2}\nq = {b3}\nn = {b4}\nphi_n = {b5}\ne = {b6}\nd = {b7}")
    b8 = sys.argv[1]
    b9 = int(sys.argv[2])
    if b8 = = "enc" or b8 == "b6":
        print(f"b9 = {b9}\nciphertext = {fonk5(b9, b6, b4)}")
    elif b8 = = "dec" or b8 == "b7":
        print(f"b10 = {b9}\ndecrypted b9 = {fonk6(b9, b7, b4)}")
def fonk2(start, end):
    b1 = []
    for num in range(start, end):
        if fonk3(num):
            b1.append(num)
    return b1
def fonk3(num):
    if num <= 1:
        return False
    for b11 in range(2, int(num**0.5) + 1):
        if num % b11 = = 0:
            return False
    return True
def fonk4(b6, b5):
    for b11 in range(0, b5):
        if (b6 * b11) % b5 = = 1:
            return b11
def fonk5(b9, b6, b4):
    return (b9 ** b6) % b4
def fonk6(b10, b7, b4):
    return (b10 ** b7) % b4
if b12 = = "__main__":
    fonk1()