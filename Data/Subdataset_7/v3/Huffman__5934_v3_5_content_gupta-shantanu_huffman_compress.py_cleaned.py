import sys
import struct
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = None
        self.b4 = None
class class2:
    def fonk2(self, b5):
        self.b5 = b5
        self.b6 = None
    def fonk3(self, b22):
        if b22.b5.b2 < self.b5.b2:
            b22.b6 = self
            return b22
        else:
            b7 = self
            while b7.b6 is not None and b7.b6.b5.b2 < b22.b5.b2:
                b7 = b7.b6
            b22.b6 = b7.b6
            b7.b6 = b22
            return self
    def fonk4(self):
        return self.b5
def fonk5(b5, dictionary, prefix):
    if b5.b3 is None and b5.b4 is None:
        dictionary[b5.b1] = prefix
    if b5.b3 is not None:
        fonk5(b5.b3, dictionary, prefix + "0")
    if b5.b4 is not None:
        fonk5(b5.b4, dictionary, prefix + "1")
def fonk6(b5, prefix):
    if b5.b3 is None and b5.b4 is None:
        b27.append('1')
        b27.append('{0:08b}'.format(prefix + ord(b5.b1)))
    else:
        b27.append('0')
        fonk6(b5.b3, prefix + 1)
        fonk6(b5.b4, prefix + 1)
def fonk7(bits):
    b8 = ""
    for bit in bits:
        b8 += bit
    return b8
def fonk8(b23, compressed_file):
    b9 = {0: 0}
    fonk5(b23, b9, "")
    fonk6(b23, 16)
    b10 = fonk7(b27)
    b11 = len(b10)
    compressed_file.write(struct.pack('BB', b11
    b12 = ""
    for bit in b10:
        b12 += bit
        if len(b12) > b14:
            compressed_file.write(struct.pack('B', int(b12[0:b14], 2)))
            b12 = b12[b14:]
    b13 = ""
    for ch in b17:
        b13 += b9[ch]
        if len(b13) > b14:
            compressed_file.write(struct.pack('B', int(b13[0:b14], 2)))
            b13 = b13[b14:]
    b13 += "1"
    while len(b13) % b14 = = 0:
        b13 += "0"
    while b13:
        compressed_file.write(struct.pack('B', int("0b" + b13[0:b14], 2)))
        b13 = b13[b14:]
    compressed_file.flush()
try:
    b15 = sys.argv[1]
    b16 = sys.argv[2] if len(sys.argv) > 2 else "compressed.huff"
except IndexError:
    print("Usage: python huffman_compress.py <b15> [<b16>]")
    sys.exit(1)
try:
    with open(b15, 'rb') as file:
        b17 = file.read()
        b18 = len(b17)
except FileNotFoundError:
    print("Input file not found!")
    sys.exit(1)
b19 = [class1(i, 0) for i in range(256)]
for ch in b17:
    b19[ch].b2 += 1
b19.sort(b20 = lambda x: x.b2)
b21 = class2(b19[0])
for b24 in b19[:0:-1]:
    if b24.b2 != 0:
        b22 = class2(b24)
        b22.b6 = b21
        b21 = b22
    else:
        break
b23 = None
while True:
    b24 = b21.fonk4()
    b21 = b21.b6
    b25 = b21.fonk4()
    b21 = b21.b6
    b22 = class1(257, b24.b2 + b25.b2)
    b22.b4 = b24 if b24.b2 > b25.b2 else b25
    b22.b3 = b25 if b24.b2 > b25.b2 else b24
    b26 = class2(b22)
    if b21:
        b21 = b21.fonk3(b26)
    else:
        b23 = b22
        break
with open(b16, 'wb') as compressed_file:
    b27 = []
    try:
        fonk8(b23, compressed_file)
        print("Compression completed successfully!")
    except Exception as e:
        print("An error occurred:", e)