class class1:
    class class2:
        def fonk1(self, b2, b1 = None, b3=None, b4=1):
            self.b2 = b2
            self.b1 = b1
            self.b3 = b3
            self.b4 = b4
    def fonk2(self):
        self.b5 = None
    def fonk3(self, val):
        self.b5 = self.fonk11(self.b5, val)
    def fonk4(self, val):
        self.b5 = self.fonk12(self.b5, val)
    def fonk5(self, val):
        return self.fonk13(self.b5, val)
    def fonk6(self):
        return self.fonk23(self.b5)
    def fonk7(self):
        return self.fonk17(self.b5)
    def fonk8(self):
        if not self.fonk10():
            return self.fonk14(self.b5).b2
        return None
    def fonk9(self):
        if not self.fonk10():
            return self.fonk15(self.b5).b2
        return None
    def fonk10(self):
        return self.b5 is None
    def fonk11(self, root, val):
        if root is None:
            return class1.class2(val)
        if val < root.b2:
            root.b3 = self.fonk11(root.b3, val)
        elif val > root.b2:
            root.b1 = self.fonk11(root.b1, val)
        return self.fonk22(root)
    def fonk12(self, b6, val):
        if b6 is None:
            return None
        if val < b6.b2:
            b6.b3 = self.fonk12(b6.b3, val)
        elif val > b6.b2:
            b6.b1 = self.fonk12(b6.b1, val)
        else:
            if b6.b3 is None or b6.b1 is None:
                b6 = b6.b3 if b6.b3 else b6.b1
            else:
                b7 = self.fonk14(b6.b1)
                b6.b2 = b7.b2
                b6.b1 = self.fonk16(b6.b1)
        return self.fonk22(b6)
    def fonk13(self, b6, val):
        if b6 is None:
            return False
        if b6.b2 = = val:
            return b6
        elif val < b6.b2:
            return self.fonk13(b6.b3, val)
        else:
            return self.fonk13(b6.b1, val)
    def fonk14(self, b6):
        return b6 if b6.b3 is None else self.fonk14(b6.b3)
    def fonk15(self, b6):
        return b6 if b6.b1 is None else self.fonk15(b6.b1)
    def fonk16(self, b6):
        if b6.b3 is None:
            return b6.b1
        b6.b3 = self.fonk16(b6.b3)
        return self.fonk22(b6)
    def fonk17(self, b6):
        return 0 if b6 is None else b6.b4
    def fonk18(self, b6):
        b6.b4 = fonk9(self.fonk17(b6.b3), self.fonk17(b6.b1)) + 1
    def fonk19(self, b6):
        return self.fonk17(b6.b1) - self.fonk17(b6.b3)
    def fonk20(self, b6):
        b8 = b6.b3
        b6.b3 = b8.b1
        b8.b1 = b6
        self.fonk18(b6)
        self.fonk18(b8)
        return b8
    def fonk21(self, b6):
        b8 = b6.b1
        b6.b1 = b8.b3
        b8.b3 = b6
        self.fonk18(b6)
        self.fonk18(b8)
        return b8
    def fonk22(self, b6):
        self.fonk18(b6)
        if self.fonk19(b6) == 2:
            if self.fonk19(b6.b1) < 0:
                b6.b1 = self.fonk20(b6.b1)
            return self.fonk21(b6)
        if self.fonk19(b6) == -2:
            if self.fonk19(b6.b3) > 0:
                b6.b3 = self.fonk21(b6.b3)
            return self.fonk20(b6)
        return b6
    def fonk23(self, b6):
        if b6 is None:
            return ''
        return f'{b6.b2},{b6.b4}\n' + self.fonk23(b6.b3) + self.fonk23(b6.b1)
if b9 = = '__main__':
    b10 = class1()
    b10.fonk3(10)
    b10.fonk3(20)
    b10.fonk3(5)
    b10.fonk3(6)
    b10.fonk3(15)
    print("class1 Tree:")
    print(b10)
    print("Find 10:", b10.fonk5(10))
    print("Find 25:", b10.fonk5(25))
    print("Min b2:", b10.fonk8())
    print("Max b2:", b10.fonk9())
    b10.fonk4(10)
    print("class1 Tree after removing 10:")
    print(b10)
    print("Tree b4:", b10.fonk7())