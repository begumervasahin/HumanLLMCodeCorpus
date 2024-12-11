from decimal import Decimal
import sys
import os
import operator
b1 = "result.txt"
b2 = "compressed.dat"
b3 = "b10.txt"
def fonk1():
    b4 = fonk2()
    b5 = fonk3(b4)
    fonk4(b5)
    fonk5(b5)
def fonk2():
    b4 = {}
    with open(b1, 'r') as file:
        for line in file:
            key, b6 = line.strip().split("\t")
            if key not in ["space", "salto"]:
                b4[key] = float(b6)
    return b4
def fonk3(b4):
    if len(b4) == 2:
        return dict(zip(b4.keys(), ['0', '1']))
    b7 = sorted(b4.items(), key=operator.itemgetter(1))
    key1, b8 = b7[0][0], b7[1][0]
    prob1, b9 = b4.pop(key1), b4.pop(b8)
    b4[key1 + b8] = prob1 + b9
    b10 = fonk3(b4)
    b11 = b10.pop(key1 + b8)
    b10[key1], b10[b8] = b11 + '0', b11 + '1'
    return b10
def fonk4(b10):
    with open(b3, "w") as file:
        for key, b6 in b10.items():
            b12 = "salto" if key == '\n' else key
            file.write(f"{b6}\t{b12}\n")
def fonk5(b10):
    with open(sys.argv[2], 'r') as text_file, open(b2, 'wb') as output:
        b13 = text_file.read().rstrip().lower()
        b14 = fonk6(b10, b13)
        b15 = fonk7(b14)
        b16 = fonk8(b15)
        output.write(b16)
def fonk6(b10, b13):
    return ''.join(b10[char] for char in b13.split() if char in b10)
def fonk7(b14):
    b17 = 8 - len(b14) % 8
    return f"{b17:08b}" + b14 + "0" * b17
def fonk8(binary_string):
    if len(binary_string) % 8 != 0:
        sys.exit(0)
    return bytearray(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))
if b18 = = "__main__":
    fonk1()
    fonk9(sys.argv[2])
def fonk9(input_file):
    b19 = os.path.getsize(input_file) / (1024 * 1024.0)
    b20 = os.path.getsize(b2) / (1024 * 1024.0)
    b21 = (b20 / b19) * 100
    print("\nOriginal Text: {} Size: {:.2f} MB".format(input_file, b19))
    print("Compressed File: {} Size: {:.2f} MB".format(b2, b20))
    print("File {} compressed by {:.2f}%".format(input_file, b21))
    print("Text file compressed successfully!\n")