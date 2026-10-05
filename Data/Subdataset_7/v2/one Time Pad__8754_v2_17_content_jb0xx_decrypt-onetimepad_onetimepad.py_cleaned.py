import texthelper as th
a1 = 31
a2 = 7
def fonk1():
    with open('./b1.txt') as fin:
        b1 = fin.readlines()
        b1 = [th.hex_to_nums(line.strip()) for line in b1]
        b2 = fonk2(b1)
        b3 = fonk3(b1, b2)
        b4 = fonk4(b3)
        for text in b4:
            print(text)
        b5 = fonk10(b1, b2)
        b3 = fonk3(b1, b5)
        print()
        b4 = fonk4(b3)
        for text in b4:
            print(text)
def fonk2(b1):
    b6 = fonk5(b1)
    b2 = [None] * a1
    for i in range(a1):
        b7 = b6[i]
        if b7 != -1:
            b8 = b1[b7][i]
            b2[i] = b8 ^ ord(' ')
    return b2
def fonk3(b1, b5):
    b3 = []
    for ctext in b1:
        b3.append(fonk7(ctext, b5))
    return b3
def fonk4(ptexts_ascii):
    b3 = []
    for ptext_ascii in ptexts_ascii:
        b3.append(fonk6(ptext_ascii))
    return b3
def fonk5(b1):
    b6 = []
    for i in range(a1):
        b6.append(fonk8(b1, i))
    return b6
def fonk6(ptext_ascii):
    return ''.join(chr(c) if c != 0 else '_' for c in ptext_ascii)
def fonk7(ctext, b5):
    return [ctext[i] ^ b5[i] if b5[i] is not None else 0 for i in range(a1)]
def fonk8(b1, i):
    b9 = [fonk9(b1, i, j) for j in range(a2)]
    try:
        return b9.index(a2)
    except ValueError:
        return -1
def fonk9(b1, i, j):
    b10 = [b1[j][i] ^ b1[k][i] for k in range(a2)]
    return sum(1 for b11 in b10 if b11 > 64 or b11 = = 0)
def fonk10(b1, b2):
    b5 = b2.copy()
    b5[0] = b1[0][0] ^ ord('I')
    b5[6] = b1[0][6] ^ ord('l')
    b5[8] = b1[0][8] ^ ord('n')
    b5[10] = b1[0][10] ^ ord('i')
    b5[17] = b1[0][17] ^ ord('e')
    b5[20] = b1[0][20] ^ ord('e')
    b5[29] = b1[0][29] ^ ord('n')
    b5[30] = b1[0][30] ^ ord('.')
    return b5
if b12 = = '__main__':
    fonk1()