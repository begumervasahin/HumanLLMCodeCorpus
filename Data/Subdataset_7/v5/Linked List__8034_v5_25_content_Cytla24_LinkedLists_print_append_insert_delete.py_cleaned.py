class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self):
        b4 = self.b3
        while b4 is not None:
            print(b4.b1)
            b4 = b4.b2
    def fonk4(self, b1):
        b5 = class1(b1)
        b5.b2 = self.b3
        self.b3 = b5
    def fonk5(self, node, b1):
        b5 = class1(b1)
        b5.b2 = node.b2
        node.b2 = b5
    def fonk6(self, b1):
        b5 = class1(b1)
        if self.b3 is None:
            self.b3 = b5
            return
        b4 = self.b3
        while b4.b2 is not None:
            b4 = b4.b2
        b4.b2 = b5
    def fonk7(self, b1):
        b4 = self.b3
        if b4 is not None and b4.b1 = = b1:
            self.b3 = b4.b2
            b4 = None
            return
        b6 = None
        while b4 is not None and b4.b1 != b1:
            b6 = b4
            b4 = b4.b2
        if b4 is None:
            return
        b6.b2 = b4.b2
        b4 = None
b7 = class2()
b7.b3 = class1("Aimie Ojuba")
b8 = class1("latifs")
b9 = class1("Toni")
b10 = class1("slap")
b7.b3.b2 = b8
b8.b2 = b9
b9.b2 = b10
b7.fonk4("imaa")
b7.fonk6("beast")
b7.fonk5(b7.b3.b2, "shile")
b7.fonk7("slap")
b7.fonk3()