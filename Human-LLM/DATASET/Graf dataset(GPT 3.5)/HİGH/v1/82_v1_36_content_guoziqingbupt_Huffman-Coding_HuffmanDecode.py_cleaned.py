class class1:
    def fonk1(self, b2, b1 = None, b3=None):
        self.b2 = b2
        self.b1 = b1
        self.b3 = b3
def fonk2(text, b7):
    b4 = ""
    b5 = b7
    for b6 in text:
        if not fonk3(b5) and b6 = = "0":
            b5 = b5.b1
        elif not fonk3(b5) and b6 = = "1":
            b5 = b5.b3
        if fonk3(b5):
            b4 += b5.b2
            b5 = b7
    return b4
def fonk3(node):
    return node.b1 is None and node.b3 is None
b7 = class1('*')
b7.b1 = class1('A')
b7.b3 = class1('*')
b7.b3.b1 = class1('B')
b7.b3.b3 = class1('*')
b7.b3.b3.b1 = class1('C')
b7.b3.b3.b3 = class1('D')
b8 = "010101001010101001011110"
b9 = fonk2(b8, b7)
print("Decoded text:", b9)