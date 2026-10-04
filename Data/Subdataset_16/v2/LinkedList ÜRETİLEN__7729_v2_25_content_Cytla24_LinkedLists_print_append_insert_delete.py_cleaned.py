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
    def fonk5(self, prev_node, b1):
        if prev_node is None:
            print("The given previous node must be in the class2.")
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
        while b6.b2 is not None:
            b6 = b6.b2
        b6.b2 = b5
    def fonk7(self, key):
        b4 = self.b3
        if b4 is not None:
            if b4.b1 = = key:
                self.b3 = b4.b2
                b4 = None
                return
        b7 = None
        while b4 is not None and b4.b1 != key:
            b7 = b4
            b4 = b4.b2
        if b4 is None:
            return
        b7.b2 = b4.b2
        b4 = None
if b8 = = "__main__":
    b9 = class2()
    b9.b3 = class1("Aimie Ojuba")
    b10 = class1("Latifs")
    b11 = class1("Toni")
    b12 = class1("Slap")
    b9.b3.b2 = b10
    b10.b2 = b11
    b11.b2 = b12
    b9.fonk4("Imaa")
    b9.fonk6("Beast")
    b9.fonk5(b9.b3.b2, "Shile")
    b9.fonk7("Slap")
    b9.fonk3()