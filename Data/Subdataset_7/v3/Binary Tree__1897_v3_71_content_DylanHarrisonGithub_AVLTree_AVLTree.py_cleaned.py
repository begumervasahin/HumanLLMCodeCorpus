class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.a1 = 1
        self.a2 = 0
        self.a3 = 0
        self.a4 = -1
        self.b2 = None
        self.b3 = None
        self.b4 = None
    def fonk2(self):
        return self.b2 is not None and self.b2.b3 = = self
    def fonk3(self):
        return self.b2 is not None and self.b2.b4 = = self
    def fonk4(self):
        return self.b3 is None and self.b4 is None
    def fonk5(self):
        return self.b2 is None
    def fonk6(self):
        return self.b2 and self.b2.b2
    def fonk7(self):
        return self.b3.a3 if self.b3 else -1
    def fonk8(self):
        return self.b4.a3 if self.b4 else -1
    def fonk9(self):
        return max(self.fonk7(), self.fonk8())
    def fonk10(self):
        return abs(self.fonk8() - self.fonk7()) <= 1
    def fonk11(self):
        b5 = self
        while b5.b3:
            b5 = b5.b3
        return b5 if b5 != self else None
    def fonk12(self):
        b5 = self
        while b5.b4:
            b5 = b5.b4
        return b5 if b5 != self else None
    def fonk13(self):
        b5 = self
        while b5.fonk3():
            b5 = b5.b2
        if b5.fonk2():
            return b5.b2
        return None
    def fonk14(self):
        b5 = self
        while b5.fonk2():
            b5 = b5.b2
        if b5.fonk3():
            return b5.b2
        return None
    def fonk15(self):
        if self.fonk5():
            return self.fonk12() if self.b4 else None
        if self.fonk2():
            return self.fonk12() if self.b4 else self.b2
        return self.fonk12() or self.fonk13()
    def fonk16(self):
        if self.fonk5():
            return self.fonk11() if self.b3 else None
        if self.fonk2():
            return self.fonk11() if self.b3 else self.fonk14()
        return self.fonk11() or self.b2
class class2:
    def fonk17(self):
        self.b6 = None
        self.a5 = 0
    def fonk18(self, b1):
        b5 = self.b6
        while b5:
            if b5.b1 = = b1:
                return b5
            b5 = b5.b3 if b5.b1 > b1 else b5.b4
        return None
    def fonk19(self, b1):
        if not self.b6:
            self.b6 = class1(b1)
            self.b6.a3 = 0
            self.b6.a2 = 0
            self.a5 = 1
        else:
            b7 = self.b6.fonk19(self, b1)
            if b7:
                b7.bubble_up(self)
    def fonk20(self, b1):
        b8 = self.fonk18(b1)
        if b8:
            b8.fonk20(self)
            self.a5 -= 1
        return b8
    def fonk21(self):
        b5 = self.b6
        while b5:
            print(b5.b1)
            b5 = b5.fonk15()
    def fonk22(self):
        b5 = self.b6
        while b5.b3:
            b5 = b5.b3
        return b5
    def fonk23(self):
        b5 = self.fonk22()
        a6 = 0
        while b5:
            b5.a4 = a6
            a6 += 1
            b5 = b5.fonk15()
if b9 = = "__main__":
    b10 = class2()
    for key in [5, 3, 7, 4, 6, 8]:
        b10.fonk19(key)
    b10.fonk21()