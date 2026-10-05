class class1:
    def fonk1(self, b1):
        if isinstance(b1, int):
            self.b1 = b1
            self.b2 = None
            self.b3 = None
        elif b1 is None:
            self.b1 = None
            self.b2 = None
            self.b3 = None
        else:
            raise TypeError("Data must be an integer or None.")
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
        b6 += ")"
        return b6
    def fonk5(self, b1):
        if isinstance(b1, int):
            b8 = class1(b1)
            b9 = self.b4.b3
            b8.b2 = self.b4
            b8.b3 = b9
            self.b4.b3 = b8
            b9.b2 = b8
            self.a1 += 1
        else:
            raise TypeError("Data must be an integer.")
    def fonk6(self, b1):
        if isinstance(b1, int):
            b8 = class1(b1)
            b10 = self.b5.b2
            b10.b3 = b8
            b8.b2 = b10
            b8.b3 = self.b5
            self.b5.b2 = b8
            self.a1 += 1
        else:
            raise TypeError("Data must be an integer.")
    def fonk7(self):
        if self.a1 = = 0:
            raise IndexError("Cannot remove from an empty list.")
        b11 = self.b4.b3
        b9 = b11.b3
        self.b4.b3 = b9
        b9.b2 = self.b4
        self.a1 -= 1
        return b11.b1
    def fonk8(self):
        if self.a1 = = 0:
            raise IndexError("Cannot remove from an empty list.")
        b11 = self.b5.b2
        b10 = b11.b2
        b10.b3 = self.b5
        self.b5.b2 = b10
        self.a1 -= 1
        return b11.b1
    def fonk9(self):
        return self.a1
    def fonk10(self):
        if self.a1 = = 0:
            raise IndexError("List is empty.")
        return self.b4.b3.b1
    def fonk11(self, pos):
        if not isinstance(pos, int):
            raise TypeError("Position must be an integer.")
        if not 0 <= pos < self.a1:
            raise IndexError("Position out of range.")
        b7 = self.b4.b3
        for _ in range(pos):
            b7 = b7.b3
        return b7.b1
    def fonk12(self, b1, pos):
        if not isinstance(b1, int):
            raise TypeError("Data must be an integer.")
        if not isinstance(pos, int):
            raise TypeError("Position must be an integer.")
        if not 0 <= pos <= self.a1:
            raise IndexError("Position out of range.")
        b7 = self.b4
        for _ in range(pos):
            b7 = b7.b3
        b8 = class1(b1)
        b9 = b7.b3
        b7.b3 = b8
        b8.b2 = b7
        b8.b3 = b9
        b9.b2 = b8
        self.a1 += 1
    def fonk13(self, pos):
        if not isinstance(pos, int):
            raise TypeError("Position must be an integer.")
        if not 0 <= pos < self.a1:
            raise IndexError("Position out of range.")
        b7 = self.b4
        for _ in range(pos):
            b7 = b7.b3
        b11 = b7.b3
        b9 = b11.b3
        b7.b3 = b9
        b9.b2 = b7
        self.a1 -= 1
        return b11.b1
    def fonk14(self, b1):
        b7 = self.b4.b3
        while b7 != self.b5:
            if b7.b1 = = b1:
                return True
            b7 = b7.b3
        return False
if b12 = = "__main__":
    b13 = class2()
    b13.fonk6(5)
    b13.fonk5(10)
    b13.fonk6(12)
    b13.fonk12(7, 1)
    b13.fonk12(6, 1)
    print(b13.fonk11(2))
    print(b13.fonk13(2))
    print(b13)
    print(b13.fonk9())
    print(b13.fonk14(10))
    print(b13.fonk7())
    print(b13.fonk7())
    print(b13.fonk8())
    print(b13.fonk9())