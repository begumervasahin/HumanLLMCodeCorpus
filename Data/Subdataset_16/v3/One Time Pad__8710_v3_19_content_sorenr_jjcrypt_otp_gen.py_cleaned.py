import os
import sys
import string
import random
import math
b1 = string.ascii_uppercase
def fonk1(b10):
    b2 = int(math.log10(b10)) + 1
    b3 = []
    for i in range(b10):
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
            if b5 < a1 - 1:
                print(' ', b9 = ' ')
        print()
def fonk2():
    if len(sys.argv) <= 1:
        print(f"Usage: python {sys.argv[0]} [chars required] > otp.txt")
        sys.exit(-1)
    b10 = int(sys.argv[1])
    fonk1(b10)
if b11 = = "__main__":
    fonk2()