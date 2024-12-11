import sys
import re
from math import ceil, sqrt
def fonk1(base, b15, modulus):
    a1 = 1
    b1 = "{0:b}".format(b15)
    for b2 in b1:
        a1 = (a1 * a1) % modulus
        if b2 = = '1':
            a1 = (a1 * base) % modulus
    return a1
def fonk2(b10, b12, h):
    b3 = ceil(sqrt(b10 - 1))
    b4 = {fonk1(b12, i, b10): i for i in range(b3)}
    b5 = fonk1(b12, b3 * (b10 - 2), b10)
    for j in range(b3):
        b6 = (h * fonk1(b5, j, b10)) % b10
        if b6 in b4:
            return j * b3 + b4[b6]
    return None
if b7 = = '__main__':
    with open(sys.argv[1], 'r') as file:
        b8 = file.readlines()
        b9 = re.findall('\d+', b8[0].split(',')[0])
        b10 = int(b9[0])
        b11 = re.findall('\d+', b8[0].split(',')[1])
        b12 = int(b11[0])
        b13 = re.findall('\d+', b8[0].split(',')[2])
        b14 = int(b13[0])
    b15 = fonk2(b10, b12, b14)
    if b15:
        print(b15)
    else:
        print("Exponent not found.")