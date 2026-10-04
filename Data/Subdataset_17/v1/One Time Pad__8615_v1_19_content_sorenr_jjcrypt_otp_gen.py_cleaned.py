import os
import sys
import string
import random
import math
letters = string.ascii_uppercase
def otp_gen(numbers):
    just = int(math.log(numbers) / math.log(10)) + 1
    pad = []
    for i in range(numbers):
        n = ord(os.urandom(1)) % len(letters)
        c = letters[n]
        v = ' '.join([str(i).rjust(just), str(ord(c) - ord('A')).rjust(2)])
        pad.append(v)
    cols = 4
    rows = int(math.ceil(len(pad) / float(cols)))
    for r in range(rows):
        for c in range(cols):
            p = c * rows + r
            if p < len(pad):
                print(pad[p], end=' ')
            if c < cols - 1:
                print(' ', end=' ')
        print()
if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python", sys.argv[0], "[chars required] > otp.txt")
        sys.exit(-1)
    otp_gen(int(sys.argv[1]))