from b5 import PriorityQueue
class class1:
    def fonk1(self, b2, b3, b1 = None, b4=None):
        self.b2 = b2
        self.b3 = b3
        self.b1 = b1
        self.b4 = b4
    def fonk2(self, other):
        return self.b3 < other.b3
    def fonk3(self):
        return "class1: value ({}) with b3 ({})\n".format(self.b2, self.b3)
def fonk4(b14):
    b5 = PriorityQueue()
    b6 = set(b14)
    for char in b6:
        b5.put(class1(char, b14.count(char)))
    return b5
def fonk5(b5):
    while b5.qsize() > 1:
        b7 = b5.get()
        b8 = b5.get()
        b3 = b7.b3 + b8.b3
        b9 = class1(None, b3, b7, b8)
        b5.put(b9)
    return b5.get()
def fonk6(node, code, b16):
    if node.b1 is None and node.b4 is None:
        b16[node.b2] = code
    if node.b1 is not None:
        fonk6(node.b1, code + "0", b16)
    if node.b4 is not None:
        fonk6(node.b4, code + "1", b16)
def fonk7(b14, b16):
    b10 = ""
    for char in b14:
        b10 += b16[char]
    return b10
def fonk8(b10, node):
    b11 = ""
    b12 = node
    for b13 in b10:
        if b13 = = "0":
            b12 = b12.b1
        elif b13 = = "1":
            b12 = b12.b4
        if b12.b2 is not None:
            b11 += b12.b2
            b12 = node
    return b11
with open('texteEncode.txt', 'r') as f:
    b14 = f.read()
b5 = fonk4(b14)
b15 = fonk5(b5)
print(b15)
b16 = {}
fonk6(b15, "", b16)
print(b16)
b10 = fonk7(b14, b16)
print(b10)
with open('texteEncode.txt', 'w') as f:
    f.write(b10)
b11 = fonk8(b10, b15)
print(b11)