class class1:
    class class2:
        def fonk1(self, b2, b1 = None, b3=None, b4=None):
            self.b2 = b2
            self.b1 = b1
            self.b3 = b3
            self.b4 = b4
    def fonk2(self):
        self.b5 = None
    def fonk3(self, val):
        self.b5 = self.fonk22(self.b5, val)
    def fonk4(self, val):
        self.b5 = self.fonk17(self.b5, val)
    def fonk5(self, val):
        return self.fonk11(self.b5, val)
    def fonk6(self):
        return self.fonk23(self.b5)
    def fonk7(self):
        return self.fonk18(self.b5)
    def fonk8(self):
        if not self.fonk12():
            return self.fonk20(self.b5).b2
    def fonk9(self):
        if not self.fonk12():
            return self.fonk10(self.b5).b2
    def fonk10(self, b6):
        while b6.b1 is not None:
            b6 = b6.b1
        return b6
    def fonk11(self, b7, val):
        while b7 is not None:
            if b7.b2 = = val:
                return b7
            elif val < b7.b2:
                b7 = b7.b3
            else:
                b7 = b7.b1
        return False
    def fonk12(self):
        return self.b5 is None
    def fonk13(self, b7):
        b7.b4 = fonk9(self.fonk18(b7.b3), self.fonk18(b7.b1)) + 1
    def fonk14(self, b7):
        return self.fonk18(b7.b1) - self.fonk18(b7.b3)
    def fonk15(self, b7):
        b8 = b7.b3
        b7.b3 = b8.b1
        b8.b1 = b7
        self.fonk13(b7)
        self.fonk13(b8)
        return b8
    def fonk16(self, b7):
        b8 = b7.b1
        b7.b1 = b8.b3
        b8.b3 = b7
        self.fonk13(b7)
        self.fonk13(b8)
        return b8
    def fonk17(self, b6, val):
        if b6 is None:
            b7 = class1.class2(val)
            b7.b4 = 1
            return b7
        if val < b6.b2:
            b6.b3 = self.fonk17(b6.b3, val)
        elif val > b6.b2:
            b6.b1 = self.fonk17(b6.b1, val)
        return self.fonk19(b6)
    def fonk18(self, b7):
        if b7 is None:
            return 0
        else:
            return b7.b4
    def fonk19(self, b7):
        self.fonk13(b7)
        if self.fonk14(b7) == 2:
            if self.fonk14(b7.b1) < 0:
                b7.b1 = self.fonk15(b7.b1)
            return self.fonk16(b7)
        if self.fonk14(b7) == -2:
            if self.fonk14(b7.b1) > 0:
                b7.b3 = self.fonk16(b7.b3)
            return self.fonk15(b7)
        return b7
    def fonk20(self, b6):
        while b6.b3 is not None:
            b6 = b6.b3
        return b6
    def fonk21(self, b7):
        if b7.b3 is None:
            return b7.b1
        b7.b3 = self.fonk21(b7.b3)
        return self.fonk19(b7)
    def fonk22(self, b7, b2):
        if b7 is None:
            return None
        if b2 < b7.b2:
            b7.b3 = self.fonk22(b7.b3, b2)
        elif b2 > b7.b2:
            b7.b1 = self.fonk22(b7.b1, b2)
        else:
            if b7.b3 is None:
                return b7.b1
            elif b7.b1 is None:
                return b7.b3
            else:
                b9 = b7
                b7 = self.fonk20(b9.b1)
                b7.b1 = self.fonk21(b9.b1)
                b7.b3 = b9.b3
        return self.fonk19(b7)
    def fonk23(self, b7):
        if b7 is None:
            return ''
        b10 = ','.join([str(b7.b2), str(b7.b4), '\n'])
        b10 += self.fonk23(b7.b3)
        b10 += self.fonk23(b7.b1)
        return b10