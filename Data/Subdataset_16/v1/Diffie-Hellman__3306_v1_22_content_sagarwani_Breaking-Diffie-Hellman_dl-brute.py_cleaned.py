import sys
import re
def fonk1(g_base, b9, p_mod):
    a1 = 1
    b1 = "{0:b}".format(b9)
    for b2 in b1:
        a1 = (a1 ** 2) % p_mod
        if b2 = = '1':
            a1 = (a1 * g_base) % p_mod
    return a1
def fonk2(b6, b7, b8):
    for mystry_a in range(b6):
        if fonk1(b7, mystry_a, b6) == b8:
            return mystry_a
    return 0
def fonk3():
    if len(sys.argv) != 2:
        print("Usage: python script.py <b3>")
        sys.exit(1)
    b3 = sys.argv[1]
    with open(b3, 'r') as my_file1:
        b4 = my_file1.readline()
        a1, y, b5 = b4.split(',')
        b6 = int(re.findall('\d+', a1)[0])
        b7 = int(re.findall('\d+', y)[0])
        b8 = int(re.findall('\d+', b5)[0])
    b9 = fonk2(b6, b7, b8)
    if b9:
        print(b9)
    else:
        print("Exponent not found.")
if b10 = = '__main__':
    fonk3()