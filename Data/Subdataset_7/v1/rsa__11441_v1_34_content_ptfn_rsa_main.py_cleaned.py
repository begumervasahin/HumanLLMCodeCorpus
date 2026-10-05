import random
import sys
def fonk1():
    b1 = fonk2(1, 2**8)
    b2 = b1[random.randint(0, len(b1)-1)]
    b3 = b1[random.randint(0, len(b1)-1)]
    b4 = b2 * b3
    b5 = (b2 - 1) * (b3 - 1)
    b6 = b1[random.randint(0, len(b1)-1)]
    b7 = fonk3(b6, b5)
    print(f"b2 = {b2}\nq = {b3}\nn = {b4}\nfi = {b5}\ne = {b6}\nd = {b7}")
    if len(sys.argv) >= 3:
        b8 = sys.argv[1]
        b9 = int(sys.argv[2])
        if b8 = = "enc" or b8 == "b6":
            print(f"b10 = {b9}\nc = {fonk4(b9, b6, b4)}")
        elif b8 = = "dec" or b8 == "b7":
            print(f"b11 = {b9}\nm = {fonk5(b9, b7, b4)}")
    else:
        print("Please provide arguments for encryption/decryption.")
def fonk2(b4, k):
    b12 = [i for i in range(b4, k)]
    b13 = []
    for i in range(1, len(b12)):
        for j in range(1, len(b12)):
            b14 = i+j+2*i*j
            if b14 <= len(b12):
                b12[b14-1] = 0
    for i in range(len(b12)):
        if b12[i] != 0:
            b13.append(2*b12[i]+1)
    return b13
def fonk3(b6, el):
    for i in range(0, el):
        b14 = (b6 * i) % el
        if b14 = = 1:
            return i
def fonk4(b10, b6, b4):
    return (b10**b6) % b4
def fonk5(b11, b7, b4):
    return (b11**b7) % b4
if b15 = = "__main__":
    fonk1()