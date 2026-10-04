from HUFFMAN.components import *
import struct
import sys
b1 = sys.argv[1]
try:
    b2 = sys.argv[2]
except IndexError:
    b2 = "compressed.huff"
b3 = open(b1, 'rb')
b4 = b3.read()
b5 = len(b4)
b6 = [huffnode(i, 0) for i in range(0, 256)]
for ch in b4:
    b6[ch].freq += 1
b6.sort(b7 = lambda x: x.freq)
b8 = lists(b6[0])
for b11 in b6[:0:-1]:
    if b11.freq != 0:
        b9 = lists(b11)
        b9.b10 = b8
        b8 = b9
    else:
        break
a1 = 0
while True:
    b11 = b8.top()
    b8 = b8.b10
    b12 = b8.top()
    b8 = b8.b10
    b13 = huffnode(257, b11.freq + b12.freq)
    b13.b14 = b11 if b11.freq > b12.freq else b12
    b13.b15 = b12 if b11.freq > b12.freq else b11
    b9 = lists(b13)
    if b8 != 0:
        b8 = b8.insert(b9)
    else:
        a1 = b13
        break
b16 = open(b2, 'wb')
def fonk1(st):
    b17 = ""
    for ch in st:
        b17 += ch
    return b17
def fonk2(a1):
    b18 = {0: 0}
    huffmantree(a1, b18, "")
    encodehufftree(a1, 16)
    b19 = fonk1(pt)
    b20 = len(b19)
    b16.write(struct.pack('B', int(b20 / 256)))
    b16.write(struct.pack('B', b20 % 256))
    b21 = ""
    for ch in b19:
        b21 = b21 + ch
        if len(b21) > b23:
            b16.write(struct.pack('B', int(b21[0:b23], 2)))
            b21 = b21[b23:]
    b22 = ""
    for ch in b4:
        b21 += b18[ch]
        b22 += b18[ch]
        if len(b21) > b23:
            b16.write(struct.pack('B', int(b21[0:b23], 2)))
            b21 = b21[b23:]
    b21 += "1"
    while len(b21) % b23 = = 0:
        b21.__add__("0")
    while b21 != "":
        b16.write(struct.pack('B', int("0b" + b21[0:b23], 2)))
        b21 = b21[b23:]
    b16.flush()
try:
    fonk2(a1)
    print("Job completed!")
except:
    print("An error occured!")