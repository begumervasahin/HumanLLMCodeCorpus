import os
import sys
import string
import random
import math
LETTERS = string.ascii_uppercase
def generate_otp(num_chars):
    just = int(math.log10(num_chars)) + 1
    pad = []
    for i in range(num_chars):
        n = ord(os.urandom(1)) % len(LETTERS)
        c = LETTERS[n]
        v = f"{str(i).rjust(just)} {str(ord(c) - ord('A')).rjust(2)}"
        pad.append(v)
    cols = 4
    rows = math.ceil(len(pad) / cols)
    for r in range(rows):
        for c in range(cols):
            p = c * rows + r
            if p < len(pad):
                print(pad[p], end=' ')
            if c < cols - 1:
                print(' ', end=' ')
        print()
def main():
    if len(sys.argv) <= 1:
        print(f"Usage: python {sys.argv[0]} [chars required] > otp.txt")
        sys.exit(-1)
    num_chars = int(sys.argv[1])
    generate_otp(num_chars)
if __name__ == "__main__":
    main()