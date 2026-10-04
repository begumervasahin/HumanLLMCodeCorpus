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
        self.b5 = self.fonk22(self.b5, val)
    def fonk4(self, val):
        self.b5 = self.fonk17(self.b5, val)
    def fonk5(self, val):
        return self.fonk11(self.b5, val)
    def fonk6(self):
        return self.fonk23(self.b5)
    def fonk7(self):
        return self.fonk18(self.b5)
    def fonk8(self):
        if not self.fonk12():
            return self.fonk20(self.b5).b2
    def fonk9(self):
        if not self.fonk12():
            return self.fonk10(self.b5).b2
    def fonk10(self, root):
        if root.b1 is None:
            return root
        else:
            return self.fonk10(root.b1)
    def fonk11(self, b7, val):
        if b7 is None:
            return False
        if b7.b2 = = val:
            return b7
        elif val < b7.b2:
            return self.fonk11(b7.b3, val)
        else:
            return self.fonk11(b7.b1, val)
    def fonk12(self):
        return self.b5 is None
    def fonk13(self, b7):
        b7.b4 = fonk9(self.fonk18(b7.b3), self.fonk18(b7.b1)) + 1
    def fonk14(self, b7):
        return self.fonk18(b7.b1) - self.fonk18(b7.b3)
    def fonk15(self, b7):
        b6 = b7.b3
        b7.b3 = b6.b1
        b6.b1 = b7
        self.fonk13(b7)
        self.fonk13(b6)
        return b6
    def fonk16(self, b7):
        b6 = b7.b1
        b7.b1 = b6.b3
        b6.b3 = b7
        self.fonk13(b7)
        self.fonk13(b6)
        return b6
    def fonk17(self, root, val):
        if root is None:
            return class1.class2(val)
        if val < root.b2:
            root.b3 = self.fonk17(root.b3, val)
        elif val > root.b2:
            root.b1 = self.fonk17(root.b1, val)
        return self.fonk19(root)
    def fonk18(self, b7):
        if b7 is None:
            return 0
        else:
            return b7.b4
    def fonk19(self, b7):
        self.fonk13(b7)
        if self.fonk14(b7) == 2:
            if self.fonk14(b7.b1) < 0:
                b7.b1 = self.fonk15(b7.b1)
            return self.fonk16(b7)
        if self.fonk14(b7) == -2:
            if self.fonk14(b7.b3) > 0:
                b7.b3 = self.fonk16(b7.b3)
            return self.fonk15(b7)
        return b7
    def fonk20(self, root):
        if root.b3 is None:
            return root
        else:
            return self.fonk20(root.b3)
    def fonk21(self, b7):
        if b7.b3 is None:
            return b7.b1
        b7.b3 = self.fonk21(b7.b3)
        return self.fonk19(b7)
    def fonk22(self, b7, b2):
        if b7 is not None:
            if b2 < b7.b2:
                b7.b3 = self.fonk22(b7.b3, b2)
            elif b2 > b7.b2:
                b7.b1 = self.fonk22(b7.b1, b2)
            else:
                if b7.b3 is None or b7.b1 is None:
                    b7 = b7.b3 if b7.b3 else b7.b1
                else:
                    b8 = self.fonk20(b7.b1)
                    b7.b2 = b8.b2
                    b7.b1 = self.fonk21(b7.b1)
            return self.fonk19(b7)
        return None
    def fonk23(self, b7):
        if b7 is None:
            return ''
        b9 = f'{b7.b2},{b7.b4}\n'
        b9 += self.fonk23(b7.b3)
        b9 += self.fonk23(b7.b1)
        return b9
if b10 = = "__main__":
    b11 = class1()
    b11.fonk4(10)
    b11.fonk4(20)
    b11.fonk4(30)
    b11.fonk4(40)
    b11.fonk4(50)
    b11.fonk4(25)
    print("class1 Tree:")
    print(b11)
    print("Find b7 with b2 20:")
    b7 = b11.fonk5(20)
    print(b7.b2 if b7 else "Not found")
    print("Minimum b2 in class1 Tree:")
    print(b11.fonk8())
    print("Maximum b2 in class1 Tree:")
    print(b11.fonk9())
    print("Removing b7 with b2 10:")
    b11.fonk3(10)
    print(b11)
    print("Tree b4:")
    print(b11.fonk7())