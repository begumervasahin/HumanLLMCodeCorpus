import sys
import random
def fonk1(filename):
    with open(filename, "r") as f:
        b1 = int(f.readline().strip())
    return b1
def fonk2(b15, b):
    b2 = {b15: [1, 0], b: [0, 1]}
    b3 = b15
    b4 = b
    a1 = -1
    while a1 != 0:
        a1 = b3 % b4
        b5 = b3
        b6 = b2[b3]
        b7 = b2[b4]
        b8 = b5 * b7[0]
        b9 = b5 * b7[1]
        b2[a1] = [b6[0] - b8, b6[1] - b9]
        b3 = b4
        b4 = a1
    b10 = b3
    x, b11 = b2[b10]
    return b10, x, b11
def fonk3(b15, b1):
    b12 = random.randint(1, b1-1)
    b10, x, b13 = fonk2(b1, b12)
    if b10 != 1:
        raise ValueError("No multiplicative b16 exists for the given inputs.")
    return (x + b1) % b1
def fonk4():
    if len(sys.argv) != 3:
        print("Usage: python script.py <b14> <b15>")
        sys.exit(1)
    b14 = sys.argv[1]
    b15 = int(sys.argv[2])
    b1 = fonk1(b14)
    b16 = fonk3(b15, b1)
    print(f"The multiplicative b16 of {b15} modulo {b1} is {b16}")
if b17 = = '__main__':
    fonk4()