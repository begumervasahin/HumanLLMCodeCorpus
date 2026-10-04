import sys
import os
import math
from bitstring import BitArray
def fonk1(b9):
    with open(b9, "rb") as f:
        return BitArray(b1 = f.read())
def fonk2(b16, b14):
    b2 = {}
    a1 = 0
    for s in range(256):
        if b16[a1]:
            a1 += 1
            b3 = a1 + b14
            b4 = int(b16[a1:b3].b6)
            b5 = b16[b3:(b3 + b4)]
            a1 = b3 + b4
            if b4 not in b2:
                b2[b4] = {}
            b2[b4][b5.bin] = BitArray(b6 = s, length=8)
        else:
            a1 += 1
    return b2, a1
def fonk3(b17, b2, b13, b10):
    b7 = BitArray()
    a2 = 0
    with open(b10, "wb") as w:
        while a2 < b17.length:
            b8 = BitArray(b17[a2:(a2 + b13)])
            for size in b2:
                b5 = b8[:size] if size > 1 else BitArray(b6=b8[0], length=1)
                if b5.bin in b2[size]:
                    b2[size][b5.bin].tofile(w)
                    break
            a2 += size
def fonk4():
    if len(sys.argv) > 2:
        b9 = sys.argv[1]
        b10 = sys.argv[2]
        print(f"File Name: {b9}")
        b11 = os.path.getsize(b9)
        print(f"File Size: {b11} Bytes")
        print("\nReading File...")
        b12 = fonk1(b9)
        b13 = int(b12[:8].b6)
        b14 = int(math.ceil(math.log(b13 + 1, 2)))
        b15 = int(b12[8:11].b6)
        print("Reading Symbol Codes...")
        b16 = b12[11:]
        b2, a1 = fonk2(b16, b14)
        a1 += b15
        print("Reading and Writing Compressed Data...")
        b17 = b16[a1:]
        fonk3(b17, b2, b13, b10)
        b18 = os.path.getsize(b10)
        print(f"\nFile Name:           {b10}")
        print(f"Compressed file size: {b18} Bytes")
if b19 = = "__main__":
    fonk4()