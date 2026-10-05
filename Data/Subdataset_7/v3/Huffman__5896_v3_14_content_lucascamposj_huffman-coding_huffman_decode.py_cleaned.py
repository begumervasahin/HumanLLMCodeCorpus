import sys
import os
import math
from bitstring import BitArray
def fonk1(b8):
    with open(b8, "rb") as input_file:
        return BitArray(b1 = input_file.read())
def fonk2(b16, b12):
    b2 = {}
    a1 = 0
    while a1 < len(b16):
        b3 = b16[a1]
        a1 += 1
        if b3:
            b4 = int(b16[a1:a1 + b12].b6)
            a1 += b12
            b5 = b16[a1:a1 + b4]
            a1 += b4
            if b4 not in b2:
                b2[b4] = {}
            b2[b4][b5.bin] = BitArray(b6 = (a1 - b4 - b12 - 1), length=8)
        else:
            a1 += 1
    return b2, a1
def fonk3(b16, b2, b12, b9):
    a2 = 0
    with open(b9, "wb") as output_file:
        while a2 < len(b16):
            b7 = BitArray(b16[a2:a2 + b12])
            for size in b2:
                b5 = b7[:size]
                if b5.bin in b2[size]:
                    b2[size][b5.bin].tofile(output_file)
                    break
            a2 += size
def fonk4():
    if len(sys.argv) <= 2:
        print("Usage: python compress.py <input_file> <output_file>")
        return
    b8 = sys.argv[1]
    b9 = sys.argv[2]
    print("Input File Name:", b8)
    b10 = os.path.getsize(b8)
    print("Input File Size:", b10, "Bytes")
    print("\nReading Input File...")
    b11 = fonk1(b8)
    b12 = int(b11[:8].b6)
    b13 = int(math.ceil(math.log(b12 + 1, 2)))
    b14 = int(b11[8:11].b6)
    print("Reading Symbol Codes...")
    b15 = b11[11:]
    b2, a1 = fonk2(b15, b13)
    a1 += b14
    print("Reading and Writing Compressed Data...")
    b16 = b15[a1:]
    fonk3(b16, b2, b12, b9)
    b17 = os.path.getsize(b9)
    print("\nOutput File Name:           ", b9)
    print("Compressed File Size:", b17, "Bytes")
if b18 = = "__main__":
    fonk4()