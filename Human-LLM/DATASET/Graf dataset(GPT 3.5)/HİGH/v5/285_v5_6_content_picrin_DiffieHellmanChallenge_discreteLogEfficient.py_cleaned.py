import sys
import random
def fonk1(filename):
    with open(filename, "r") as file:
        return int(file.readline().strip())
def fonk2(max_value):
    return random.randint(0, max_value)
def fonk3(b11, b):
    left, b1 = b11, b
    a1 = -1
    a2 = -1
    b2 = {left: [1, 0], b1: [0, 1]}
    b8, b3 = left, b1
    while a1 != 0:
        a1 = b8 % b3
        b4 = b8
        reconstruct_left, b5 = b2[b8], b2[b3]
        b6 = b4 * b5[0]
        b7 = b4 * b5[1]
        b2[a1] = [reconstruct_left[0] - b6, reconstruct_left[1] - b7]
        b8 = b3
        if a1 = = 0:
            a2 = b3
        b3 = a1
    b9 = (b2[a2][1] + b11) % b11
    return b9
def fonk4():
    if len(sys.argv) < 3:
        print("Usage: python script.py b10 value_of_a")
        return
    b10 = sys.argv[1]
    b11 = int(sys.argv[2])
    b12 = fonk1(b10)
    b13 = fonk2(b12)
    b9 = fonk3(b11, b12)
    print("Result:", b11 * b9)
if b14 = = "__main__":
    fonk4()