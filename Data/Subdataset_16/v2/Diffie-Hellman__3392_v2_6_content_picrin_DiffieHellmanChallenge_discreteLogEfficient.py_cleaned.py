import sys
import random
def fonk1(filename):
    with open(filename, "r") as f:
        b1 = int(f.readline().strip())
    return b1
def fonk2(b13, b):
    b2 = {b13: [1, 0], b: [0, 1]}
    current_left, b3 = b13, b
    a1 = -1
    while a1 != 0:
        a1 = current_left % b3
        b4 = current_left
        b5 = b2[current_left]
        b6 = b2[b3]
        b7 = b4 * b6[0]
        b8 = b4 * b6[1]
        b2[a1] = [b5[0] - b7, b5[1] - b8]
        current_left, b3 = b3, a1
    b9 = current_left
    x, b10 = b2[b9]
    return b9, x, b10
def fonk3(b13, b14):
    b9, x, b11 = fonk2(b14, b13)
    if b9 != 1:
        raise ValueError("No multiplicative b15 exists for the given inputs.")
    return (x + b14) % b14
def fonk4():
    if len(sys.argv) != 3:
        print("Usage: python script.py <b12> <b13>")
        sys.exit(1)
    b12 = sys.argv[1]
    b13 = int(sys.argv[2])
    b14 = fonk1(b12)
    b15 = fonk3(b13, b14)
    print(f"The multiplicative b15 of {b13} modulo {b14} is {b15}")
if b16 = = '__main__':
    fonk4()