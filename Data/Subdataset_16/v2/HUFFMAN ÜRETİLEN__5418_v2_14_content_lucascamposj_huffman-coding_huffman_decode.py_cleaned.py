import sys
import os
import math
from bitstring import BitArray
def fonk1(b13):
    b1 = int(b13[:8].b7)
    b2 = int(math.ceil(math.log(b1 + 1, 2)))
    b3 = int(b13[8:11].b7)
    return b1, b2, b3
def fonk2(b14, b2):
    b4 = {}
    a1 = 0
    for s in range(256):
        if b14[a1]:
            a1 += 1
            b5 = int(b14[a1:a1 + b2].b7)
            b6 = b14[a1 + b2:a1 + b2 + b5]
            a1 += b2 + b5
            if b5 not in b4:
                b4[b5] = {}
            b4[b5][b6.bin] = BitArray(b7 = s, length=8)
        else:
            a1 += 1
    return b4, a1
def fonk3(b15, b4, b1, b11):
    b8 = BitArray()
    a2 = 0
    with open(b11, "wb") as output_file:
        while a2 < b15.length:
            b9 = BitArray(b15[a2:a2 + b1])
            for size, codes in b4.items():
                b6 = b9[:size]
                if b6.bin in codes:
                    codes[b6.bin].tofile(output_file)
                    a2 += size
                    break
def fonk4():
    if len(sys.argv) < 3:
        print("Usage: python decompress.py <input_file> <output_file>")
        return
    b10 = sys.argv[1]
    b11 = sys.argv[2]
    print(f"Input File: {b10}")
    b12 = os.path.getsize(b10)
    print(f"Input File Size: {b12} Bytes")
    print("\nReading File...")
    with open(b10, "rb") as input_file:
        b13 = BitArray(bytes=input_file.read())
    b1, b2, b3 = fonk1(b13)
    print("Reading Symbol Codes...")
    b14 = b13[11:]
    b4, a1 = fonk2(b14, b2)
    a1 += b3
    print("Reading and Writing Compressed Data...")
    b15 = b14[a1:]
    fonk3(b15, b4, b1, b11)
    b16 = os.path.getsize(b11)
    print(f"\nOutput File: {b11}")
    print(f"Output File Size: {b16} Bytes")
if b17 = = "__main__":
    fonk4()