import sys
import random
def fonk1(filename):
    with open(filename, "r") as f:
        b1 = int(f.readline().strip())
    return b1
def fonk2(b12, b):
    b2 = {b12: [1, 0], b: [0, 1]}
    current_left, b3 = b12, b
    while b3 != 0:
        b4 = current_left % b3
        b5 = current_left
        b6 = b2[current_left]
        b7 = b2[b3]
        b2[b4] = [
            b6[0] - b5 * b7[0],
            b6[1] - b5 * b7[1]
        ]
        current_left, b3 = b3, b4
    b8 = current_left
    x, b9 = b2[b8]
    return b8, x, b9
def fonk3(b12, b13):
    b8, x, b10 = fonk2(b13, b12)
    if b8 != 1:
        raise ValueError("No multiplicative inverse exists for the given inputs.")
    return (x + b13) % b13
def fonk4():
    if len(sys.argv) != 3:
        print("Usage: python script.py <b11> <b12>")
        sys.exit(1)
    b11 = sys.argv[1]
    b12 = int(sys.argv[2])
    b13 = fonk1(b11)
    b14 = random.randint(1, b13 - 1)
    b15 = fonk3(b14, b13)
    b16 = (b12 * b15) % b13
    print(f"The b16 of {b12} * multiplicative inverse of {b14} modulo {b13} is {b16}")
if b17 = = '__main__':
    fonk4()