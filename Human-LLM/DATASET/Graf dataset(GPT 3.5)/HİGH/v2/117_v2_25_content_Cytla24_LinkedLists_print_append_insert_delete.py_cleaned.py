class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self):
        b4 = self.b3
        while b4:
            print(b4.b1)
            b4 = b4.b2
    def fonk4(self, b1):
        b5 = class1(b1)
        b5.b2 = self.b3
        self.b3 = b5
    def fonk5(self, prev_node, b1):
        if prev_node is None:
            print("Previous node must be valid.")
            return
        b5 = class1(b1)
        b5.b2 = prev_node.b2
        prev_node.b2 = b5
    def fonk6(self, b1):
        b5 = class1(b1)
        if self.b3 is None:
            self.b3 = b5
            return
        b6 = self.b3
        while b6.b2:
            b6 = b6.b2
        b6.b2 = b5
    def fonk7(self, key):
        b4 = self.b3
        if b4 and b4.b1 = = key:
            self.b3 = b4.b2
            b4 = None
            return
        b7 = None
        while b4 and b4.b1 != key:
            b7 = b4
            b4 = b4.b2
        if b4 is None:
            return
        b7.b2 = b4.b2
        b4 = None
b8 = class2()
b8.b3 = class1("Aimie Ojuba")
b9 = class1("latifs")
b10 = class1("Toni")
b11 = class1("slap")
b8.b3.b2 = b9
b9.b2 = b10
b10.b2 = b11
b8.fonk4("imaa")
b8.fonk6("beast")
b8.fonk5(b9, "shile")
b8.fonk7("slap")
b8.fonk3()