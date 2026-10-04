class class1:
    class class2:
        b1 = "b2", "b3"
        def fonk1(self, v, n):
            self.b2 = v
            self.b3 = n
    def fonk2(self):
        self.b4 = None
        self.b5 = None
        self.a1 = 0
    def fonk3(self):
        b6 = self.b4
        while b6 is not None:
            yield b6.b2
            b6 = b6.b3
    def fonk4(self):
        return self.a1
    def fonk5(self):
        return "".join(list(iter(self)))
    def fonk6(self, b8):
        b7 = self.class2(b8, None)
        if self.b4 is None:
            self.b4 = self.b5 = b7
        else:
            b7.b3 = self.b4
            self.b4 = b7
        self.a1 += 1
    def fonk7(self):
        if self.b4 is None:
            raise IndexError("pop from empty list")
        b8 = self.b4.b2
        self.b4 = self.b4.b3
        self.a1 -= 1
        if self.b4 is None:
            self.b5 = None
        return b8
    def fonk8(self):
        if self.b5 is None:
            raise IndexError("top from empty list")
        return self.b5.b2
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
