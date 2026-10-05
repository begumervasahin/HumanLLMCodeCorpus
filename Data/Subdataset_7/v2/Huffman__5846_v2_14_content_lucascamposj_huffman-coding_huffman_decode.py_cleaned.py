import sys
import os
import math
from bitstring import BitArray
def fonk1():
    if len(sys.argv) > 2:
        b1 = sys.argv[1]
        b2 = sys.argv[2]
        print("Input File Name:", b1)
        b3 = os.path.getsize(b1)
        print("Input File Size:", b3, "Bytes")
        print("\nReading Input File...")
        with open(b1, "rb") as input_file:
            b4 = BitArray(bytes=input_file.read())
        b5 = int(b4[:8].b13)
        b6 = int(math.ceil(math.log(b5 + 1, 2)))
        b7 = int(b4[8:11].b13)
        print("Reading Symbol Codes...")
        b8 = b4[11:]
        b9 = {}
        a1 = 0
        for symbol in range(256):
            if b8[a1]:
                a1 += 1
                b10 = a1 + b6
                b11 = int(b8[a1:b10].b13)
                b12 = b8[b10:(b10 + b11)]
                a1 = b10 + b11
                if b11 not in b9:
                    b9[b11] = {}
                b9[b11][b12.bin] = BitArray(b13 = symbol, length=8)
            else:
                a1 += 1
        a1 += b7
        print("Reading and Writing Compressed Data...")
        b14 = b8[a1:]
        a2 = 0
        with open(b2, "wb") as output_file:
            while a2 < b14.length:
                b15 = BitArray(b14[a2:(a2 + b5)])
                for size in b9:
                    if size <= 1:
                        b12 = BitArray(b13=b15[0], length=1)
                    else:
                        b12 = b15[:size]
                    if b12.bin in b9[size]:
                        b9[size][b12.bin].tofile(output_file)
                        break
                a2 += size
        b16 = os.path.getsize(b2)
        print("\nOutput File Name:           ", b2)
        print("Compressed File Size:", b16, "Bytes")
if b17 = = "__main__":
    fonk1()