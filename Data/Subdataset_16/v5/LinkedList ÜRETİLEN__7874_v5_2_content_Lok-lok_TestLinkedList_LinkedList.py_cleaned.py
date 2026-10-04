
class class1:
    def fonk1(self, b1):
        if isinstance(b1, int) or b1 is None:
            self.b1 = b1
            self.b2 = None
            self.b3 = None
        else:
            raise TypeError("Input must be an int or None")
    def fonk2(self):
        return str(self.b1)
class class2:
    def fonk3(self):
        self.b4 = class1(None)
        self.b5 = class1(None)
        self.b4.b3 = self.b5
        self.b5.b2 = self.b4
        self.a1 = 0
    def fonk4(self):
        b6 = "("
        b7 = self.b4.b3
        while b7 != self.b5:
            b6 += str(b7.b1) + " "
            b7 = b7.b3
        b6 = b6.strip() + ")"
        return b6
    def fonk5(self, b1):
        self.fonk16(b1)
        b8 = class1(b1)
        b8.b3 = self.b4.b3
        b8.b2 = self.b4
        self.b4.b3.b2 = b8
        self.b4.b3 = b8
        self.a1 += 1
    def fonk6(self, b1):
        self.fonk16(b1)
        b8 = class1(b1)
        b8.b2 = self.b5.b2
        b8.b3 = self.b5
        self.b5.b2.b3 = b8
        self.b5.b2 = b8
        self.a1 += 1
    def fonk7(self):
        self.fonk17()
        b9 = self.b4.b3
        self.b4.b3 = b9.b3
        b9.b3.b2 = self.b4
        self.a1 -= 1
        return b9.b1
    def fonk8(self):
        self.fonk17()
        b10 = self.b5.b2
        self.b5.b2 = b10.b2
        b10.b2.b3 = self.b5
        self.a1 -= 1
        return b10.b1
    def fonk9(self):
        return self.a1
    def fonk10(self):
        self.fonk17()
        return self.b4.b3.b1
    def fonk11(self, pos):
        self.fonk18(pos)
        b7 = self.b4.b3
        for _ in range(pos):
            b7 = b7.b3
        return b7.b1
    def fonk12(self, b1, pos):
        self.fonk16(b1)
        self.fonk19(pos)
        b7 = self.b4
        for _ in range(pos):
            b7 = b7.b3
        b8 = class1(b1)
        b8.b2 = b7
        b8.b3 = b7.b3
        b7.b3.b2 = b8
        b7.b3 = b8
        self.a1 += 1
    def fonk13(self, pos):
        self.fonk18(pos)
        b7 = self.b4.b3
        for _ in range(pos):
            b7 = b7.b3
        b7.b2.b3 = b7.b3
        b7.b3.b2 = b7.b2
        self.a1 -= 1
        return b7.b1
    def fonk14(self, b1):
        self.fonk16(b1)
        a2 = 0
        b7 = self.b4.b3
        while b7 != self.b5:
            if b7.b1 = = b1:
                a2 += 1
            b7 = b7.b3
        return a2
    def fonk15(self):
        return self.a1 = = 0
    def fonk16(self, b1):
        if not isinstance(b1, int):
            raise TypeError("Input must be an int")
    def fonk17(self):
        if self.fonk15():
            raise IndexError("Operation on empty list")
    def fonk18(self, pos):
        if not isinstance(pos, int):
            raise TypeError("Position must be an int")
        if pos < 0 or pos >= self.a1:
            raise IndexError("Position out of range")
    def fonk19(self, pos):
        if not isinstance(pos, int):
            raise TypeError("Position must be an int")
        if pos < 0 or pos > self.a1:
            raise IndexError("Position out of range")
if b11 = = "__main__":
    b12 = class2()
    b12.fonk6(5)
    b12.fonk5(10)
    b12.fonk6(12)
    b12.fonk12(7, 1)
    b12.fonk12(6, 1)
    print(b12.fonk11(2))
    print(b12.fonk13(2))
    print(b12)
    print(b12.fonk9())
    print(b12.fonk14(10))
    print(b12.fonk7())
    print(b12.fonk7())
    print(b12.fonk8())
    print(b12.fonk9())
