class class1:
    class class2:
        def fonk1(self, b2, b1 = None, b3=None):
            self.b2 = b2
            self.b1 = b1
            self.b3 = b3
            self.a1 = 1
    def fonk2(self):
        self.b4 = None
    def fonk3(self, val):
        self.b4 = self.fonk20(self.b4, val)
    def fonk4(self, val):
        self.b4 = self.fonk16(self.b4, val)
    def fonk5(self, val):
        return self.fonk21(self.b4, val)
    def fonk6(self):
        return self.fonk22(self.b4)
    def fonk7(self):
        return self.fonk12(self.b4)
    def fonk8(self):
        return self.fonk18(self.b4).b2 if not self.fonk10() else None
    def fonk9(self):
        return self.__find_max(self.b4).b2 if not self.fonk10() else None
    def fonk10(self):
        return self.b4 is None
    def fonk11(self, b6):
        b6.a1 = fonk9(self.fonk12(b6.b3), self.fonk12(b6.b1)) + 1
    def fonk12(self, b6):
        return b6.a1 if b6 else 0
    def fonk13(self, b6):
        return self.fonk12(b6.b1) - self.fonk12(b6.b3)
    def fonk14(self, b6):
        b5 = b6.b3
        b6.b3 = b5.b1
        b5.b1 = b6
        self.fonk11(b6)
        self.fonk11(b5)
        return b5
    def fonk15(self, b6):
        b5 = b6.b1
        b6.b1 = b5.b3
        b5.b3 = b6
        self.fonk11(b6)
        self.fonk11(b5)
        return b5
    def fonk16(self, root, val):
        if root is None:
            return class1.class2(val)
        if val < root.b2:
            root.b3 = self.fonk16(root.b3, val)
        elif val > root.b2:
            root.b1 = self.fonk16(root.b1, val)
        return self.fonk17(root)
    def fonk17(self, b6):
        self.fonk11(b6)
        if self.fonk13(b6) == 2:
            if self.fonk13(b6.b1) < 0:
                b6.b1 = self.fonk14(b6.b1)
            return self.fonk15(b6)
        if self.fonk13(b6) == -2:
            if self.fonk13(b6.b3) > 0:
                b6.b3 = self.fonk15(b6.b3)
            return self.fonk14(b6)
        return b6
    def fonk18(self, root):
        return root if root.b3 is None else self.fonk18(root.b3)
    def fonk19(self, b6):
        if b6.b3 is None:
            return b6.b1
        b6.b3 = self.fonk19(b6.b3)
        return self.fonk17(b6)
    def fonk20(self, b6, b2):
        if b6:
            if b2 < b6.b2:
                b6.b3 = self.fonk20(b6.b3, b2)
            elif b2 > b6.b2:
                b6.b1 = self.fonk20(b6.b1, b2)
            else:
                if b6.b3 is None or b6.b1 is None:
                    b6 = b6.b3 if b6.b3 else b6.b1
                else:
                    b7 = self.fonk18(b6.b1)
                    b6.b2 = b7.b2
                    b6.b1 = self.fonk19(b6.b1)
            return self.fonk17(b6)
    def fonk21(self, b6, val):
        if b6 is None:
            return False
        if b6.b2 = = val:
            return True
        elif val < b6.b2:
            return self.fonk21(b6.b3, val)
        else:
            return self.fonk21(b6.b1, val)
    def fonk22(self, b6):
        if b6 is None:
            return ''
        b8 = f"{b6.b2},{b6.a1}\n"
        b8 += self.fonk22(b6.b3)
        b8 += self.fonk22(b6.b1)
        return b8