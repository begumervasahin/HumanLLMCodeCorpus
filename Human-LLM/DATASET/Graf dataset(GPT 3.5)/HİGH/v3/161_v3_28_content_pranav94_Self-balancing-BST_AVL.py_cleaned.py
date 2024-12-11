class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.a1 = 1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = None
    def fonk3(self, b8):
        b5 = b8.b3
        b8.b3 = b5.b2
        b5.b2 = b8
        self.fonk11(b8)
        self.fonk11(b5)
        return b5
    def fonk4(self, b8):
        b5 = b8.b2
        b8.b2 = b5.b3
        b5.b3 = b8
        self.fonk11(b8)
        self.fonk11(b5)
        return b5
    def fonk5(self, b8):
        b6 = self.fonk13(b8)
        if b6 > 1:
            if self.fonk13(b8.b2) >= 0:
                return self.fonk4(b8)
            b8.b2 = self.fonk3(b8.b2)
            return self.fonk4(b8)
        if b6 < -1:
            if self.fonk13(b8.b3) <= 0:
                return self.fonk3(b8)
            b8.b3 = self.fonk4(b8.b3)
            return self.fonk3(b8)
        return b8
    def fonk6(self, b1):
        self.b4 = self.fonk7(self.b4, b1)
    def fonk7(self, b8, b1):
        if not b8:
            return class1(b1)
        if b1 < b8.b1:
            b8.b2 = self.fonk7(b8.b2, b1)
        else:
            b8.b3 = self.fonk7(b8.b3, b1)
        self.fonk11(b8)
        return self.fonk5(b8)
    def fonk8(self, b1):
        self.b4 = self.fonk9(self.b4, b1)
    def fonk9(self, b8, b1):
        if not b8:
            return None
        if b1 < b8.b1:
            b8.b2 = self.fonk9(b8.b2, b1)
        elif b1 > b8.b1:
            b8.b3 = self.fonk9(b8.b3, b1)
        else:
            if not b8.b2 and not b8.b3:
                return None
            elif not b8.b2:
                return b8.b3
            elif not b8.b3:
                return b8.b2
            else:
                b7 = self.fonk10(b8)
                b8.b1 = b7.b1
                b8.b2 = self.fonk9(b8.b2, b7.b1)
        self.fonk11(b8)
        return self.fonk5(b8)
    def fonk10(self, b8):
        b8 = b8.b2
        while b8.b3:
            b8 = b8.b3
        return b8
    def fonk11(self, b8):
        if b8:
            b8.a1 = 1 + max(self.fonk12(b8.b2), self.fonk12(b8.b3))
    def fonk12(self, b8):
        return b8.a1 if b8 else 0
    def fonk13(self, b8):
        return self.fonk12(b8.b2) - self.fonk12(b8.b3)