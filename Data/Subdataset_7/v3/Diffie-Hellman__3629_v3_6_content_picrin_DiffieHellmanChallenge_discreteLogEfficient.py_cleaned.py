import sys
import random
def fonk1(filename):
    with open(filename, "r") as file:
        return int(file.readline().strip())
def fonk2(b13):
    return random.randint(0, b13)
def fonk3(b12, b13):
    left, b1 = b12, b13
    b2 = {left: [1, 0], b1: [0, 1]}
    b9, b3 = -1, -1
    current_left, b4 = left, b1
    while b3 != 0:
        b3 = current_left % b4
        b5 = current_left
        reconstruct_left, b6 = b2[current_left], b2[b4]
        b7 = b5 * b6[0]
        b8 = b5 * b6[1]
        b2[b3] = [reconstruct_left[0] - b7, reconstruct_left[1] - b8]
        current_left, b4 = b4, b3
        if b3 = = 0:
            b9 = b4
    b10 = (b2[b9][1] + b12) % b12
    return b10
def fonk4():
    if len(sys.argv) != 3:
        print("Usage: python script.py b11 value_of_a")
        return
    b11 = sys.argv[1]
    b12 = int(sys.argv[2])
    b13 = fonk1(b11)
    b14 = fonk2(b13)
    b10 = fonk3(b12, b13)
    print("Prime (b13):", b13)
    print("Random Number (b14):", b14)
    print("Multiplicative Inverse (b12^-1 mod b13):", b10)
if b15 = = "__main__":
    fonk4()