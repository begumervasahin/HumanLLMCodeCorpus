from queue import PriorityQueue
class class1:
    def fonk1(self, b2, b3, b1 = None, b4=None):
        self.b2 = b2
        self.b3 = b3
        self.b1 = b1
        self.b4 = b4
    def fonk2(self, other):
        return self.b3 < other.b3
    def fonk3(self):
        return f"class1(b2 = {self.b2}, b3={self.b3})"
def fonk4(string):
    b5 = {}
    for char in string:
        if char in b5:
            b5[char] += 1
        else:
            b5[char] = 1
    b6 = PriorityQueue()
    for char, b3 in b5.items():
        b6.put(class1(char, b3))
    return b6
def fonk5(b6):
    while b6.qsize() > 1:
        b7 = b6.get()
        b8 = b6.get()
        b9 = b7.b3 + b8.b3
        b10 = class1(None, b9, b7, b8)
        b6.put(b10)
    return b6.get()
def fonk6(node, b11 = '', b12=None):
    if b12 is None:
        b12 = {}
    if node.b1 is None and node.b4 is None:
        b12[node.b2] = b11
    else:
        if node.b1 is not None:
            fonk6(node.b1, b11 + '0', b12)
        if node.b4 is not None:
            fonk6(node.b4, b11 + '1', b12)
    return b12
def fonk7(string, b12):
    return ''.join(b12[char] for char in string)
def fonk8(b18, b17):
    b13 = ''
    b14 = b17
    for bit in b18:
        b14 = b14.b1 if bit == '0' else b14.b4
        if b14.b1 is None and b14.b4 is None:
            b13 += b14.b2
            b14 = b17
    return b13
if b15 = = "__main__":
    with open('texteEncode.txt', 'r') as file:
        b16 = file.read()
    b6 = fonk4(b16)
    b17 = fonk5(b6)
    b12 = fonk6(b17)
    b18 = fonk7(b16, b12)
    with open('texteEncode.txt', 'w') as file:
        file.write(b18)
    b13 = fonk8(b18, b17)
    print(b13)