class class1:
    class class2:
        def fonk1(self, b1 = None, b2=None):
            self.b1 = b1
            self.b2 = b2
            self.b3 = None
            self.b4 = None
    def fonk2(self):
        self.b5 = self.class2()
        self.b6 = self.class2()
        self.b5.b4 = self.b6
        self.b6.b3 = self.b5
    def fonk3(self, b1, b2):
        b7 = self.class2(b1, b2)
        self.fonk7(b7)
        return b7
    def fonk4(self, node):
        self.fonk6(node)
        self.fonk7(node)
    def fonk5(self, b1, b2):
        b7 = self.class2(b1, b2)
        self.fonk8()
        self.fonk7(b7)
        return b7
    def fonk6(self, node):
        node.b3.b4 = node.b4
        node.b4.b3 = node.b3
    def fonk7(self, node):
        node.b3 = self.b6.b3
        node.b4 = self.b6
        self.b6.b3.b4 = node
        self.b6.b3 = node
    def fonk8(self):
        if self.b5.b4 != self.b6:
            b8 = self.b5.b4
            self.fonk6(b8)
            return b8
    def fonk9(self):
        if self.b5.b4 != self.b6:
            return self.b5.b4
    def fonk10(self):
        b9 = self.b5.b4
        while b9 != self.b6:
            print(f"({b9.b1}, {b9.b2})")
            b9 = b9.b4
class class3:
    def fonk11(self, b11):
        self.b10 = {}
        self.b11 = b11
        self.a1 = 0
        self.b12 = class1()
    def fonk12(self, b1):
        if b1 in self.b10:
            self.b12.fonk4(self.b10[b1])
        else:
            print(-1)
    def fonk13(self, b1, b2):
        if b1 in self.b10:
            self.b12.fonk4(self.b10[b1])
            self.b10[b1].b2 = b2
        else:
            if self.a1 >= self.b11:
                del self.b10[self.b12.fonk8().b1]
                self.a1 -= 1
            self.b10[b1] = self.b12.fonk3(b1, b2)
            self.a1 += 1
    def fonk14(self):
        self.b12.fonk10()
if b13 = = "__main__":
    b10 = class3(5)
    b10.fonk13(1, 1)
    b10.fonk13(2, 2)
    b10.fonk13(3, 3)
    b10.fonk13(4, 4)
    b10.fonk13(5, 5)
    b10.fonk12(1)
    b10.fonk13(6, 6)
    b10.fonk13(7, 7)
    b10.fonk12(11)
    b10.fonk14()