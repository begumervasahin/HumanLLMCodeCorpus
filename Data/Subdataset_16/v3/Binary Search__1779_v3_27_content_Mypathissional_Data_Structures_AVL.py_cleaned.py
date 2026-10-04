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
    def fonk11(self, b7, b2):
        if b7 is None:
            return class1.class2(b2)
        if b2 < b7.b2:
            b7.b1 = self.fonk11(b7.b1, b2)
        elif b2 > b7.b2:
            b7.b3 = self.fonk11(b7.b3, b2)
        else:
            return b7
        return self.fonk22(b7)
    def fonk12(self, b7, b2):
        if b7 is None:
            return None
        if b2 < b7.b2:
            b7.b1 = self.fonk12(b7.b1, b2)
        elif b2 > b7.b2:
            b7.b3 = self.fonk12(b7.b3, b2)
        else:
            if b7.b1 is None or b7.b3 is None:
                return b7.b1 if b7.b1 else b7.b3
            else:
                b6 = self.fonk14(b7.b3)
                b7.b2 = b6.b2
                b7.b3 = self.fonk16(b7.b3)
        return self.fonk22(b7)
    def fonk13(self, b7, b2):
        if b7 is None or b7.b2 = = b2:
            return b7
        if b2 < b7.b2:
            return self.fonk13(b7.b1, b2)
        else:
            return self.fonk13(b7.b3, b2)
    def fonk14(self, b7):
        while b7.b1 is not None:
            b7 = b7.b1
        return b7
    def fonk15(self, b7):
        while b7.b3 is not None:
            b7 = b7.b3
        return b7
    def fonk16(self, b7):
        if b7.b1 is None:
            return b7.b3
        b7.b1 = self.fonk16(b7.b1)
        return self.fonk22(b7)
    def fonk17(self, b7):
        return b7.b4 if b7 else 0
    def fonk18(self, b7):
        b7.b4 = fonk8(self.fonk17(b7.b1), self.fonk17(b7.b3)) + 1
    def fonk19(self, b7):
        return self.fonk17(b7.b3) - self.fonk17(b7.b1)
    def fonk20(self, b7):
        b8 = b7.b1
        b7.b1 = b8.b3
        b8.b3 = b7
        self.fonk18(b7)
        self.fonk18(b8)
        return b8
    def fonk21(self, b7):
        b8 = b7.b3
        b7.b3 = b8.b1
        b8.b1 = b7
        self.fonk18(b7)
        self.fonk18(b8)
        return b8
    def fonk22(self, b7):
        self.fonk18(b7)
        if self.fonk19(b7) == 2:
            if self.fonk19(b7.b3) < 0:
                b7.b3 = self.fonk20(b7.b3)
            return self.fonk21(b7)
        if self.fonk19(b7) == -2:
            if self.fonk19(b7.b1) > 0:
                b7.b1 = self.fonk21(b7.b1)
            return self.fonk20(b7)
        return b7
    def fonk23(self, b7):
        if b7 is None:
            return ''
        b9 = f'{b7.b2},{b7.b4}\n'
        b9 += self.fonk23(b7.b1)
        b9 += self.fonk23(b7.b3)
        return b9
if b10 = = "__main__":
    b11 = class1()
    b12 = [10, 20, 30, 40, 50, 25]
    for val in b12:
        b11.fonk3(val)
    print("AVL Tree:")
    print(b11)
    print("Find b7 with b2 20:")
    b7 = b11.fonk5(20)
    print(b7.b2 if b7 else "Not found")
    print("Minimum b2 in AVL Tree:")
    print(b11.fonk7())
    print("Maximum b2 in AVL Tree:")
    print(b11.fonk8())
    print("Removing b7 with b2 10:")
    b11.fonk4(10)
    print(b11)
    print("Tree b4:")
    print(b11.fonk6())