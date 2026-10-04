
import sys
import os
import operator
from collections import defaultdict
b1 = "result.txt"
b2 = "comprimido.dat"
b3 = "codigos.txt"
def fonk1(b23):
    b4 = fonk2(b1)
    b5 = fonk3(b4)
    fonk5(b5, b3)
    with open(b23, 'r') as txt, open(b2, 'wb') as output:
        b6 = txt.read().rstrip().lower()
        b7 = fonk6(b5, b6)
        b8 = fonk7(b7)
        b9 = fonk8(b8)
        output.write(bytes(b9))
def fonk2(filename):
    b4 = {}
    with open(filename, 'r') as file:
        for line in file:
            symbol, b10 = line.split("\t")
            if symbol not in {"space", "salto"}:
                b4[symbol] = float(b10.strip())
    return b4
def fonk3(b4):
    if len(b4) == 2:
        return dict(zip(b4.keys(), ['0', '1']))
    b11 = b4.copy()
    sym1, b12 = fonk4(b11)
    b13 = b11.pop(sym1) + b11.pop(b12)
    b11[sym1 + b12] = b13
    b14 = fonk3(b11)
    b15 = b14.pop(sym1 + b12)
    b14[sym1] = b15 + '0'
    b14[b12] = b15 + '1'
    return b14
def fonk4(b4):
    b16 = sorted(b4.items(), key=operator.itemgetter(1))
    return b16[0][0], b16[1][0]
def fonk5(b14, filename):
    with open(filename, 'w') as file:
        for symbol, code in b14.items():
            b17 = "salto" if symbol == '\n' else symbol
            file.write(f"{b17}\t{code}\n")
def fonk6(b14, b6):
    return ''.join(b14.get(char, '') for char in b6)
def fonk7(b7):
    b18 = 8 - len(b7) % 8
    b8 = b7 + '0' * b18
    b19 = f"{b18:08b}"
    return b19 + b8
def fonk8(binary_string):
    if len(binary_string) % 8 != 0:
        raise ValueError("Binary string length must be a multiple of 8")
    return bytearray(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))
def fonk9(original_file, compressed_file):
    b20 = os.path.getsize(original_file) / (1024 * 1024.0)
    b21 = os.path.getsize(compressed_file) / (1024 * 1024.0)
    b22 = (b21 / b20) * 100
    print(f"\n\n------------ Compression Results ------------\n")
    print(f"Original Text: {original_file} | Size: {b20:.2f} MB")
    print(f"Compressed File: {compressed_file} | Size: {b21:.2f} MB")
    print(f"Compression Ratio: {round(b22)}%")
    print("Text file compressed successfully!\n\n")
def fonk10():
    if len(sys.argv) < 3 or sys.argv[1] != '-f':
        print("Usage: python generardor_huffman_code.py -f <FILE_TO_COMPRESS>")
        sys.exit(1)
    b23 = sys.argv[2]
    fonk1(b23)
    fonk9(b23, b2)
if b24 = = "__main__":
    fonk10()