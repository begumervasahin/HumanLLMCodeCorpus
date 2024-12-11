class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.a1 = 0
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = None
    def fonk3(self, b10):
        b5 = b10.b3
        b6 = b5.b2
        b5.b2 = b10
        b10.b3 = b6
        self.fonk10(b10)
        self.fonk10(b5)
        return b5
    def fonk4(self, b10):
        b5 = b10.b2
        b7 = b5.b3
        b5.b3 = b10
        b10.b2 = b7
        self.fonk10(b10)
        self.fonk10(b5)
        return b5
    def fonk5(self, b10):
        b8 = self.fonk12(b10)
        if b8 > 1:
            if self.fonk12(b10.b2) >= 0:
                return self.fonk4(b10)
            b10.b2 = self.fonk3(b10.b2)
            return self.fonk4(b10)
        if b8 < -1:
            if self.fonk12(b10.b3) <= 0:
                return self.fonk3(b10)
            b10.b3 = self.fonk4(b10.b3)
            return self.fonk3(b10)
        return b10
    def fonk6(self, b10, b1):
        if not b10:
            return class1(b1)
        if b1 < b10.b1:
            b10.b2 = self.fonk6(b10.b2, b1)
        else:
            b10.b3 = self.fonk6(b10.b3, b1)
        self.fonk10(b10)
        return self.fonk5(b10)
    def fonk7(self, b1):
        self.b4 = self.fonk6(self.b4, b1)
    def fonk8(self, b10, b1):
        if not b10:
            return None
        if b1 < b10.b1:
            b10.b2 = self.fonk8(b10.b2, b1)
        elif b1 > b10.b1:
            b10.b3 = self.fonk8(b10.b3, b1)
        else:
            if not b10.b2 and not b10.b3:
                return None
            elif not b10.b2:
                return b10.b3
            elif not b10.b3:
                return b10.b2
            else:
                b9 = self.fonk13(b10)
                b10.b1 = b9.b1
                b10.b2 = self.fonk8(b10.b2, b9.b1)
        self.fonk10(b10)
        return self.fonk5(b10)
    def fonk9(self, b1):
        self.b4 = self.fonk8(self.b4, b1)
    def fonk10(self, b10):
        if not b10:
            return 0
        b10.a1 = 1 + max(self.fonk11(b10.b2), self.fonk11(b10.b3))
    @staticmethod
    def fonk11(b10):
        if not b10:
            return 0
        return b10.a1
    def fonk12(self, b10):
        if not b10:
            return 0
        return self.fonk11(b10.b2) - self.fonk11(b10.b3)
    def fonk13(self, b10):
        b10 = b10.b2
        while b10.b3:
            b10 = b10.b3
        return b10