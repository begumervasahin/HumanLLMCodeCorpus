class class1:
    class class2:
        def fonk1(self, b2, b1 = None):
            self.b2 = b2
            self.b3 = b1
    def fonk2(self):
        self.b4 = None
        self.b5 = None
        self.a1 = 0
    def fonk3(self):
        b6 = self.b4
        while b6:
            yield b6.b2
            b6 = b6.b3
    def fonk4(self):
        return self.a1
    def fonk5(self):
        return "->".join(str(b2) for b2 in self)
    def fonk6(self, b2):
        b7 = self.class2(b2)
        if not self.b4:
            self.b4 = self.b5 = b7
        else:
            self.b5.b3 = b7
            self.b5 = b7
        self.a1 += 1
    def fonk7(self, b2):
        b7 = self.class2(b2, self.b4)
        self.b4 = b7
        if not self.b5:
            self.b5 = b7
        self.a1 += 1
    def fonk8(self):
        if not self.b4:
            raise IndexError("pop from empty list")
        b2 = self.b4.b2
        self.b4 = self.b4.b3
        if not self.b4:
            self.b5 = None
        self.a1 -= 1
        return b2
    def fonk9(self):
        if not self.b4:
            raise IndexError("list is empty")
        return self.b4.b2
    def fonk10(self):
        if not self.b5:
            raise IndexError("list is empty")
        return self.b5.b2
    def fonk11(self):
        return self.a1 = = 0