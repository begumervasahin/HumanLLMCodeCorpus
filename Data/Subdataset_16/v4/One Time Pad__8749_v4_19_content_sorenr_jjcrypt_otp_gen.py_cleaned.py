import os
import sys
import string
import random
import math
b1 = string.ascii_uppercase
def fonk1(numbers):
    b2 = int(math.log10(numbers)) + 1
    b3 = []
    for i in range(numbers):
        b4 = ord(os.urandom(1)) % len(b1)
        b5 = b1[b4]
        b6 = f"{str(i).rjust(b2)} {str(ord(b5) - ord('A')).rjust(2)}"
        b3.append(b6)
    a1 = 4
    b7 = math.ceil(len(b3) / a1)
    for r in range(b7):
        for b5 in range(a1):
            b8 = b5 * b7 + r
            if b8 < len(b3):
                print(b3[b8], b9 = ' ')
        print()
if b10 = = "__main__":
    if len(sys.argv) <= 1:
        print(f"Usage: {sys.argv[0]} [chars required] > otp.txt")
        sys.exit(-1)
    try:
        b11 = int(sys.argv[1])
    except ValueError:
        print("Error: The argument must be an integer.")
        sys.exit(-1)
    fonk1(b11)