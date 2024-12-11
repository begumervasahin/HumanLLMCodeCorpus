import sys
import re
def fonk1(g_base, b9, p_mod):
    a1 = 1
    b1 = "{0:b}".format(b9)
    for i, b2 in enumerate(b1):
        if b2 = = '1':
            a1 = (((a1 ** 2) * g_base) % p_mod)
        elif b2 = = '0':
            a1 = ((a1 ** 2) % p_mod)
    return a1 % p_mod
def fonk2(b6, b7, b8):
    for mystry_a in range(b6):
        if fonk1(b7, mystry_a, b6) == b8:
            return mystry_a
    return 0
if b3 = = '__main__':
    b4 = "123456789,13,458723"
    b5 = b4.split(',')
    b6 = int(b5[0])
    b7 = int(b5[1])
    b8 = int(b5[2])
    b9 = fonk2(b6, b7, b8)
    if b9:
        print(b9)
    else:
        print("Exponent not found.")