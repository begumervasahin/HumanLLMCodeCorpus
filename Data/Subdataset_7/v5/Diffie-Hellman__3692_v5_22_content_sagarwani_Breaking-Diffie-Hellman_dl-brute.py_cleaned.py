import sys
import re
def fonk1(base, b9, modulus):
    a1 = 1
    b1 = "{0:b}".format(b9)
    for b2 in b1:
        a1 = (a1 * a1) % modulus
        if b2 = = '1':
            a1 = (a1 * base) % modulus
    return a1
def fonk2(prime_modulus, base, a1):
    for potential_exponent in range(prime_modulus):
        if fonk1(base, potential_exponent, prime_modulus) == a1:
            return potential_exponent
    return 0
if b3 = = '__main__':
    b4 = sys.argv[1]
    with open(b4, 'r') as input_file:
        b5 = input_file.readline().strip().split(',')
        b6 = int(re.findall('\d+', b5[0])[0])
        b7 = int(re.findall('\d+', b5[1])[0])
        b8 = int(re.findall('\d+', b5[2])[0])
    b9 = fonk2(b6, b7, b8)
    if b9:
        print("Found b9:", b9)
    else:
        print("Exponent not found.")