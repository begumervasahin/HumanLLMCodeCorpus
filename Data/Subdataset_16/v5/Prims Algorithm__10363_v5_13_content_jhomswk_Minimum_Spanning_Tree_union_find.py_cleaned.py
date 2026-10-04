class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = self
        self.b3 = self
        self.a1 = 0
    def fonk2(self):
        if self.b2 != self:
            self.b2 = self.b2.fonk2()
        return self.b2
    def fonk3(self, other):
        b4 = self.fonk2()
        b5 = other.fonk2()
        if b4 != b5:
            if b4.a1 < b5.a1:
                b4.b2 = b5
            elif b4.a1 > b5.a1:
                b5.b2 = b4
            else:
                b5.b2 = b4
                b4.a1 += 1
            b4.b3, b5.b3 = b5.b3, b4.b3
    def fonk4(self, b1):
        b6 = class1(b1)
        self.fonk3(b6)
    def fonk5(self):
        b7 = self
        while True:
            yield b7.b1
            b7 = b7.b3
            if b7 = = self:
                break
    def fonk6(self):
        return "{{{}}}".format(", ".join(map(str, self.fonk5())))
    def fonk7(self):
        return self.fonk6()