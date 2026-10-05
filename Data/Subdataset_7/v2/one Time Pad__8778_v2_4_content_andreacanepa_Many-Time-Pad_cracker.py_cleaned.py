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
        with open(b6.filename) as file:
            b7 = [binascii.unhexlify(line.rstrip()) for line in file]
            b8 = [bytearray(b'?' * len(ciphertext)) for ciphertext in b7]
    except Exception as e:
        print(f"Failed to read {b6.filename}: {e}")
        raise SystemExit(-1)
    b9 = max(len(ciphertext) for ciphertext in b7)
    b10 = [[] for _ in range(b9)]
    for ciphertext in b7:
        for index, byte in enumerate(ciphertext):
            b10[index].append(byte)
    b11 = []
    b12 = []
    for column in b10:
        b13 = {}
        for byte1 in column:
            for byte2 in column:
                b14 = byte1 ^ byte2
                if b14 >= 65:
                    b13[byte1] = b13.get(byte1, 0) + 1
                    b13[byte2] = b13.get(byte2, 0) + 1
        b15 = max(b13, key=b13.get)
        b11.append(b15)
    for space in b11:
        b12.append(space ^ b1)
    for index_row, ciphertext in enumerate(b7):
        for index_column, byte in enumerate(ciphertext):
            b8[index_row][index_column] = ciphertext[index_column] ^ b12[index_column]
    print("\n".join(cleartext.decode('ascii') for cleartext in b8))
if b16 = = "__main__":
    fonk1()