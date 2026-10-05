import texthelper as th
a1 = 31
a2 = 7
def fonk1():
    b1 = fonk2('./b1.txt')
    b2 = fonk3(b1)
    fonk4(b1, b2, "Predicted Key:")
    b3 = fonk9(b1, b2)
    fonk4(b1, b3, "\nAdjusted Key:")
def fonk2(file_path):
    with open(file_path) as fin:
        return [th.hex_to_nums(line.strip()) for line in fin.readlines()]
def fonk3(b1):
    b4 = [fonk7(b1, i) for i in range(a1)]
    b2 = [None if id_msg == -1 else b1[id_msg][i] ^ ord(' ') for i, id_msg in enumerate(b4)]
    return b2
def fonk4(b1, b3, label):
    b5 = [fonk5(fonk6(ctext, b3)) for ctext in b1]
    print(label)
    for text in b5:
        print(text)
def fonk5(ptext_ascii):
    return ''.join(chr(c) if c != 0 else '_' for c in ptext_ascii)
def fonk6(ctext, b3):
    return [ctext[i] ^ b3[i] if b3[i] is not None else 0 for i in range(a1)]
def fonk7(b1, i):
    b6 = [fonk8(b1, i, j) for j in range(a2)]
    return b6.index(a2) if a2 in b6 else -1
def fonk8(b1, i, j):
    b7 = [b1[j][i] ^ b1[k][i] for k in range(a2)]
    return sum(1 for b8 in b7 if b8 > 64 or b8 = = 0)
def fonk9(b1, b2):
    b3 = b2.copy()
    b3[0] = b1[0][0] ^ ord('I')
    b3[6] = b1[0][6] ^ ord('l')
    b3[8] = b1[0][8] ^ ord('n')
    b3[10] = b1[0][10] ^ ord('i')
    b3[17] = b1[0][17] ^ ord('e')
    b3[20] = b1[0][20] ^ ord('e')
    b3[29] = b1[0][29] ^ ord('n')
    b3[30] = b1[0][30] ^ ord('.')
    return b3
if b9 = = '__main__':
    fonk1()