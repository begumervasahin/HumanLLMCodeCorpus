import sys
import os
import math
from bitstring import BitArray
def fonk1(b7):
    with open(b7, "rb") as file:
        return BitArray(b1 = file.read())
def fonk2(b14, b12):
    b2 = {}
    a1 = 0
    for s in range(256):
        if b14[a1]:
            a1 += 1
            b3 = b14[a1:a1 + b12].b5
            b4 = b14[a1 + b12:a1 + b12 + b3]
            a1 += b12 + b3
            if b3 not in b2:
                b2[b3] = {}
            b2[b3][b4.bin] = BitArray(b5 = s, length=8)
        else:
            a1 += 1
    return b2, a1
def fonk3(b15, b2, b11, b8):
    with open(b8, "wb") as output_file:
        a2 = 0
        while a2 < b15.length:
            b6 = BitArray(b15[a2:a2 + b11])
            for size in b2:
                b4 = b6[:size]
                if b4.bin in b2[size]:
                    b2[size][b4.bin].tofile(output_file)
                    a2 += size
                    break
def fonk4():
    if len(sys.argv) < 3:
        print("Usage: python decompress.py <input_file> <output_file>")
        return
    b7 = sys.argv[1]
    b8 = sys.argv[2]
    print(f"Input File: {b7}")
    b9 = os.path.getsize(b7)
    print(f"File Size: {b9} Bytes")
    print("\nReading File...")
    b10 = fonk1(b7)
    b11 = b10[:8].b5
    b12 = math.ceil(math.log2(b11 + 1))
    b13 = b10[8:11].b5
    print("Parsing Symbol Codes...")
    b14 = b10[11:]
    b2, a1 = fonk2(b14, b12)
    a1 += b13
    print("Decompressing Data...")
    b15 = b14[a1:]
    fonk3(b15, b2, b11, b8)
    b16 = os.path.getsize(b8)
    print(f"\nOutput File: {b8}")
    print(f"Decompressed File Size: {b16} Bytes")
if b17 = = "__main__":
    fonk4()