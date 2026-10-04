class class1:
    def fonk1(self, b1 = None, b2=None, b3=None):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
def fonk2(node):
    return node.b2 is None and node.b3 is None
def fonk3(b8, b7):
    b4 = ""
    b5 = b7
    for bit in b8:
        b5 = b5.b2 if bit == "0" else b5.b3
        if fonk2(b5):
            b4 += b5.b1
            b5 = b7
    return b4
if b6 = = "__main__":
    b7 = class1()
    b7.b2 = class1()
    b7.b3 = class1('c')
    b7.b2.b2 = class1('a')
    b7.b2.b3 = class1('b')
    b8 = "000110"
    b4 = fonk3(b8, b7)
    print("Decoded text:", b4)
