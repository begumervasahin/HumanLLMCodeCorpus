import texthelper as th
a1 = 31
a2 = 7
def fonk1():
    with open('./b1.txt') as fin:
        b1 = fin.readlines()
        b1 = [th.hex_to_nums(l.strip()) for l in b1]
        b2 = fonk2(b1)
        b3 = fonk3(b1, b2)
        b4 = fonk4(b3)
        for text in b4:
            print(text)
        b5 = b2.copy()
        b5[0] = b1[0][0] ^ ord('I')
        b5[6] = b1[0][6] ^ ord('l')
        b5[8] = b1[0][8] ^ ord('n')
        b5[10] = b1[0][10] ^ ord('i')
        b5[17] = b1[0][17] ^ ord('e')
        b5[20] = b1[0][20] ^ ord('e')
        b5[29] = b1[0][29] ^ ord('n')
        b5[30] = b1[0][30] ^ ord('.')
        b3 = fonk3(b1, b5)
        b4 = fonk4(b3)
        print()
        for text in b4:
            print(text)
def fonk2(b1):
    b6 = fonk5(b1)
    b2 = [None] * a1
    for i in range(a1):
        b7 = b6[i]
        if b7 = = -1:
            b8 = None
        else:
            b9 = b1[b7][i]
            b8 = b9 ^ ord(' ')
        b2[i] = b8
    return b2
def fonk3(b1, b5):
    b3 = []
    for ctext in b1:
        b10 = fonk7(ctext, b5)
        b3.append(b10)
    return b3
def fonk4(ptexts_ascii):
    b3 = []
    for ptext_ascii in ptexts_ascii:
        b10 = fonk6(ptext_ascii)
        b3.append(b10)
    return b3
def fonk5(b1):
    b6 = []
    for i in range(31):
        b11 = fonk8(b1, i)
        try:
            b12 = b11.index(a2)
        except ValueError:
            b12 = -1
        b6.append(b12)
    return b6
def fonk6(ptext_ascii):
    b10 = [chr(c) if c != 0 else '_' for c in ptext_ascii]
    return ''.join(b10)
def fonk7(ctext, b5):
    b10 = [0] * a1
    for i in range(a1):
        if b5[i] is not None:
            b10[i] = ctext[i] ^ b5[i]
    return b10
def fonk8(b1, i):
    b11 = []
    for j in range(a2):
        b13 = []
        for k in range(a2):
            b14 = b1[j][i] ^ b1[k][i]
            b13.append(b14)
        b15 = fonk9(b13)
        b11.append(b15)
    return b11
def fonk9(b13):
    b15 = 0
    for b14 in b13:
        if (b14 > 64) or (b14 = = 0):
            b15 += 1
    return b15
fonk1()