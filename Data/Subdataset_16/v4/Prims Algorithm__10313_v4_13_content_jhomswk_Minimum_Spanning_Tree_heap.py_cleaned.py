class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        return f"({self.b1}, {self.b2})"
class class2:
    def fonk3(self):
        self.b3 = []
        self.b4 = {}
    def fonk4(self, b2):
        return self.b3[self.b4[b2]].b1
    def fonk5(self, b9):
        return 2 * b9 + 1
    def fonk6(self, b9):
        return 2 * (b9 + 1)
    def fonk7(self, b9):
        return (b9 - 1)
    def fonk8(self, b9):
        b5 = self.fonk5(b9)
        b6 = self.fonk6(b9)
        b7 = b9
        if b5 < len(self) and self.b3[b5].b1 < self.b3[b7].b1:
            b7 = b5
        if b6 < len(self) and self.b3[b6].b1 < self.b3[b7].b1:
            b7 = b6
        if b7 != b9:
            self.fonk12(b9, b7)
            self.fonk8(b7)
    def fonk9(self):
        if not self:
            return None
        self.fonk12(0, len(self) - 1)
        b8 = self.b3.pop()
        del self.b4[b8.b2]
        self.fonk8(0)
        return (b8.b1, b8.b2)
    def fonk10(self, b1, b2):
        self.b3.append(class1(b1, b2))
        self.b4[b2] = len(self) - 1
        self.fonk11(b2, b1)
    def fonk11(self, b2, b1):
        b9 = self.b4[b2]
        self.b3[b9].b1 = b1
        b10 = self.fonk7(b9)
        while b9 > 0 and self.b3[b9].b1 < self.b3[b10].b1:
            self.fonk12(b9, b10)
            b9, b10 = b10, self.fonk7(b10)
    def fonk12(self, b9, j):
        self.b4[self.b3[b9].b2], self.b4[self.b3[j].b2] = j, b9
        self.b3[b9], self.b3[j] = self.b3[j], self.b3[b9]
    def fonk13(self):
        return len(self.b3)
    def fonk14(self):
        return len(self.b3) > 0
    def fonk15(self, b2):
        return b2 in self.b4