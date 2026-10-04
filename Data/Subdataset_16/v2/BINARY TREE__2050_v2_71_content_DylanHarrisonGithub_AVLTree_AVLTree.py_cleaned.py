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
        return self.b2 and self.b2.b3 = = self
    def fonk3(self):
        return self.b2 and self.b2.b4 = = self
    def fonk4(self):
        return not self.b3 and not self.b4
    def fonk5(self):
        return not self.b2
    def fonk6(self):
        return self.b2 and self.b2.b2
    def fonk7(self):
        return self.b3.a3 if self.b3 else -1
    def fonk8(self):
        return self.b4.a3 if self.b4 else -1
    def fonk9(self):
        return max(self.fonk7(), self.fonk8())
    def fonk10(self):
        return abs(self.fonk7() - self.fonk8()) <= 1
    def fonk11(self):
        b5 = self
        if b5.b3:
            b5 = b5.b3
            while b5.b4:
                b5 = b5.b4
            return b5
        return None
    def fonk12(self):
        b5 = self
        if b5.b4:
            b5 = b5.b4
            while b5.b3:
                b5 = b5.b3
            return b5
        return None
    def fonk13(self):
        b5 = self
        if b5.fonk3():
            while b5.fonk3():
                b5 = b5.b2
            if b5.fonk2():
                return b5.b2
        return None
    def fonk14(self):
        b5 = self
        if b5.fonk2():
            while b5.fonk2():
                b5 = b5.b2
            if b5.fonk3():
                return b5.b2
        return None
    def fonk15(self):
        if self.fonk5():
            return self.fonk12() if self.b4 else None
        if self.fonk2():
            return self.fonk12() if self.b4 else self.b2
        return self.fonk12() if self.b4 else self.fonk13()
    def fonk16(self):
        if self.fonk5():
            return self.fonk11() if self.b3 else None
        if self.fonk2():
            return self.fonk11() if self.b3 else self.fonk14()
        return self.fonk11() if self.b3 else self.b2
    def fonk17(self, tree, b1):
        if self.b1 = = b1:
            self.a1 += 1
            return None
        if self.b1 > b1:
            if not self.b3:
                self.b3 = class1(b1)
                self.b3.b2 = self
                self.b3.a2 = self.a2 + 1
                tree.a5 += 1
                return self.b3
            return self.b3.fonk25(tree, b1)
        if not self.b4:
            self.b4 = class1(b1)
            self.b4.b2 = self
            self.b4.a2 = self.a2 + 1
            tree.a5 += 1
            return self.b4
        return self.b4.fonk25(tree, b1)
    def fonk18(self, tree):
        if self.fonk4():
            if self.fonk2():
                self.b2.b3 = None
                self.b2.fonk20(tree)
            elif self.fonk3():
                self.b2.b4 = None
                self.b2.fonk20(tree)
            else:
                tree.b6 = None
        else:
            if self.b3 and self.b4:
                if self.fonk16().fonk4():
                    self.fonk19(tree, self.fonk16().fonk26(tree))
                else:
                    self.fonk19(tree, self.fonk15().fonk26(tree))
            elif self.b4:
                self.fonk19(tree, self.fonk15().fonk26(tree))
            else:
                self.fonk19(tree, self.fonk16().fonk26(tree))
        return self
    def fonk19(self, tree, b11):
        b11.b2 = self.b2
        b11.b3 = self.b3
        b11.b4 = self.b4
        b11.a3 = self.a3
        b11.a2 = self.a2
        if self.b3:
            self.b3.b2 = b11
        if self.b4:
            self.b4.b2 = b11
        if self.fonk2():
            self.b2.b3 = b11
        if self.fonk3():
            self.b2.b4 = b11
        if self.fonk5():
            tree.b6 = b11
    def fonk20(self, tree):
        self.a3 = self.fonk9() + 1
        if not self.fonk10():
            self.fonk21(tree)
        if self.b2:
            self.b2.fonk20(tree)
    def fonk21(self, tree):
        b2 = self.b2
        if self.fonk7() > self.fonk8():
            if self.b3.fonk7() > self.b3.fonk8():
                b7 = self
                b8 = self.b3
                b9 = self.b3.b3
                T0, T1, T2, b10 = b9.b3, b9.b4, b8.b4, b7.b4
            else:
                b7 = self
                b8 = self.b3.b4
                b9 = self.b3
                T0, T1, T2, b10 = b9.b3, b8.b3, b8.b4, b7.b4
            if b7.fonk2():
                b2.b3 = b8
            elif b7.fonk3():
                b2.b4 = b8
            else:
                tree.b6 = b8
        else:
            if self.b4.fonk8() > self.b4.fonk7():
                b7 = self.b4.b4
                b8 = self.b4
                b9 = self
                T0, T1, T2, b10 = b9.b3, b8.b3, b7.b3, b7.b4
            else:
                b7 = self.b4
                b8 = self.b4.b3
                b9 = self
                T0, T1, T2, b10 = b9.b3, b8.b3, b8.b4, b7.b4
            if b9.fonk2():
                b2.b3 = b8
            elif b9.fonk3():
                b2.b4 = b8
            else:
                tree.b6 = b8
        b8.b2 = b2
        b8.b3 = b9
        b8.b4 = b7
        b9.b2 = b8
        b7.b2 = b8
        b9.b3 = T0
        b9.b4 = T1
        b7.b3 = T2
        b7.b4 = b10
        if T0:
            T0.b2 = b9
        if T1:
            T1.b2 = b9
        if T2:
            T2.b2 = b7
        if b10:
            b10.b2 = b7
        b9.a3 = b9.fonk9() + 1
        b7.a3 = b7.fonk9() + 1
        b8.a3 = b8.fonk9() + 1
        if b2:
            b8.fonk22(b2.a2 + 1)
        else:
            b8.fonk22(0)
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
            if b5.b1 > b1:
                b5 = b5.b3
            else:
                b5 = b5.b4
        return None
    def fonk25(self, b1):
        if not self.b6:
            self.b6 = class1(b1)
            self.b6.a3 = 0
            self.b6.a2 = 0
            self.a5 = 1
        else:
            b11 = self.b6.fonk25(self, b1)
            if b11:
                b11.fonk20(self)
    def fonk26(self, b1):
        b12 = self.fonk24(b1)
        if b12:
            b12.fonk26(self)
            self.a5 -= 1
        return b12
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
if b13 = = "__main__":
    b14 = class2()
    b14.fonk25(10)
    b14.fonk25(20)
    b14.fonk25(30)
    b14.fonk25(40)
    b14.fonk25(50)
    b14.fonk25(25)
    print("AVL Tree in a4:")
    b14.fonk27()
    b14.fonk26(30)
    print("AVL Tree after removing 30:")
    b14.fonk27()
    b15 = b14.fonk28()
    if b15:
        print("First node:", b15.b1)
    b14.fonk29()
    print("Nodes with a4 marked:")
    b14.fonk27()