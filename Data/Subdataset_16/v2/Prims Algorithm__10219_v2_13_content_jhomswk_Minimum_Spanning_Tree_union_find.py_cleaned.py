class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = self
        self.b3 = self
        self.a1 = 0
    def fonk2(self):
        b4 = []
        b5 = self
        while b5 is not b5.b2:
            b4.append(b5)
            b5 = b5.b2
        b6 = b5
        for element in b4:
            element.b2 = b6
        return b6
    def fonk3(self, other):
        b7 = self.fonk2()
        b8 = other.fonk2()
        if b7 is not b8:
            if b7.a1 < b8.a1:
                b7.b2 = b8
            else:
                b8.b2 = b7
                if b7.a1 = = b8.a1:
                    b7.a1 += 1
            b7.b3, b8.b3 = b8.b3, b7.b3
    def fonk4(self, b1):
        b9 = class1(b1)
        self.fonk3(b9)
    def fonk5(self):
        yield self.b1
        b5 = self.b3
        while b5 != self:
            yield b5.b1
            b5 = b5.b3
    def fonk6(self):
        return "{{{}}}".format(", ".join(map(str, self.fonk5())))
    def fonk7(self):
        return str(self)
if b10 = = "__main__":
    b11 = class1(1)
    b12 = class1(2)
    b13 = class1(3)
    b11.fonk3(b12)
    b12.fonk3(b13)
    b11.fonk4(4)
    print(b11)
    print(b12)
    print(b13)
