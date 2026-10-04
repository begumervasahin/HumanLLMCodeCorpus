class class1:
    class class2:
        def fonk1(self, b1, b2):
            self.b1 = b1
            self.b2 = b2
            self.b3 = None
            self.b4 = None
    def fonk2(self):
        self.fonk3()
    def fonk3(self):
        self.b5 = None
        self.a1 = 0
        self.b6 = None
        self.b7 = "pre"
    def fonk4(self, b1, b2):
        self.b5 = self.fonk5(self.b5, b1, b2)
        self.a1 += 1
    def fonk5(self, b9, b1, b2):
        if b9 is None:
            return class1.class2(b1, b2)
        if b1 < b9.b1:
            b9.b3 = self.fonk5(b9.b3, b1, b2)
        else:
            b9.b4 = self.fonk5(b9.b4, b1, b2)
        return b9
    def fonk6(self, b1):
        return self.fonk7(self.b5, b1)
    def fonk7(self, b9, b1):
        if b9 is None:
            return None
        if b1 = = b9.b1:
            return b9.b2
        elif b1 < b9.b1:
            return self.fonk7(b9.b3, b1)
        else:
            return self.fonk7(b9.b4, b1)
    def fonk8(self, b1):
        self.b6 = None
        self.b5 = self.fonk9(self.b5, b1)
        return self.b6
    def fonk9(self, b9, b1):
        if b9 is None:
            return None
        if b1 = = b9.b1:
            self.b6 = b9.b2
            self.a1 -= 1
            if b9.b3 is None and b9.b4 is None:
                return None
            if b9.b4 is None:
                return b9.b3
            if b9.b3 is None:
                return b9.b4
            b8 = self.fonk10(b9.b4)
            b9.b1, b9.b2 = b8.b1, b8.b2
            b9.b4 = self.fonk9(b9.b4, b8.b1)
        elif b1 < b9.b1:
            b9.b3 = self.fonk9(b9.b3, b1)
        else:
            b9.b4 = self.fonk9(b9.b4, b1)
        return b9
    def fonk10(self, b9):
        while b9.b3 is not None:
            b9 = b9.b3
        return b9
    def fonk11(self):
        self.b7 = "pre"
        return self
    def fonk12(self):
        self.b7 = "in"
        return self
    def fonk13(self):
        self.b7 = "post"
        return self
    def fonk14(self):
        return self.fonk15(self.b5)
    def fonk15(self, b9):
        if b9 is None:
            return
        if self.b7 = = "pre":
            yield b9.b2
        if b9.b3 is not None:
            yield from self.fonk15(b9.b3)
        if self.b7 = = "in":
            yield b9.b2
        if b9.b4 is not None:
            yield from self.fonk15(b9.b4)
        if self.b7 = = "post":
            yield b9.b2
    def fonk16(self):
        return self.a1
if b10 = = "__main__":
    b11 = class1()
    b11.fonk4(10, "Value for 10")
    b11.fonk4(5, "Value for 5")
    b11.fonk4(15, "Value for 15")
    b11.fonk4(3, "Value for 3")
    b11.fonk4(7, "Value for 7")
    print("Lookup 10:", b11.fonk6(10))
    print("Lookup 5:", b11.fonk6(5))
    print("Lookup 20:", b11.fonk6(20))
    print("Remove 5:", b11.fonk8(5))
    print("Lookup 5:", b11.fonk6(5))
    print("In-order traversal:")
    for b2 in b11.fonk12():
        print(b2)
    print("Pre-order traversal:")
    for b2 in b11.fonk11():
        print(b2)
    print("Post-order traversal:")
    for b2 in b11.fonk13():
        print(b2)
    print("Number of nodes:", len(b11))
