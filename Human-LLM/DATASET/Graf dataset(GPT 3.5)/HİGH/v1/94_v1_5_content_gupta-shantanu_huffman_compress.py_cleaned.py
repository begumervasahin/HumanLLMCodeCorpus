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
    def fonk3(self, new_node):
        if new_node.b5.b2 < self.b5.b2:
            new_node.b6 = self
            return new_node
        else:
            b7 = self
            while b7.b6 is not None and b7.b6.b5.b2 < new_node.b5.b2:
                b7 = b7.b6
            new_node.b6 = b7.b6
            b7.b6 = new_node
            return self
    def fonk4(self):
        return self.b5
def fonk5(b5, b23, prefix):
    if b5.b3 is None and b5.b4 is None:
        b23[b5.b1] = prefix
    if b5.b3 is not None:
        fonk5(b5.b3, b23, prefix + "0")
    if b5.b4 is not None:
        fonk5(b5.b4, b23, prefix + "1")
def fonk6(b5, prefix):
    if b5.b3 is None and b5.b4 is None:
        b21.append('1')
        b21.append('{0:08b}'.format(prefix + ord(b5.b1)))
    else:
        b21.append('0')
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
for b17 in b13[:0:-1]:
    if b17.b2 != 0:
        b16 = class2(b17)
        b16.b6 = b15
        b15 = b16
    else:
        break
a1 = 0
while True:
    b17 = b15.fonk4()
    b15 = b15.b6
    b18 = b15.fonk4()
    b15 = b15.b6
    b19 = class1(257, b17.b2 + b18.b2)
    b19.b4 = b17 if b17.b2 > b18.b2 else b18
    b19.b3 = b18 if b17.b2 > b18.b2 else b17
    b16 = class2(b19)
    if b15 != 0:
        b15 = b15.fonk3(b16)
    else:
        a1 = b19
        break
b20 = open(b9, 'wb')
b21 = []
def fonk7(st):
    b22 = ""
    for ch in st:
        b22 += ch
    return b22
def fonk8(a1):
    b23 = {0: 0}
    fonk5(a1, b23, "")
    fonk6(a1, 16)
    b24 = fonk7(b21)
    b25 = len(b24)
    b20.write(struct.pack('B', b25
    b20.write(struct.pack('B', b25 % 256))
    b26 = ""
    for ch in b24:
        b26 = b26 + ch
        if len(b26) > b28:
            b20.write(struct.pack('B', int(b26[0:b28], 2)))
            b26 = b26[b28:]
    b27 = ""
    for ch in b11:
        b26 += b23[ch]
        b27 += b23[ch]
        if len(b26) > b28:
            b20.write(struct.pack('B', int(b26[0:b28], 2)))
            b26 = b26[b28:]
    b26 += "1"
    while len(b26) % b28 = = 0:
        b26 += "0"
    while b26 != "":
        b20.write(struct.pack('B', int("0b" + b26[0:b28], 2)))
        b26 = b26[b28:]
    b20.flush()
try:
    fonk8(a1)
    print("Job completed!")
except Exception as e:
    print("An error occurred:", e)