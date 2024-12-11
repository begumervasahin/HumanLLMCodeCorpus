import sys
import os
import math
from bitstring import BitArray
def fonk1():
    if len(sys.argv) > 2:
        b1 = sys.argv[1]
        b2 = sys.argv[2]
        print("File Name:", b1)
        b3 = os.path.getsize(b1)
        print("File Size:", b3, "Bytes")
        print("\nReading File...")
        with open(b1, "rb") as f:
            b4 = BitArray(bytes=f.read())
        b5 = int(b4[:8].b13)
        b6 = int(math.ceil(math.log(b5 + 1, 2)))
        b7 = int(b4[8:11].b13)
        print("Reading Symbol Codes...")
        b8 = b4[11:]
        b9 = {}
        a1 = 0
        for s in range(256):
            if b8[a1]:
                a1 += 1
                b10 = a1 + b6
                b11 = int(b8[a1:b10].b13)
                b12 = b8[b10:(b10 + b11)]
                a1 = b10 + b11
                if b11 not in b9:
                    b9[b11] = {}
                b9[b11][b12.bin] = BitArray(b13 = s, length=8)
            else:
                a1 += 1
        a1 += b7
        print("Reading and Writing Compressed Data...")
        b14 = b8[a1:]
        b15 = BitArray()
        a2 = 0
        with open(b2, "wb") as w:
            while a2 < b14.length:
                b16 = BitArray(b14[a2:(a2 + b5)])
                for size in b9:
                    if size <= 1:
                        b12 = BitArray(b13=b16[0], length=1)
                    else:
                        b12 = b16[:size]
                    if b12.bin in b9[size]:
                        b9[size][b12.bin].tofile(w)
                        break
                a2 += size
        b17 = os.path.getsize(b2)
        print("\nFile Name:           ", b2)
        print("Compressed file size:", b17, "Bytes")
if b18 = = "__main__":
    fonk1()