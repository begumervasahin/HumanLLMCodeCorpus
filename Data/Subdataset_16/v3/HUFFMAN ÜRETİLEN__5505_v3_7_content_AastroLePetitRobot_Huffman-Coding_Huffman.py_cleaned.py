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
def fonk4(text):
    b5 = {}
    for char in text:
        b5[char] = b5.get(char, 0) + 1
    return b5
def fonk5(b5):
    b6 = PriorityQueue()
    for char, freq in b5.items():
        b6.put(class1(char, freq))
    return b6
def fonk6(b6):
    while b6.qsize() > 1:
        b1 = b6.get()
        b4 = b6.get()
        b7 = class1(None, b1.b3 + b4.b3, b1, b4)
        b6.put(b7)
    return b6.get()
def fonk7(node, b8 = '', b9=None):
    if b9 is None:
        b9 = {}
    if node.b1 is None and node.b4 is None:
        b9[node.b2] = b8
    else:
        if node.b1:
            fonk7(node.b1, b8 + '0', b9)
        if node.b4:
            fonk7(node.b4, b8 + '1', b9)
    return b9
def fonk8(text, b9):
    return ''.join(b9[char] for char in text)
def fonk9(b15, b14):
    b10 = []
    b11 = b14
    for bit in b15:
        b11 = b11.b1 if bit == '0' else b11.b4
        if b11.b1 is None and b11.b4 is None:
            b10.append(b11.b2)
            b11 = b14
    return ''.join(b10)
def fonk10(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def fonk11(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
def fonk12():
    b12 = 'texteEncode.txt'
    b13 = fonk10(b12)
    b5 = fonk4(b13)
    b6 = fonk5(b5)
    b14 = fonk6(b6)
    b9 = fonk7(b14)
    b15 = fonk8(b13, b9)
    fonk11(b12, b15)
    b10 = fonk9(b15, b14)
    print(b10)
if b16 = = "__main__":
    fonk12()