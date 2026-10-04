import sys, re
def fonk1(g_base,b11,p_mod):
  a1 = 1
  b1 = "{0:b}".format(b11)
  for i, b2 in enumerate(b1):
    if b2 = ='1':
        a1 = (((a1**2)*g_base)%p_mod)
    elif b2 = ='0':
        a1 = ((a1**2)%p_mod)
  return a1%p_mod
def fonk2(b6, b8, b10):
    for mystry_a in range(b6):
        if fonk1(b8, mystry_a, b6) == b10:
            return mystry_a
    return 0
if b3 = = '__main__':
    with open(sys.argv[1], 'r') as my_file1:
        b4 = my_file1.readlines()
        a1 = b4[0].split(',')[0]
        b5 = re.findall('\d+', a1)
        b6 = int(b5[0])
        b7 = b4[0].split(',')[1]
        b5 = re.findall('\d+', b7)
        b8 = int(b5[0])
        b9 = b4[0].split(',')[2]
        b5 = re.findall('\d+', b9)
        b10 = int(b5[0])
    b11 = fonk2(b6, b8, b10)
    if b11:
        print(b11)
    else:
        print("Exponent not found.")