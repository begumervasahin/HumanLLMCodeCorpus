import binascii
import argparse
b1 = ord(' ')
def fonk1(filename):
    try:
        with open(filename) as f:
            return [binascii.unhexlify(line.rstrip()) for line in f]
    except Exception as e:
        print(f"Error reading b12 from {filename}: {e}")
        raise SystemExit(-1)
def fonk2(b12):
    b2 = [[] for _ in range(max(len(c) for c in b12))]
    for ciphertext in b12:
        for index, char in enumerate(ciphertext):
            b2[index].append(char)
    return b2
def fonk3(b2):
    b3 = []
    for column in b2:
        b4 = {}
        for char1 in column:
            for char2 in column:
                b5 = char1 ^ char2
                if b5 >= 65:
                    b4[char1] = b4.get(char1, 0) + 1
                    b4[char2] = b4.get(char2, 0) + 1
        b3.append(max(b4, b6 = b4.get))
    return b3
def fonk4(spaces):
    return [space ^ b1 for space in spaces]
def fonk5(b12, b13):
    b7 = [bytearray(b'?' * len(c)) for c in b12]
    for index_row, row in enumerate(b12):
        for index_column, column in enumerate(row):
            b7[index_row][index_column] = row[index_column] ^ b13[index_column]
    return b7
def fonk6():
    b8 = argparse.ArgumentParser(description="Many-time Pad Cracker")
    b8.add_argument("--filename", b9 = str, default="b12.txt",
                        b10 = "Name of the file containing the b12 (default: b12.txt)")
    b11 = b8.parse_args()
    b12 = fonk1(b11.filename)
    b2 = fonk2(b12)
    b3 = fonk3(b2)
    b13 = fonk4(b3)
    b7 = fonk5(b12, b13)
    for cleartext in b7:
        print(cleartext.decode('ascii'))
if b14 = = "__main__":
    fonk6()