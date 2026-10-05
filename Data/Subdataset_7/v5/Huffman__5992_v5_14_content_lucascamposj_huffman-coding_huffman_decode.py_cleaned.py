import sys
import os
import math
from bitstring import BitArray
def fonk1(b14, b12):
    b1 = {}
    a1 = 0
    for s in range(256):
        if b14[a1]:
            a1 += 1
            b2 = a1 + b12
            b3 = int(b14[a1:b2].b5)
            b4 = b14[b2:(b2 + b3)]
            a1 = b2 + b3
            if b3 not in b1:
                b1[b3] = {}
            b1[b3][b4.bin] = BitArray(b5 = s, length=8)
        else:
            a1 += 1
    return b1, a1
def fonk2(b15, b1, b11, b8):
    a2 = 0
    with open(b8, "wb") as w:
        while a2 < b15.length:
            b6 = BitArray(b15[a2:(a2 + b11)])
            for size in b1:
                if size <= 1:
                    b4 = BitArray(b5=b6[0], length=1)
                else:
                    b4 = b6[:size]
                if b4.bin in b1[size]:
                    b1[size][b4.bin].tofile(w)
                    break
            a2 += size
def fonk3():
    if len(sys.argv) > 2:
        b7 = sys.argv[1]
        b8 = sys.argv[2]
        print("File Name:", b7)
        b9 = os.path.getsize(b7)
        print("File Size:", b9, "Bytes")
        print("\nReading File...")
        with open(b7, "rb") as f:
            b10 = BitArray(bytes=f.read())
        b11 = int(b10[:8].b5)
        b12 = int(math.ceil(math.log(b11 + 1, 2)))
        b13 = int(b10[8:11].b5)
        print("Reading Symbol Codes...")
        b14 = b10[11:]
        b1, a1 = fonk1(b14, b12)
        a1 += b13
        print("Reading and Writing Compressed Data...")
        b15 = b14[a1:]
        fonk2(b15, b1, b11, b8)
        b16 = os.path.getsize(b8)
        print("\nFile Name:           ", b8)
        print("Compressed file size:", b16, "Bytes")
if b17 = = "__main__":
    fonk3()