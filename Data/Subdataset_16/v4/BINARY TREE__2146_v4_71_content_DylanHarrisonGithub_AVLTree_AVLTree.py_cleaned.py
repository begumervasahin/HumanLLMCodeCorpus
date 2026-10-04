class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.a1 = 1
        self.a2 = 0
        self.a3 = 0
        self.a4 = -1
        self.b2 = None
        self.b3 = None
        self.b4 = None
    def fonk2(self):
        return self.b2 is not None and self.b2.b3 = = self
    def fonk3(self):
        return self.b2 is not None and self.b2.b4 = = self
    def fonk4(self):
        return self.b3 is None and self.b4 is None
    def fonk5(self):
        return self.b2 is None
    def fonk6(self):
        return self.b2 is not None and self.b2.b2 is not None
    def fonk7(self):
        return self.b3.a3 if self.b3 else -1
    def fonk8(self):
        return self.b4.a3 if self.b4 else -1
    def fonk9(self):
        return max(self.fonk7(), self.fonk8())
    def fonk10(self):
        return abs(self.fonk7() - self.fonk8()) <= 1
    def fonk11(self):
        b5 = self.b3
        while b5 and b5.b4:
            b5 = b5.b4
        return b5
    def fonk12(self):
        b5 = self.b4
        while b5 and b5.b3:
            b5 = b5.b3
        return b5
    def fonk13(self):
        b5 = self
        while b5.fonk3():
            b5 = b5.b2
        return b5.b2 if b5.fonk2() else None
    def fonk14(self):
        b5 = self
        while b5.fonk2():
            b5 = b5.b2
        return b5.b2 if b5.fonk3() else None
    def fonk15(self):
        if self.b4:
            return self.fonk12()
        elif self.fonk2():
            return self.b2
        else:
            return self.fonk13()
    def fonk16(self):
        if self.b3:
            return self.fonk11()
        elif self.fonk3():
            return self.b2
        else:
            return self.fonk14()
    def fonk17(self, delegate_tree, b1):
        if self.b1 = = b1:
            self.a1 += 1
            return None
        elif self.b1 > b1:
            if self.b3:
                return self.b3.fonk25(delegate_tree, b1)
            else:
                self.b3 = class1(b1)
                self.b3.b2 = self
                self.b3.a2 = self.a2 + 1
                delegate_tree.a5 += 1
                return self.b3
        else:
            if self.b4:
                return self.b4.fonk25(delegate_tree, b1)
            else:
                self.b4 = class1(b1)
                self.b4.b2 = self
                self.b4.a2 = self.a2 + 1
                delegate_tree.a5 += 1
                return self.b4
    def fonk18(self, delegate_tree):
        if self.fonk4():
            if self.fonk2():
                self.b2.b3 = None
            elif self.fonk3():
                self.b2.b4 = None
            else:
                delegate_tree.b6 = None
            self.b2.fonk20(delegate_tree)
        else:
            if self.b3 and self.b4:
                if self.fonk16().fonk4():
                    self.fonk19(delegate_tree, self.fonk16().fonk26(delegate_tree))
                else:
                    self.fonk19(delegate_tree, self.fonk15().fonk26(delegate_tree))
            else:
                self.fonk19(delegate_tree, self.fonk15().fonk26(delegate_tree) if self.b4 else self.fonk16().fonk26(delegate_tree))
        return self
    def fonk19(self, delegate_tree, b10):
        b10.b2 = self.b2
        b10.b3 = self.b3
        b10.b4 = self.b4
        b10.a3 = self.a3
        b10.a2 = self.a2
        if self.b3:
            self.b3.b2 = b10
        if self.b4:
            self.b4.b2 = b10
        if self.fonk2():
            self.b2.b3 = b10
        elif self.fonk3():
            self.b2.b4 = b10
        if self.fonk5():
            delegate_tree.b6 = b10
    def fonk20(self, delegate_tree):
        self.a3 = self.fonk9() + 1
        if not self.fonk10():
            self.fonk21(delegate_tree)
        if self.b2:
            self.b2.fonk20(delegate_tree)
    def fonk21(self, delegate_tree):
        b7 = self.b2
        if self.fonk7() > self.fonk8():
            if self.b3.fonk7() > self.b3.fonk8():
                z, y, b8 = self, self.b3, self.b3.b3
                T_0, T_1, T_2, b9 = b8.b3, b8.b4, y.b4, z.b4
            else:
                z, y, b8 = self, self.b3.b4, self.b3
                T_0, T_1, T_2, b9 = b8.b3, y.b3, y.b4, z.b4
        else:
            if self.b4.fonk8() > self.b4.fonk7():
                z, y, b8 = self.b4.b4, self.b4, self
                T_0, T_1, T_2, b9 = b8.b3, y.b3, z.b3, z.b4
            else:
                z, y, b8 = self.b4, self.b4.b3, self
                T_0, T_1, T_2, b9 = b8.b3, y.b3, y.b4, z.b4
        if b8.fonk2():
            b7.b3 = y
        elif b8.fonk3():
            b7.b4 = y
        else:
            delegate_tree.b6 = y
        y.b2 = b7
        y.b3, y.b4 = b8, z
        b8.b2, z.b2 = y, y
        if T_0: T_0.b2 = b8
        if T_1: T_1.b2 = b8
        if T_2: T_2.b2 = z
        if b9: b9.b2 = z
        b8.b3, b8.b4 = T_0, T_1
        z.b3, z.b4 = T_2, b9
        b8.a3 = b8.fonk9() + 1
        z.a3 = z.fonk9() + 1
        y.a3 = y.fonk9() + 1
        if b7:
            y.fonk22(b7.a2 + 1)
        else:
            y.fonk22(0)
    def fonk22(self, a2):
        self.a2 = a2
        if self.b3:
            self.b3.fonk22(a2 + 1)
        if self.b4:
            self.b4.fonk22(a2 + 1)
class class2:
    def fonk23(self):
        self.b6 = None
        self.a5 = 0
    def fonk24(self, b1):
        b5 = self.b6
        while b5:
            if b5.b1 = = b1:
                return b5
            elif b5.b1 > b1:
                b5 = b5.b3
            else:
                b5 = b5.b4
        return None
    def fonk25(self, b1):
        if not self.b6:
            self.b6 = class1(b1)
            self.a5 = 1
        else:
            b10 = self.b6.fonk25(self, b1)
            if b10:
                b10.fonk20(self)
    def fonk26(self, b1):
        b11 = self.fonk24(b1)
        if b11:
            b11.fonk26(self)
            self.a5 -= 1
        return b11
    def fonk27(self):
        b5 = self.fonk28()
        while b5:
            print(b5.b1)
            b5 = b5.fonk15()
    def fonk28(self):
        b5 = self.b6
        while b5 and b5.b3:
            b5 = b5.b3
        return b5
    def fonk29(self):
        b5 = self.fonk28()
        a4 = 0
        while b5:
            b5.a4 = a4
            a4 += 1
            b5 = b5.fonk15()