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
        return self.b2 is not None and self.b2.b2 is not None
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
        if b5.b3:
            b5 = b5.b3
            while b5.b4:
                b5 = b5.b4
            return b5
        else:
            return None
    def fonk12(self):
        b5 = self
        if b5.b4:
            b5 = b5.b4
            while b5.b3:
                b5 = b5.b3
            return b5
        else:
            return None
    def fonk13(self):
        b5 = self
        if b5.fonk3():
            while b5.fonk3():
                b5 = b5.b2
            if b5.fonk2():
                return b5.b2
            else:
                return None
        else:
            return None
    def fonk14(self):
        b5 = self
        if b5.fonk2():
            while b5.fonk2():
                b5 = b5.b2
            if b5.fonk3():
                return b5.b2
            else:
                return None
        else:
            return None
    def fonk15(self):
        if self.fonk5():
            if self.b4:
                return self.fonk12()
            else:
                return None
        elif self.fonk2():
            if self.b4:
                return self.fonk12()
            else:
                return self.b2
        else:
            if self.b4:
                return self.fonk12()
            else:
                return self.fonk13()
    def fonk16(self):
        if self.fonk5():
            if self.b3:
                return self.fonk11()
            else:
                return None
        elif self.fonk2():
            if self.b3:
                return self.fonk11()
            else:
                return self.fonk14()
        else:
            if self.b3:
                return self.fonk11()
            else:
                return self.b2
class class2:
    def fonk17(self):
        self.b6 = None
        self.a5 = 0
        self.b5 = None
    def fonk18(self, b7):
        b5 = self.b6
        while b5:
            if b5.b7 = = b7:
                return b5
            elif b5.b7 > b7:
                b5 = b5.b3
            else:
                b5 = b5.b4
        return b5
    def fonk19(self, b7):
        if not self.b6:
            self.b6 = class1(b7)
            self.b6.a3 = 0
            self.b6.a2 = 0
            self.a5 = 1
        else:
            b8 = self.b6.fonk19(self, b7)
            if b8:
                b8.bubble_up(self)
    def fonk20(self, b7):
        b9 = self.fonk18(b7)
        if b9:
            b9.fonk20(self)
            self.a5 -= 1
        return b9
    def fonk21(self):
        if self.b6:
            b5 = self.b6
            while b5.b3:
                b5 = b5.b3
            while b5:
                print(b5.b7)
                b5 = b5.fonk15()
    def fonk22(self):
        if self.b6:
            b5 = self.b6
            while b5.b3:
                b5 = b5.b3
            return b5
        else:
            return None
    def fonk23(self):
        if self.b6:
            b5 = self.fonk22()
            a6 = 0
            while b5:
                b5.a4 = a6
                a6 += 1
                b5 = b5.fonk15()
if b10 = = "__main__":
    b11 = class2()
    b11.fonk19(5)
    b11.fonk19(3)
    b11.fonk19(7)
    b11.fonk19(4)
    b11.fonk19(6)
    b11.fonk19(8)
    b11.fonk21()