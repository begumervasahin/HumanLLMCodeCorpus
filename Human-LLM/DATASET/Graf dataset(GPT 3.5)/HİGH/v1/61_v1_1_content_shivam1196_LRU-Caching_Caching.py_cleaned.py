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
    def fonk4(self, b13):
        self.fonk6(b13)
        self.fonk7(b13)
    def fonk5(self, b1, b2):
        b7 = self.class2(b1, b2)
        self.fonk8()
        self.fonk7(b7)
        return b7
    def fonk6(self, b13):
        b13.b3.b4 = b13.b4
        b13.b4.b3 = b13.b3
    def fonk7(self, b13):
        b13.b3 = self.b6.b3
        b13.b4 = self.b6
        self.b6.b3.b4 = b13
        self.b6.b3 = b13
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
    def fonk11(self, b1 = None, b2=None):
        self.b1 = b1
        self.b2 = b2
class class4:
    def fonk12(self, capacity):
        self.b10 = {}
        self.b11 = capacity
        self.a1 = 0
        self.b12 = class1()
    def fonk13(self, b1):
        if b1 in self.b10:
            self.b12.fonk4(self.b10[b1])
        else:
            print(-1)
    def fonk14(self, b1, b2):
        if self.a1 < self.b11:
            self.b10[b1] = self.b12.fonk3(b1, b2)
            self.a1 += 1
        else:
            b13 = self.b12.fonk9()
            del self.b10[b13.b1]
            self.b10[b1] = self.b12.fonk5(b1, b2)
    def fonk15(self, b1):
        b14 = b1 % self.b11
        return b14
    def fonk16(self):
        return self.a1
    def fonk17(self):
        self.b12.fonk10()
if b15 = = "__main__":
    b16 = class4(5)
    b16.fonk14(1, 1)
    b16.fonk14(2, 2)
    b16.fonk14(3, 3)
    b16.fonk14(4, 4)
    b16.fonk14(5, 5)
    b16.fonk13(1)
    b16.fonk14(6, 6)
    b16.fonk14(7, 7)
    b16.fonk13(11)
    b16.fonk17()