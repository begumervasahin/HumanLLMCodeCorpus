class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.a1 = 1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self, b4 = None):
        self.b4 = b4
    def fonk3(self, b1):
        return self.fonk9(self.b4, b1)
    def fonk4(self, b1):
        if not self.b4:
            self.b4 = class1(b1)
        else:
            self.fonk8(self.b4, b1)
    def fonk5(self):
        self.fonk12(self.b4)
    def fonk6(self):
        return self.fonk10(self.b4)
    def fonk7(self):
        return self.fonk11(self.b4)
    def fonk8(self, b4, b1):
        if b4.b1 = = b1:
            b4.a1 += 1
        elif b1 < b4.b1:
            if b4.b2 is None:
                b4.b2 = class1(b1)
            else:
                self.fonk8(b4.b2, b1)
        else:
            if b4.b3 is None:
                b4.b3 = class1(b1)
            else:
                self.fonk8(b4.b3, b1)
    def fonk9(self, b4, b1):
        if b4 is None:
            return 0
        if b4.b1 = = b1:
            return b4.a1
        elif b1 < b4.b1:
            return self.fonk9(b4.b2, b1)
        else:
            return self.fonk9(b4.b3, b1)
    def fonk10(self, b4):
        if b4 is None:
            return 0
        return 1 + self.fonk10(b4.b2) + self.fonk10(b4.b3)
    def fonk11(self, b4):
        if b4 is None:
            return 0
        b5 = self.fonk11(b4.b2)
        b6 = self.fonk11(b4.b3)
        return max(b5, b6) + 1
    def fonk12(self, b4):
        if b4 is None:
            return
        self.fonk12(b4.b2)
        print(f"{b4.b1}: {b4.a1}")
        self.fonk12(b4.b3)
