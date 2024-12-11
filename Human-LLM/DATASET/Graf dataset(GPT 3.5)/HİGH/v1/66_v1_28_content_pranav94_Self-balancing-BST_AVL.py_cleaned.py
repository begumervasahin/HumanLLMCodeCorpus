class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.a1 = 0
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = None
    def fonk3(self, b11):
        b5 = b11.b3
        b6 = b5.b2
        b5.b2 = b11
        b11.b3 = b6
        self.fonk10(b11)
        self.fonk10(b5)
        return b5
    def fonk4(self, b11):
        b5 = b11.b2
        b7 = b5.b3
        b5.b3 = b11
        b11.b2 = b7
        self.fonk10(b11)
        self.fonk10(b5)
        return b5
    def fonk5(self, b11):
        b8 = self.fonk12(b11)
        if b8 > 1:
            if self.fonk12(b11.b2) >= 0:
                return self.fonk4(b11)
            b11.b2 = self.fonk3(b11.b2)
            return self.fonk4(b11)
        if b8 < -1:
            if self.fonk12(b11.b3) <= 0:
                return self.fonk3(b11)
            b11.b3 = self.fonk4(b11.b3)
            return self.fonk3(b11)
        return b11
    def fonk6(self, b11, b1):
        if not b11:
            return class1(b1)
        if b1 < b11.b1:
            b11.b2 = self.fonk6(b11.b2, b1)
        else:
            b11.b3 = self.fonk6(b11.b3, b1)
        self.fonk10(b11)
        return self.fonk5(b11)
    def fonk7(self, b1):
        self.b4 = self.fonk6(self.b4, b1)
    def fonk8(self, b11, b1):
        if not b11:
            return None
        if b1 < b11.b1:
            b11.b2 = self.fonk8(b11.b2, b1)
        elif b1 > b11.b1:
            b11.b3 = self.fonk8(b11.b3, b1)
        else:
            if not b11.b2 and not b11.b3:
                return None
            elif not b11.b2:
                if b11.b3:
                    b11.b1 = b11.b3.b1
                return b11.b3
            elif not b11.b3:
                return b11.b2
            else:
                b9 = self.fonk13(b11)
                b10 = b9.b1
                b11.b2 = self.fonk8(b11.b2, b10)
                b11.b1 = b10
        self.fonk10(b11)
        return self.fonk5(b11)
    def fonk9(self,  b1):
        self.b4 = self.fonk8(self.b4, b1)
    def fonk10(self, b11):
        b11.a1 = 1 + max(self.fonk11(b11.b2), self.fonk11(b11.b3))
    @staticmethod
    def fonk11(b11):
        if not b11:
            return 0
        return b11.a1
    def fonk12(self, b11):
        if not b11:
            return 0
        return self.fonk11(b11.b2) - self.fonk11(b11.b3)
    def fonk13(self, b11):
        b11 = b11.b2
        while b11.b3:
            b11 = b11.b3
        return b11