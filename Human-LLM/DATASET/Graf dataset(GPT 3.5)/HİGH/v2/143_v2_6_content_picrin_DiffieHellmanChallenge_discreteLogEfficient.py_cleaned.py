import sys
import random
def fonk1(filename):
    with open(filename, "r") as f:
        return int(f.readline().strip())
def fonk2(b14):
    return random.randint(0, b14)
def fonk3(b13, b):
    b1 = b13
    b2 = b
    a1 = -1
    a2 = -1
    b3 = {b1: [1, 0], b2: [0, 1]}
    b4 = b1
    b5 = b2
    while a1 != 0:
        a1 = b4 % b5
        b6 = b4
        b7 = b3[b4]
        b8 = b3[b5]
        b9 = b6 * b8[0]
        b10 = b6 * b8[1]
        b3[a1] = [b7[0] - b9, b7[1] - b10]
        b4 = b5
        if a1 = = 0:
            a2 = b5
        b5 = a1
    b11 = (b3[a2][1] + b13) % b13
    return b11
def fonk4():
    if len(sys.argv) < 3:
        print("Usage: python script.py b12 value_of_a")
        return
    b12 = sys.argv[1]
    b13 = int(sys.argv[2])
    b14 = fonk1(b12)
    b15 = fonk2(b14)
    b11 = fonk3(b13, b14)
    print("Multiplicative Inverse:", b11)
if b16 = = "__main__":
    fonk4()