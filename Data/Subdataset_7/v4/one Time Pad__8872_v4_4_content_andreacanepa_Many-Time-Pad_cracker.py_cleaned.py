import binascii
import argparse
b1 = ord(' ')
def fonk1():
    b2 = argparse.ArgumentParser(description="Many-time Pad Cracker")
    b2.add_argument("--filename", b3 = str,
                        b4 = "Name of the file containing the b7 (b5: b7.txt)",
                        b5 = "b7.txt")
    b6 = b2.parse_args()
    try:
        with open(b6.filename) as f:
            b7 = [binascii.unhexlify(line.rstrip()) for line in f]
        b8 = [bytearray(b'?' * len(c)) for c in b7]
    except Exception as e:
        print("Cannot crack {} --- {}".format(b6.filename, e))
        raise SystemExit(-1)
    for k in range(max(len(c) for c in b7)):
        b9 = [c for c in b7 if len(c) > k]
    b10 = list()
    a1 = 0
    for line_of_ciphertexts in b7:
        if (len(line_of_ciphertexts) > a1):
            a1 = len(line_of_ciphertexts)
        b11 = list()
        for c in line_of_ciphertexts:
            b11.append(c)
        b10.append(b11)
    b12 = range(0,a1)
    b13 = list()
    for step in b12:
        b13.insert(step,list())
    for line in b10:
        for index, item in enumerate(line,0):
            b14 = b13.pop(index)
            b14.append(item)
            b13.insert(index,b14)
    b15 = list()
    b16 = list()
    for column in b13:
        b17 = {}
        for i in column:
            for j in column:
                b18 = i ^ j
                if (b18 >= 65):
                    if i not in b17:
                        b17[i] = 1
                    else:
                        b17[i] = b17.get(i) + 1
                    if j not in b17:
                        b17[j] = 1
                    else:
                        b17[j] = b17.get(j) + 1
                    b19 = max(b17, key=b17.get)
        b15.append(b19)
    for space in b15:
        b16.append(space ^ 32)
    for index_row, row in enumerate(b7,0):
        for index_column, column in enumerate(row,0):
            b8[index_row][index_column] = b7[index_row][index_column] ^ b16[index_column]
    print("\n".join(c.decode('ascii') for c in b8))
if b20 = = "__main__":
    fonk1()