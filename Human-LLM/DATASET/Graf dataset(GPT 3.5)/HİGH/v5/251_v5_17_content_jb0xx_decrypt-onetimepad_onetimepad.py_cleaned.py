import texthelper as th
a1 = 31
a2 = 7
def fonk1():
    b1 = fonk2('./b1.txt')
    b2 = fonk3(b1)
    print("Predicted plaintexts:")
    fonk9(fonk6(b1, b2))
    b3 = fonk8(b2, b1[0])
    print("\nUpdated plaintexts:")
    fonk9(fonk6(b1, b3))
def fonk2(file_path):
    with open(file_path) as fin:
        b1 = [th.hex_to_nums(l.strip()) for l in fin.readlines()]
    return b1
def fonk3(b1):
    b4 = fonk4(b1)
    b2 = [b1[b6][i] ^ ord(' ') if b6 != -1 else None for i, b6 in enumerate(b4)]
    return b2
def fonk4(b1):
    b4 = []
    for i in range(a1):
        b5 = [fonk5([ctext[i] ^ b1[k][i] for k in range(a2)]) for ctext in b1]
        b6 = b5.index(a2) if a2 in b5 else -1
        b4.append(b6)
    return b4
def fonk5(list_xors):
    return sum(1 for b7 in list_xors if b7 > 64 or b7 = = 0)
def fonk6(b1, key):
    return [fonk7(ctext, key) for ctext in b1]
def fonk7(ctext, key):
    return [ctext[i] ^ key[i] if key[i] is not None else 0 for i in range(a1)]
def fonk8(b2, ctext):
    b3 = b2.copy()
    b3[0] = ctext[0] ^ ord('I')
    b3[6] = ctext[6] ^ ord('l')
    b3[8] = ctext[8] ^ ord('n')
    b3[10] = ctext[10] ^ ord('i')
    b3[17] = ctext[17] ^ ord('e')
    b3[20] = ctext[20] ^ ord('e')
    b3[29] = ctext[29] ^ ord('n')
    b3[30] = ctext[30] ^ ord('.')
    return b3
def fonk9(ptexts_ascii):
    b8 = [fonk10(ptext_ascii) for ptext_ascii in ptexts_ascii]
    for text in b8:
        print(text)
def fonk10(ptext_ascii):
    return ''.join(chr(c) if c != 0 else '_' for c in ptext_ascii)
fonk1()