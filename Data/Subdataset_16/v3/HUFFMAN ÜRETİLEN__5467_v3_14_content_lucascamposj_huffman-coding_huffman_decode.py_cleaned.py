import sys
import os
import math
from bitstring import BitArray
def fonk1(b11):
    b1 = b11[:8].b7
    b2 = math.ceil(math.log(b1 + 1, 2))
    b3 = b11[8:11].b7
    return b1, b2, b3
def fonk2(b12, b2):
    b4 = {}
    a1 = 0
    for s in range(256):
        if b12[a1]:
            a1 += 1
            b5 = b12[a1:a1 + b2].b7
            b6 = b12[a1 + b2:a1 + b2 + b5]
            a1 += b2 + b5
            if b5 not in b4:
                b4[b5] = {}
            b4[b5][b6.bin] = BitArray(b7 = s, length=8)
        else:
            a1 += 1
    return b4, a1
def fonk3(b13, b4, b1, b10):
    with open(b10, "wb") as output_file:
        a2 = 0
        while a2 < b13.length:
            b8 = b13[a2:a2 + b1]
            for size, codes in b4.items():
                b6 = b8[:size]
                if b6.bin in codes:
                    codes[b6.bin].tofile(output_file)
                    a2 += size
                    break
def fonk4():
    if len(sys.argv) < 3:
        print("Usage: python decompress.py <input_file> <output_file>")
        return
    b9 = sys.argv[1]
    b10 = sys.argv[2]
    print(f"Input File: {b9}")
    print(f"Input File Size: {os.path.getsize(b9)} Bytes\n")
    print("Reading File...")
    with open(b9, "rb") as input_file:
        b11 = BitArray(bytes=input_file.read())
    b1, b2, b3 = fonk1(b11)
    print("Reading Symbol Codes...")
    b12 = b11[11:]
    b4, a1 = fonk2(b12, b2)
    a1 += b3
    print("Decompressing Data...")
    b13 = b12[a1:]
    fonk3(b13, b4, b1, b10)
    print(f"\nOutput File: {b10}")
    print(f"Output File Size: {os.path.getsize(b10)} Bytes")
if b14 = = "__main__":
    fonk4()