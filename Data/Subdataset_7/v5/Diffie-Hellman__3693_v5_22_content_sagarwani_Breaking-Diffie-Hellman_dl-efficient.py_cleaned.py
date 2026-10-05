import sys
import re
from math import ceil, sqrt
def fonk1(base, b12, modulus):
    a1 = 1
    b1 = "{0:b}".format(b12)
    for b2 in b1:
        a1 = (a1 * a1) % modulus
        if b2 = = '1':
            a1 = (a1 * base) % modulus
    return a1
def fonk2(b9, b10, h):
    b3 = ceil(sqrt(b9 - 1))
    b4 = {fonk1(b10, i, b9): i for i in range(b3)}
    b5 = fonk1(b10, b3 * (b9 - 2), b9)
    for j in range(b3):
        b6 = (h * fonk1(b5, j, b9)) % b9
        if b6 in b4:
            return j * b3 + b4[b6]
    return None
if b7 = = '__main__':
    with open(sys.argv[1], 'r') as file:
        b8 = file.readlines()
        b9 = int(re.findall('\d+', b8[0].split(',')[0])[0])
        b10 = int(re.findall('\d+', b8[0].split(',')[1])[0])
        b11 = int(re.findall('\d+', b8[0].split(',')[2])[0])
    b12 = fonk2(b9, b10, b11)
    if b12:
        print(b12)
    else:
        print("Exponent not found.")