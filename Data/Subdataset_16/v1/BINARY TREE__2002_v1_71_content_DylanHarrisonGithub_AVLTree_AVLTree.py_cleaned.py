class class1(object):
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
        return (self.b2 is not None) and (self.b2.b3 = = self)
    def fonk3(self):
        return (self.b2 is not None) and (self.b2.b4 = = self)
    def fonk4(self):
        return (self.b3 is None) and (self.b4 is None)
    def fonk5(self):
        return self.b2 is None
    def fonk6(self):
        return (self.b2 is not None) and (self.b2.b2 is not None)
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
        if b5.b3 is not None:
            b5 = b5.b3
            while b5.b4 is not None:
                b5 = b5.b4
            return b5
        return None
    def fonk12(self):
        b5 = self
        if b5.b4 is not None:
            b5 = b5.b4
            while b5.b3 is not None:
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
        elif self.fonk2():
            return self.fonk12() if self.b4 else self.b2
        else:
            return self.fonk12() if self.b4 else self.fonk13()
    def fonk16(self):
        if self.fonk5():
            return self.fonk11() if self.b3 else None
        elif self.fonk2():
            return self.fonk11() if self.b3 else self.fonk14()
        else:
            return self.fonk11() if self.b3 else self.b2
    def fonk17(self, delegateTree, b1):
        if self.b1 = = b1:
            self.a1 += 1
            return None
        elif self.b1 > b1:
            if self.b3 is None:
                self.b3 = class1(b1)
                self.b3.b2 = self
                self.b3.a2 = self.a2 + 1
                delegateTree.a5 += 1
                return self.b3
            else:
                return self.b3.fonk25(delegateTree, b1)
        else:
            if self.b4 is None:
                self.b4 = class1(b1)
                self.b4.b2 = self
                self.b4.a2 = self.a2 + 1
                delegateTree.a5 += 1
                return self.b4
            else:
                return self.b4.fonk25(delegateTree, b1)
    def fonk18(self, delegateTree):
        if self.fonk4():
            if self.fonk2():
                self.b2.b3 = None
                self.b2.fonk20(delegateTree)
            elif self.fonk3():
                self.b2.b4 = None
                self.b2.fonk20(delegateTree)
            else:
                delegateTree.b6 = None
        else:
            if self.b3 and self.b4:
                if self.fonk16().fonk4():
                    self.fonk19(delegateTree, self.fonk16().fonk26(delegateTree))
                else:
                    self.fonk19(delegateTree, self.fonk15().fonk26(delegateTree))
            else:
                if self.b4:
                    self.fonk19(delegateTree, self.fonk15().fonk26(delegateTree))
                else:
                    self.fonk19(delegateTree, self.fonk16().fonk26(delegateTree))
        return self
    def fonk19(self, delegateTree, b12):
        b12.b2 = self.b2
        b12.b3 = self.b3
        b12.b4 = self.b4
        b12.a3 = self.a3
        b12.a2 = self.a2
        if self.b3:
            self.b3.b2 = b12
        if self.b4:
            self.b4.b2 = b12
        if self.fonk2():
            self.b2.b3 = b12
        if self.fonk3():
            self.b2.b4 = b12
        if self.fonk5():
            delegateTree.b6 = b12
    def fonk20(self, delegateTree):
        self.a3 = self.fonk9() + 1
        if not self.fonk10():
            self.fonk21(delegateTree)
        if self.b2:
            self.b2.fonk20(delegateTree)
    def fonk21(self, delegateTree):
        b7 = self.b2
        if self.fonk7() > self.fonk8():
            if self.b3.fonk7() > self.b3.fonk8():
                b8 = self
                b9 = self.b3
                b10 = self.b3.b3
                T_0, T_1, T_2, b11 = b10.b3, b10.b4, b9.b4, b8.b4
            else:
                b8 = self
                b9 = self.b3.b4
                b10 = self.b3
                T_0, T_1, T_2, b11 = b10.b3, b9.b3, b9.b4, b8.b4
            if b8.fonk2():
                b7.b3 = b9
            elif b8.fonk3():
                b7.b4 = b9
            else:
                delegateTree.b6 = b9
        else:
            if self.b4.fonk8() > self.b4.fonk7():
                b8 = self.b4.b4
                b9 = self.b4
                b10 = self
                T_0, T_1, T_2, b11 = b10.b3, b9.b3, b8.b3, b8.b4
            else:
                b8 = self.b4
                b9 = self.b4.b3
                b10 = self
                T_0, T_1, T_2, b11 = b10.b3, b9.b3, b9.b4, b8.b4
            if b10.fonk2():
                b7.b3 = b9
            elif b10.fonk3():
                b7.b4 = b9
            else:
                delegateTree.b6 = b9
        b9.b2 = b7
        b9.b3 = b10
        b9.b4 = b8
        b10.b2 = b9
        b8.b2 = b9
        if T_0:
            T_0.b2 = b10
        if T_1:
            T_1.b2 = b10
        if T_2:
            T_2.b2 = b8
        if b11:
            b11.b2 = b8
        b10.b3 = T_0
        b10.b4 = T_1
        b8.b3 = T_2
        b8.b4 = b11
        b10.a3 = b10.fonk9() + 1
        b8.a3 = b8.fonk9() + 1
        b9.a3 = b9.fonk9() + 1
        if b7:
            b9.fonk22(b7.a2 + 1)
        else:
            b9.fonk22(0)
    def fonk22(self, a2):
        if self.b3:
            self.b3.fonk22(a2 + 1)
        self.a2 = a2
        if self.b4:
            self.b4.fonk22(a2 + 1)
class class2(object):
    def fonk23(self):
        self.b6 = None
        self.a5 = 0
    def fonk24(self, b1):
        if self.b6:
            b5 = self.b6
            while b5:
                if b5.b1 = = b1:
                    return b5
                elif b5.b1 > b1:
                    b5 = b5.b3
                else:
                    b5 = b5.b4
            return b5
        return None
    def fonk25(self, b1):
        if self.b6 is None:
            self.b6 = class1(b1)
            self.b6.a3 = 0
            self.b6.a2 = 0
            self.a5 = 1
        else:
            b12 = self.b6.fonk25(self, b1)
            if b12:
                b12.fonk20(self)
    def fonk26(self, b1):
        b13 = self.fonk24(b1)
        if b13:
            b13.fonk26(self)
            self.a5 -= 1
        return b13
    def fonk27(self):
        if self.b6:
            b5 = self.b6
            while b5.b3:
                b5 = b5.b3
            while b5:
                print(b5.b1)
                b5 = b5.fonk15()
    def fonk28(self):
        if self.b6:
            b5 = self.b6
            while b5.b3:
                b5 = b5.b3
            return b5
        return None
    def fonk29(self):
        if self.b6:
            b5 = self.fonk28()
            a6 = 0
            while b5:
                b5.a4 = a6
                a6 += 1
                b5 = b5.fonk15()
if b14 = = "__main__":
    b15 = class2()
    b15.fonk25(10)
    b15.fonk25(20)
    b15.fonk25(30)
    b15.fonk25(40)
    b15.fonk25(50)
    b15.fonk25(25)
    print("AVL Tree in a4:")
    b15.fonk27()
    b15.fonk26(30)
    print("AVL Tree after removing 30:")
    b15.fonk27()
    print("First node:", b15.fonk28().b1)
    b15.fonk29()
    print("Nodes with a4 marked:")
    b15.fonk27()