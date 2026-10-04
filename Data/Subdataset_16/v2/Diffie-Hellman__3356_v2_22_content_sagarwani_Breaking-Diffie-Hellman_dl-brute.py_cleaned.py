import sys
import re
def fonk1(g_base, a, p_mod):
    a1 = 1
    b1 = bin(a)[2:]
    for b2 in b1:
        a1 = (a1 ** 2) % p_mod
        if b2 = = '1':
            a1 = (a1 * g_base) % p_mod
    return a1
def fonk2(b5, b6, b7):
    for possible_a in range(b5):
        if fonk1(b6, possible_a, b5) == b7:
            return possible_a
    return 0
def fonk3(file_path):
    with open(file_path, 'r') as file:
        b3 = file.readline().strip()
        p_str, g_str, b4 = b3.split(',')
        b5 = int(re.findall(r'\d+', p_str)[0])
        b6 = int(re.findall(r'\d+', g_str)[0])
        b7 = int(re.findall(r'\d+', b4)[0])
    return b5, b6, b7
def fonk4():
    if len(sys.argv) != 2:
        print("Usage: python script.py <b8>")
        sys.exit(1)
    b8 = sys.argv[1]
    b5, b6, b7 = fonk3(b8)
    b9 = fonk2(b5, b6, b7)
    if b9:
        print(f"The secret exponent is: {b9}")
    else:
        print("Exponent not found.")
if b10 = = '__main__':
    fonk4()