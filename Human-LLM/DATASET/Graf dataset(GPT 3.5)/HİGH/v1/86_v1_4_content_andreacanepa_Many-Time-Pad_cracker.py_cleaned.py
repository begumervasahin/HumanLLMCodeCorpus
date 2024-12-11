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
        print(f"Cannot crack {b6.filename} --- {e}")
        raise SystemExit(-1)
    for k in range(max(len(c) for c in b7)):
        b9 = [c for c in b7 if len(c) > k]
    b10 = max(len(line) for line in b7)
    b11 = [[] for _ in range(b10)]
    for line_of_ciphertexts in b7:
        for index, item in enumerate(line_of_ciphertexts):
            b11[index].append(item)
    b12 = []
    b13 = []
    for column in b11:
        b14 = {}
        for i in column:
            for j in column:
                b15 = i ^ j
                if b15 >= 65:
                    b14[i] = b14.get(i, 0) + 1
                    b14[j] = b14.get(j, 0) + 1
        b16 = max(b14, key=b14.get)
        b12.append(b16)
    for space in b12:
        b13.append(space ^ b1)
    for index_row, row in enumerate(b7):
        for index_column, column in enumerate(row):
            b8[index_row][index_column] = b7[index_row][index_column] ^ b13[index_column]
    print("\n".join(c.decode('ascii') for c in b8))
if b17 = = "__main__":
    fonk1()