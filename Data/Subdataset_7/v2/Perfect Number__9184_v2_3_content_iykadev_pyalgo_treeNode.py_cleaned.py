class class1:
    def fonk1(self, b2, b3, b1 = None, right=None, b6=None):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b1
        self.b5 = right
        self.b6 = b6
    def fonk2(self):
        return self.b4
    def fonk3(self):
        return self.b5
    def fonk4(self):
        return self.b6 and self.b6.b4 = = self
    def fonk5(self):
        return self.b6 and self.b6.b5 = = self
    def fonk6(self):
        return not self.b6
    def fonk7(self):
        return not (self.b5 or self.b4)
    def fonk8(self):
        return self.b5 or self.b4
    def fonk9(self):
        return self.b5 and self.b4
    def fonk10(self, b2, b3, b4, b5):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        if self.fonk2():
            self.b4.b6 = self
        if self.fonk3():
            self.b5.b6 = self
class class2:
    def fonk11(self):
        self.b7 = None
        self.a1 = 0
    def fonk12(self):
        return self.a1
    def fonk13(self):
        return self.a1
    def fonk14(self, b2, b3):
        if self.b7:
            self.fonk15(b2, b3, self.b7)
        else:
            self.b7 = class1(b2, b3)
        self.a1 += 1
    def fonk15(self, b2, b3, b11):
        if b2 < b11.b2:
            if b11.fonk2():
                self.fonk15(b2, b3, b11.b4)
            else:
                b11.b4 = class1(b2, b3, b6=b11)
        else:
            if b11.fonk3():
                self.fonk15(b2, b3, b11.b5)
            else:
                b11.b5 = class1(b2, b3, b6=b11)
    def fonk16(self, b2, b3):
        self.fonk14(b2, b3)
    def fonk17(self, b2):
        if self.b7:
            b8 = self.fonk18(b2, self.b7)
            if b8:
                return b8.b3
            else:
                return None
        else:
            return None
    def fonk18(self, b2, b11):
        if not b11:
            return None
        elif b11.b2 = = b2:
            return b11
        elif b2 < b11.b2:
            return self.fonk18(b2, b11.b4)
        else:
            return self.fonk18(b2, b11.b5)
    def fonk19(self, b2):
        return self.fonk17(b2)
    def fonk20(self, b2):
        return bool(self.fonk18(b2, self.b7))
    def fonk21(self, b2):
        if self.a1 > 1:
            b9 = self.fonk18(b2, self.b7)
            if b9:
                self.fonk25(b9)
                self.a1 -= 1
            else:
                raise KeyError('Error, b2 not in tree')
        elif self.a1 = = 1 and self.b7.b2 == b2:
            self.b7 = None
            self.a1 -= 1
        else:
            raise KeyError('Error, b2 not in tree')
    def fonk22(self, b2):
        self.fonk21(b2)
    def fonk23(self, b11):
        b10 = None
        if b11.fonk3():
            b10 = b11.b5.fonk24()
        else:
            if b11.b6:
                if b11.fonk4():
                    b10 = b11.b6
                else:
                    b11.b6.b5 = None
                    b10 = b11.b6.fonk23()
                    b11.b6.b5 = b11
        return b10
    def fonk24(self, b11):
        while b11.fonk2():
            b11 = b11.b4
        return b11
    def fonk25(self, b11):
        if b11.fonk7():
            if b11.fonk4():
                b11.b6.b4 = None
            else:
                b11.b6.b5 = None
        elif b11.fonk9():
            b10 = b11.fonk23()
            b10.fonk26()
            b11.b2 = b10.b2
            b11.b3 = b10.b3
        else:
            if b11.fonk2():
                if b11.fonk4():
                    b11.b4.b6 = b11.b6
                    b11.b6.b4 = b11.b4
                elif b11.fonk5():
                    b11.b4.b6 = b11.b6
                    b11.b6.b5 = b11.b4
                else:
                    b11.fonk10(
                        b11.b4.b2,
                        b11.b4.b3,
                        b11.b4.b4,
                        b11.b4.b5)
            else:
                if b11.fonk4():
                    b11.b5.b6 = b11.b6
                    b11.b6.b4 = b11.b5
                elif b11.fonk5():
                    b11.b5.b6 = b11.b6
                    b11.b6.b5 = b11.b5
                else:
                    b11.fonk10(
                        b11.b5.b2,
                        b11.b5.b3,
                        b11.b5.b4,
                        b11.b5.b5)
    def fonk26(self, b11):
        if b11.fonk7():
            if b11.fonk4():
                b11.b6.b4 = None
            else:
                b11.b6.b5 = None
        elif b11.fonk8():
            if b11.fonk2():
                if b11.fonk4():
                    b11.b6.b4 = b11.b4
                else:
                    b11.b6.b5 = b11.b4
                b11.b4.b6 = b11.b6
            else:
                if b11.fonk4():
                    b11.b6.b4 = b11.b5
                else:
                    b11.b6.b5 = b11.b5
                b11.b5.b6 = b11.b6
b12 = class2()
b12[3] = "red"
b12[4] = "blue"
b12[6] = "yellow"
b12[2] = "at"
print(b12[6])
print(b12[2])