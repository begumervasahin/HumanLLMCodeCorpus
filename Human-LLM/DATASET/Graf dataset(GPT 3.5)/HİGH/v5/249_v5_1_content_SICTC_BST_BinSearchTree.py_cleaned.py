class class1:
    class class2:
        def fonk1(self, b1, b2):
            self.b1 = b1
            self.b2 = b2
            self.b3 = None
            self.b4 = None
    def fonk2(self):
        self.b5 = None
        self.a1 = 0
        self.b6 = None
        self.b7 = "pre"
    def fonk3(self, b1, b2):
        self.b5 = self.fonk11(self.b5, b1, b2)
        self.a1 += 1
    def fonk4(self, b1):
        return self.fonk12(self.b5, b1)
    def fonk5(self, b1):
        self.b6 = None
        self.b5 = self.fonk13(self.b5, b1)
        return self.b6
    def fonk6(self):
        self.b7 = "pre"
        return self
    def fonk7(self):
        self.b7 = "in"
        return self
    def fonk8(self):
        self.b7 = "post"
        return self
    def fonk9(self):
        return self.fonk14(self.b5)
    def fonk10(self):
        return self.a1
    def fonk11(self, b10, b1, b2):
        if not b10:
            return class1.class2(b1, b2)
        if b1 < b10.b1:
            b10.b3 = self.fonk11(b10.b3, b1, b2)
        else:
            b10.b4 = self.fonk11(b10.b4, b1, b2)
        return b10
    def fonk12(self, b10, b1):
        if not b10:
            return None
        if b1 = = b10.b1:
            return b10.b2
        if b1 < b10.b1:
            return self.fonk12(b10.b3, b1)
        else:
            return self.fonk12(b10.b4, b1)
    def fonk13(self, b10, b1):
        if not b10:
            return None
        if b1 = = b10.b1:
            if not b10.b3 and not b10.b4:
                self.b6 = b10.b2
                self.a1 -= 1
                return None
            if not b10.b4:
                self.b6 = b10.b2
                self.a1 -= 1
                return b10.b3
            if not b10.b3:
                self.b6 = b10.b2
                self.a1 -= 1
                return b10.b4
            b8 = self.fonk15(b10.b4)
            b9 = b10.b2
            b10.b1 = b8.b1
            b10.b2 = b8.b2
            b10.b4 = self.fonk13(b10.b4, b8.b1)
            self.b6 = b9
            return b10
        if b1 < b10.b1:
            b10.b3 = self.fonk13(b10.b3, b1)
        else:
            b10.b4 = self.fonk13(b10.b4, b1)
        return b10
    def fonk14(self, b10):
        if self.b7 = = "pre":
            yield b10.b2
        if b10.b3:
            for element in self.fonk14(b10.b3):
                yield element
        if self.b7 = = "in":
            yield b10.b2
        if b10.b4:
            for element in self.fonk14(b10.b4):
                yield element
        if self.b7 = = "post":
            yield b10.b2
    def fonk15(self, b10):
        while b10.b3:
            b10 = b10.b3
        return b10