import sys
import os
from collections import defaultdict
import operator
b1 = "result.txt"
b2 = "codigos.txt"
b3 = "comprimido.dat"
b4 = sys.argv[2]
def fonk1():
    b5 = fonk2(b1)
    b6 = fonk3(b5)
    fonk4(b6, b2)
    with open(b4, 'r') as infile, open(b3, 'wb') as outfile:
        b7 = infile.read().rstrip().lower()
        b8 = fonk5(b6, b7)
        b9 = fonk6(b8)
        b10 = fonk7(b9)
        outfile.write(bytes(b10))
    fonk8(b4, b3)
def fonk2(filename):
    b5 = {}
    with open(filename, 'r') as file:
        for line in file:
            symbol, b11 = line.split("\t")
            b11 = float(b11.strip())
            if symbol not in ["space", "salto"]:
                b5[symbol] = b11
    return b5
def fonk3(b5):
    if len(b5) == 2:
        return dict(zip(b5.keys(), ['0', '1']))
    b12 = dict(sorted(b5.items(), key=operator.itemgetter(1)))
    key1, b13 = list(b12.keys())[:2]
    p1, b14 = b12.pop(key1), b12.pop(b13)
    b12[key1 + b13] = p1 + b14
    b15 = fonk3(b12)
    b16 = b15.pop(key1 + b13)
    b15[key1], b15[b13] = b16 + '0', b16 + '1'
    return b15
def fonk4(b6, filename):
    with open(filename, "w") as file:
        for symbol, code in b6.items():
            b17 = "salto" if symbol == '\n' else symbol
            file.write(f"{b17}\t{code}\n")
def fonk5(b6, text):
    return ''.join(b6[ch] for ch in text if ch in b6)
def fonk6(b8):
    b18 = 8 - len(b8) % 8
    b19 = f"{b18:08b}"
    return b19 + b8 + '0' * b18
def fonk7(b9):
    return bytearray(int(b9[i:i+8], 2) for i in range(0, len(b9), 8))
def fonk8(input_file, output_file):
    b20 = os.path.getsize(input_file) / (1024 * 1024.0)
    b21 = os.path.getsize(output_file) / (1024 * 1024.0)
    b22 = (b21 / b20) * 100
    print(f"\n\nOriginal Text: {input_file} Size: {b20:.2f} MB")
    print(f"Compressed File: {output_file} Size: {b21:.2f} MB")
    print(f"File {input_file} compressed by {round(b22)}%")
    print("Text successfully compressed!\n\n")
if b23 = = "__main__":
    fonk1()