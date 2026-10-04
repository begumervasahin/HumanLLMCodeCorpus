class class1:
    class class2:
        b1 = "b3", "b4"
        def fonk1(self, b3, b2 = None):
            self.b3 = b3
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
        return "".join(str(b3) for b3 in self)
    def fonk6(self, b3):
        b8 = self.class2(b3, self.b5)
        self.b5 = b8
        if self.b6 is None:
            self.b6 = b8
        self.a1 += 1
    def fonk7(self):
        if self.b5 is None:
            raise IndexError("pop from empty list")
        b3 = self.b5.b3
        self.b5 = self.b5.b4
        self.a1 -= 1
        if self.b5 is None:
            self.b6 = None
        return b3
    def fonk8(self):
        if self.b6 is None:
            raise IndexError("top from empty list")
        return self.b6.b3
    def fonk9(self):
        return self.a1 = = 0
if b9 = = "__main__":
    b10 = class1()
    b10.fonk6('a')
    b10.fonk6('b')
    b10.fonk6('c')
    print("List:", str(b10))
    print("Length:", len(b10))
    print("Top:", b10.fonk8())
    print("Pop:", b10.fonk7())
    print("List after pop:", str(b10))
    print("Is empty:", b10.fonk9())
