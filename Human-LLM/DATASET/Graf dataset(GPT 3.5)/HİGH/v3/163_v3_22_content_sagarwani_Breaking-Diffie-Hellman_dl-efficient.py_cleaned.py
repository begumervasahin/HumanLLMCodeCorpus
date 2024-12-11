import sys
import re
from math import ceil, sqrt
def fonk1(base, b10, modulus):
    a1 = 1
    b1 = "{0:b}".format(b10)
    for b2 in b1:
        a1 = (a1 * a1) % modulus
        if b2 = = '1':
            a1 = (a1 * base) % modulus
    return a1
def fonk2(p, g, h):
    b3 = ceil(sqrt(p - 1))
    b4 = {fonk1(g, i, p): i for i in range(b3)}
    b5 = fonk1(g, b3 * (p - 2), p)
    for j in range(b3):
        b6 = (h * fonk1(b5, j, p)) % p
        if b6 in b4:
            return j * b3 + b4[b6]
    return None
if b7 = = '__main__':
    with open(sys.argv[1], 'r') as file:
        b8 = file.readlines()
        p, g, b9 = map(int, re.findall('\d+', b8[0]))
    b10 = fonk2(p, g, b9)
    if b10:
        print(b10)
    else:
        print("Exponent not found.")