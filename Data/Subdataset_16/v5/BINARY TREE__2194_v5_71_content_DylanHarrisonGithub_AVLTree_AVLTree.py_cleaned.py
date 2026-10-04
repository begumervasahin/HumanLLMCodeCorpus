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
        return self.b3.a2 if self.b3 else -1
    def fonk7(self):
        return self.b4.a2 if self.b4 else -1
    def fonk8(self):
        return max(self.fonk6(), self.fonk7())
    def fonk9(self):
        return abs(self.fonk6() - self.fonk7()) <= 1
    def fonk10(self):
        b5 = self.b3
        while b5 and b5.b4:
            b5 = b5.b4
        return b5
    def fonk11(self):
        b5 = self.b4
        while b5 and b5.b3:
            b5 = b5.b3
        return b5
    def fonk12(self):
        if self.b4:
            return self.fonk11()
        elif self.fonk2():
            return self.b2
        else:
            b5 = self
            while b5.fonk3():
                b5 = b5.b2
            return b5.b2 if b5.fonk2() else None
    def fonk13(self):
        if self.b3:
            return self.fonk10()
        elif self.fonk3():
            return self.b2
        else:
            b5 = self
            while b5.fonk2():
                b5 = b5.b2
            return b5.b2 if b5.fonk3() else None
    def fonk14(self, delegate_tree, b1):
        if self.b1 = = b1:
            self.a1 += 1
            return None
        elif self.b1 > b1:
            if self.b3:
                return self.b3.fonk22(delegate_tree, b1)
            else:
                self.b3 = class1(b1)
                self.b3.b2 = self
                self.b3.a3 = self.a3 + 1
                delegate_tree.a5 += 1
                return self.b3
        else:
            if self.b4:
                return self.b4.fonk22(delegate_tree, b1)
            else:
                self.b4 = class1(b1)
                self.b4.b2 = self
                self.b4.a3 = self.a3 + 1
                delegate_tree.a5 += 1
                return self.b4
    def fonk15(self, delegate_tree):
        if self.fonk4():
            if self.fonk2():
                self.b2.b3 = None
            elif self.fonk3():
                self.b2.b4 = None
            else:
                delegate_tree.b6 = None
            if self.b2:
                self.b2.fonk17(delegate_tree)
        else:
            if self.b3 and self.b4:
                b7 = self.fonk12() if not self.fonk13().fonk4() else self.fonk13()
                self.fonk16(delegate_tree, b7.fonk23(delegate_tree))
            else:
                b7 = self.fonk12() if self.b4 else self.fonk13()
                self.fonk16(delegate_tree, b7.fonk23(delegate_tree))
        return self
    def fonk16(self, delegate_tree, b11):
        if not b11:
            return
        b11.b2 = self.b2
        b11.b3 = self.b3
        b11.b4 = self.b4
        b11.a2 = self.a2
        b11.a3 = self.a3
        if self.b3:
            self.b3.b2 = b11
        if self.b4:
            self.b4.b2 = b11
        if self.fonk2():
            self.b2.b3 = b11
        elif self.fonk3():
            self.b2.b4 = b11
        if self.fonk5():
            delegate_tree.b6 = b11
    def fonk17(self, delegate_tree):
        self.a2 = self.fonk8() + 1
        if not self.fonk9():
            self.fonk18(delegate_tree)
        if self.b2:
            self.b2.fonk17(delegate_tree)
    def fonk18(self, delegate_tree):
        b8 = self.b2
        if self.fonk6() > self.fonk7():
            if self.b3.fonk6() > self.b3.fonk7():
                z, y, b9 = self, self.b3, self.b3.b3
                T0, T1, T2, b10 = b9.b3, b9.b4, y.b4, z.b4
            else:
                z, y, b9 = self, self.b3.b4, self.b3
                T0, T1, T2, b10 = b9.b3, y.b3, y.b4, z.b4
        else:
            if self.b4.fonk7() > self.b4.fonk6():
                z, y, b9 = self.b4.b4, self.b4, self
                T0, T1, T2, b10 = b9.b3, y.b3, z.b3, z.b4
            else:
                z, y, b9 = self.b4, self.b4.b3, self
                T0, T1, T2, b10 = b9.b3, y.b3, y.b4, z.b4
        if b8:
            if self.fonk2():
                b8.b3 = y
            elif self.fonk3():
                b8.b4 = y
        else:
            delegate_tree.b6 = y
        y.b2 = b8
        y.b3, y.b4 = b9, z
        b9.b2, z.b2 = y, y
        b9.b3, b9.b4 = T0, T1
        z.b3, z.b4 = T2, b10
        if T0: T0.b2 = b9
        if T1: T1.b2 = b9
        if T2: T2.b2 = z
        if b10: b10.b2 = z
        b9.a2 = b9.fonk8() + 1
        z.a2 = z.fonk8() + 1
        y.a2 = y.fonk8() + 1
        y.fonk19(b8.a3 + 1 if b8 else 0)
    def fonk19(self, a3):
        self.a3 = a3
        if self.b3:
            self.b3.fonk19(a3 + 1)
        if self.b4:
            self.b4.fonk19(a3 + 1)
class class2:
    def fonk20(self):
        self.b6 = None
        self.a5 = 0
    def fonk21(self, b1):
        b5 = self.b6
        while b5:
            if b5.b1 = = b1:
                return b5
            elif b5.b1 > b1:
                b5 = b5.b3
            else:
                b5 = b5.b4
        return None
    def fonk22(self, b1):
        if not self.b6:
            self.b6 = class1(b1)
            self.a5 = 1
        else:
            b11 = self.b6.fonk22(self, b1)
            if b11:
                b11.fonk17(self)
    def fonk23(self, b1):
        b12 = self.fonk21(b1)
        if b12:
            b12.fonk23(self)
            self.a5 -= 1
        return b12
    def fonk24(self):
        b5 = self.fonk25()
        while b5:
            print(b5.b1)
            b5 = b5.fonk12()
    def fonk25(self):
        b5 = self.b6
        while b5 and b5.b3:
            b5 = b5.b3
        return b5
    def fonk26(self):
        b5 = self.fonk25()
        a4 = 0
        while b5:
            b5.a4 = a4
            a4 += 1
            b5 = b5.fonk12()