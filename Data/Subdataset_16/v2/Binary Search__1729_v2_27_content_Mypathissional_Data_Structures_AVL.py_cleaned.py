class class1:
    class class2:
        def fonk1(self, b2, b1 = None, b3=None, b4=1):
            self.b2 = b2
            self.b1 = b1
            self.b3 = b3
            self.b4 = b4
    def fonk2(self):
        self.b5 = None
    def fonk3(self, b2):
        self.b5 = self.fonk11(self.b5, b2)
    def fonk4(self, b2):
        self.b5 = self.fonk12(self.b5, b2)
    def fonk5(self, b2):
        return self.fonk13(self.b5, b2)
    def fonk6(self):
        return self.fonk17(self.b5)
    def fonk7(self):
        if not self.fonk9():
            return self.fonk14(self.b5).b2
        return None
    def fonk8(self):
        if not self.fonk9():
            return self.fonk15(self.b5).b2
        return None
    def fonk9(self):
        return self.b5 is None
    def fonk10(self):
        return self.fonk23(self.b5)
    def fonk11(self, b6, b2):
        if b6 is None:
            return class1.class2(b2)
        if b2 < b6.b2:
            b6.b1 = self.fonk11(b6.b1, b2)
        elif b2 > b6.b2:
            b6.b3 = self.fonk11(b6.b3, b2)
        return self.fonk22(b6)
    def fonk12(self, b6, b2):
        if b6 is None:
            return None
        if b2 < b6.b2:
            b6.b1 = self.fonk12(b6.b1, b2)
        elif b2 > b6.b2:
            b6.b3 = self.fonk12(b6.b3, b2)
        else:
            if b6.b1 is None or b6.b3 is None:
                b6 = b6.b1 if b6.b1 else b6.b3
            else:
                b7 = self.fonk14(b6.b3)
                b6.b2 = b7.b2
                b6.b3 = self.fonk16(b6.b3)
        return self.fonk22(b6)
    def fonk13(self, b6, b2):
        if b6 is None:
            return None
        if b2 = = b6.b2:
            return b6
        elif b2 < b6.b2:
            return self.fonk13(b6.b1, b2)
        else:
            return self.fonk13(b6.b3, b2)
    def fonk14(self, b6):
        while b6.b1 is not None:
            b6 = b6.b1
        return b6
    def fonk15(self, b6):
        while b6.b3 is not None:
            b6 = b6.b3
        return b6
    def fonk16(self, b6):
        if b6.b1 is None:
            return b6.b3
        b6.b1 = self.fonk16(b6.b1)
        return self.fonk22(b6)
    def fonk17(self, b6):
        return b6.b4 if b6 else 0
    def fonk18(self, b6):
        b6.b4 = fonk8(self.fonk17(b6.b1), self.fonk17(b6.b3)) + 1
    def fonk19(self, b6):
        return self.fonk17(b6.b3) - self.fonk17(b6.b1)
    def fonk20(self, b6):
        b8 = b6.b1
        b6.b1 = b8.b3
        b8.b3 = b6
        self.fonk18(b6)
        self.fonk18(b8)
        return b8
    def fonk21(self, b6):
        b8 = b6.b3
        b6.b3 = b8.b1
        b8.b1 = b6
        self.fonk18(b6)
        self.fonk18(b8)
        return b8
    def fonk22(self, b6):
        self.fonk18(b6)
        if self.fonk19(b6) == 2:
            if self.fonk19(b6.b3) < 0:
                b6.b3 = self.fonk20(b6.b3)
            return self.fonk21(b6)
        if self.fonk19(b6) == -2:
            if self.fonk19(b6.b1) > 0:
                b6.b1 = self.fonk21(b6.b1)
            return self.fonk20(b6)
        return b6
    def fonk23(self, b6):
        if b6 is None:
            return ''
        b9 = f'{b6.b2},{b6.b4}\n'
        b9 += self.fonk23(b6.b1)
        b9 += self.fonk23(b6.b3)
        return b9
if b10 = = "__main__":
    b11 = class1()
    b12 = [10, 20, 30, 40, 50, 25]
    for val in b12:
        b11.fonk3(val)
    print("class1 Tree:")
    print(b11)
    print("Find b6 with b2 20:")
    b6 = b11.fonk5(20)
    print(b6.b2 if b6 else "Not found")
    print("Minimum b2 in class1 Tree:")
    print(b11.fonk7())
    print("Maximum b2 in class1 Tree:")
    print(b11.fonk8())
    print("Removing b6 with b2 10:")
    b11.fonk4(10)
    print(b11)
    print("Tree b4:")
    print(b11.fonk6())