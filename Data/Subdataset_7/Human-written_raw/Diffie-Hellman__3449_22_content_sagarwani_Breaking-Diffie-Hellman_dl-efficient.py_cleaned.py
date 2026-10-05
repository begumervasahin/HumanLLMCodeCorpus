import sys, re
from math import ceil, sqrt
def fonk1(g_base,b14,p_mod):
  a1 = 1
  b1 = "{0:b}".format(b14)
  for i, b2 in enumerate(b1):
    if b2 = ='1':
        a1 = (((a1**2)*g_base)%p_mod)
    elif b2 = ='0':
        a1 = ((a1**2)%p_mod)
  return a1%p_mod
def fonk2(b10, b11, h):
    b3 = ceil(sqrt(b10 - 1))
    b4 = {fonk1(b11, i, b10): i for i in range(b3)}
    b5 = fonk1(b11, b3 * (b10 - 2), b10)
    for j in range(b3):
        b6 = (h * fonk1(b5, j, b10)) % b10
        if b6 in b4:
            return j * b3 + b4[b6]
    return None
if b7 = = '__main__':
    with open(sys.argv[1], 'r') as my_file1:
        b8 = my_file1.readlines()
        a1 = b8[0].split(',')[0]
        b9 = re.findall('\d+', a1)
        b10 = int(b9[0])
        b6 = b8[0].split(',')[1]
        b9 = re.findall('\d+', b6)
        b11 = int(b9[0])
        b12 = b8[0].split(',')[2]
        b9 = re.findall('\d+', b12)
        b13 = int(b9[0])
    b14 = fonk2(b10, b11, b13)
    if b14:
        print(b14)
    else:
        print("Exponent not found.")