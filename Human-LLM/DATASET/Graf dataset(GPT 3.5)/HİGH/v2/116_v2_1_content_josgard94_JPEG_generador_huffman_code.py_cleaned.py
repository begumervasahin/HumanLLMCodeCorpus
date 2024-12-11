from decimal import Decimal
import sys
import os
import operator
b1 = "result.txt"
b2 = sys.argv[2]
b3 = "compressed.dat"
b4 = "b16.txt"
def fonk1():
    b5 = {}
    b6 = {}
    with open(b1, 'r') as file:
        for line in file:
            b7 = line.split("\t")
            if b7[0] in ["space", "salto"]:
                continue
            b5[b7[0]] = float(b7[1].rstrip())
    b6 = fonk3(b5)
    fonk4(b6)
    with open(b2, 'r') as text_file, open(b3, 'wb') as output:
        b8 = text_file.read().rstrip().lower()
        b9 = fonk5(b6, b8)
        b10 = fonk6(b9)
        b11 = fonk7(b10)
        output.write(bytes(b11))
def fonk2(dictionary):
    b12 = sorted(dictionary.items(), b18=operator.itemgetter(1), reverse=False)
    return b12[0][0], b12[1][0]
def fonk3(dictionary):
    if len(dictionary) == 2:
        return dict(zip(dictionary.keys(), ['0', '1']))
    b13 = dictionary.copy()
    key1, b14 = fonk2(dictionary)
    prob1, b15 = b13.pop(key1), b13.pop(b14)
    b13[key1 + b14] = prob1 + b15
    b16 = fonk3(b13)
    b17 = b16.pop(key1 + b14)
    b16[key1], b16[b14] = b17 + '0', b17 + '1'
    return b16
def fonk4(dictionary):
    with open(b4, "w") as file:
        for b18 in dictionary:
            if b18 = = '\n':
                file.write("salto" + "\t" + dictionary.get(b18, b18) + "\n")
            else:
                file.write(dictionary.get(0, b18) + "\t" + dictionary.get(b18, b18) + "\n")
def fonk5(b16, b8):
    b9 = ""
    for char in b8.split():
        if char in b16:
            b9 += b16[char]
    return b9
def fonk6(encoded):
    b19 = 8 - len(encoded) % 8
    for _ in range(b19):
        encoded += "0"
    b20 = "{0:08b}".format(b19)
    return b20 + encoded
def fonk7(binary_string):
    if len(binary_string) % 8 != 0:
        exit(0)
    b11 = bytearray()
    for i in range(0, len(binary_string), 8):
        b21 = binary_string[i:i+8]
        b11.append(int(b21, 2))
    return b11
fonk1()
print("\n\n")
b22 = os.path.getsize(sys.argv[2]) / (1024 * 1024.0)
b23 = os.path.getsize(b3) / (1024 * 1024.0)
b24 = ((b23 / b22) * 100)
print("Original Text: " + str(sys.argv[2]) + " Size: " + str(b22) + " MB")
print("Compressed File: " + b3 + " Size: " + str(b23) + " MB")
print("File " + sys.argv[2] + " compressed by " + str(round(b24)) + "%")
print("Text file compressed successfully! :) !!\n\n")