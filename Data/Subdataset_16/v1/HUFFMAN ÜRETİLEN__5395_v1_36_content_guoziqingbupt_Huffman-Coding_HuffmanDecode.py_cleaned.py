class class1:
    def fonk1(self, b1 = None, b2=None, b3=None):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
def fonk2(node):
    return node.b2 is None and node.b3 is None
def fonk3(text, b8):
    b4 = ""
    b5 = b8
    for b6 in text:
        if not fonk2(b5):
            if b6 = = "0":
                b5 = b5.b2
            elif b6 = = "1":
                b5 = b5.b3
        if fonk2(b5):
            b4 += b5.b1
            b5 = b8
    return b4
if b7 = = "__main__":
    b8 = class1()
    b8.b2 = class1()
    b8.b3 = class1('c')
    b8.b2.b2 = class1('a')
    b8.b2.b3 = class1('b')
    b9 = "000110"
    b10 = fonk3(b9, b8)
    print("Decoded text:", b10)
