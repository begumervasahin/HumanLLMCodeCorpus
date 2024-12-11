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
    def fonk3(self, b16):
        if b16.b5.b2 < self.b5.b2:
            b16.b6 = self
            return b16
        else:
            b7 = self
            while b7.b6 is not None and b7.b6.b5.b2 < b16.b5.b2:
                b7 = b7.b6
            b16.b6 = b7.b6
            b7.b6 = b16
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
        b22.append('1')
        b22.append('{0:08b}'.format(prefix + ord(b5.b1)))
    else:
        b22.append('0')
        fonk6(b5.b3, prefix + 1)
        fonk6(b5.b4, prefix + 1)
b8 = sys.argv[1]
try:
    b9 = sys.argv[2]
except IndexError:
    b9 = "compressed.huff"
try:
    b10 = open(b8, 'rb')
    b11 = b10.read()
    b12 = len(b11)
except FileNotFoundError:
    print("Input b10 not found!")
    sys.exit(1)
b13 = [class1(i, 0) for i in range(0, 256)]
for ch in b11:
    b13[ch].b2 += 1
b13.sort(b14 = lambda x: x.b2)
b15 = class2(b13[0])
for b18 in b13[:0:-1]:
    if b18.b2 != 0:
        b16 = class2(b18)
        b16.b6 = b15
        b15 = b16
    else:
        break
b17 = None
while True:
    b18 = b15.fonk4()
    b15 = b15.b6
    b19 = b15.fonk4()
    b15 = b15.b6
    b16 = class1(257, b18.b2 + b19.b2)
    b16.b4 = b18 if b18.b2 > b19.b2 else b19
    b16.b3 = b19 if b18.b2 > b19.b2 else b18
    b20 = class2(b16)
    if b15 != None:
        b15 = b15.fonk3(b20)
    else:
        b17 = b16
        break
b21 = open(b9, 'wb')
b22 = []
def fonk7(bits):
    b23 = ""
    for bit in bits:
        b23 += bit
    return b23
def fonk8(b17):
    b24 = {0: 0}
    fonk5(b17, b24, "")
    fonk6(b17, 16)
    b25 = fonk7(b22)
    b26 = len(b25)
    b21.write(struct.pack('B', b26
    b21.write(struct.pack('B', b26 % 256))
    b27 = ""
    for bit in b25:
        b27 = b27 + bit
        if len(b27) > b29:
            b21.write(struct.pack('B', int(b27[0:b29], 2)))
            b27 = b27[b29:]
    b28 = ""
    for ch in b11:
        b28 += b24[ch]
        if len(b28) > b29:
            b21.write(struct.pack('B', int(b28[0:b29], 2)))
            b28 = b28[b29:]
    b28 += "1"
    while len(b28) % b29 = = 0:
        b28 += "0"
    while b28 != "":
        b21.write(struct.pack('B', int("0b" + b28[0:b29], 2)))
        b28 = b28[b29:]
    b21.flush()
try:
    fonk8(b17)
    print("Compression completed successfully!")
except Exception as e:
    print("An error occurred:", e)