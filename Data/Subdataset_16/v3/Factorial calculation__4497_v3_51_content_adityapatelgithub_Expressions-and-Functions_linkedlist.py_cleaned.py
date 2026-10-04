class class1:
    class class2:
        b1 = "b3", "b4"
        def fonk1(self, b9, b2 = None):
            self.b3 = b9
            self.b4 = b2
    def fonk2(self):
        self.b5 = None
        self.b6 = None
        self.a1 = 0
    def fonk3(self):
        b7 = self.b5
        while b7:
            yield b7.b3
            b7 = b7.b4
    def fonk4(self):
        return self.a1
    def fonk5(self):
        return "".join(str(b9) for b9 in self)
    def fonk6(self, b9):
        b8 = self.class2(b9, self.b5)
        if self.a1 = = 0:
            self.b6 = b8
        self.b5 = b8
        self.a1 += 1
    def fonk7(self):
        if self.b5 is None:
            raise IndexError("pop from empty list")
        b9 = self.b5.b3
        self.b5 = self.b5.b4
        self.a1 -= 1
        if self.a1 = = 0:
            self.b6 = None
        return b9
    def fonk8(self):
        if self.b6 is None:
            raise IndexError("top from empty list")
        return self.b6.b3
    def fonk9(self):
        return self.a1 = = 0
if b10 = = "__main__":
    b11 = class1()
    b11.fonk6('a')
    b11.fonk6('b')
    b11.fonk6('c')
    print("List:", str(b11))
    print("Length:", len(b11))
    print("Top:", b11.fonk8())
    print("Pop:", b11.fonk7())
    print("List after pop:", str(b11))
    print("Is empty:", b11.fonk9())
