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
        return self.b3.a3 if (self.b3 is not None) else -1
    def fonk8(self):
        return self.b4.a3 if (self.b4 is not None) else -1
    def fonk9(self):
        b5 = self.fonk7()
        b6 = self.fonk8()
        return max(b5, b6)
    def fonk10(self):
        b7 = self.fonk7()
        b8 = self.fonk8()
        return abs(b8 - b7) <= 1
    def fonk11(self):
        b9 = self
        if self.b3:
            b9 = b9.b3
            while b9.b4:
                b9 = b9.b4
            return b9
        else:
            return None
    def fonk12(self):
        b9 = self
        if self.b4:
            b9 = b9.b4
            while b9.b3:
                b9 = b9.b3
            return b9
        else:
            return None
    def fonk13(self):
        b9 = self
        if b9.fonk3():
            while b9.fonk3():
                b9 = b9.b2
            if b9.fonk2():
                return b9.b2
            else:
                return None
        else:
            return None
    def fonk14(self):
        b9 = self
        if b9.fonk2():
            while b9.fonk2():
                b9 = b9.b2
            if b9.fonk3():
                return b9.b2
            else:
                return None
        else:
            return None
    def fonk15(self):
        if self.fonk5():
            if self.b4:
                return self.fonk12()
            else:
                return None
        elif self.fonk2():
            if self.b4:
                return self.fonk12()
            else:
                return self.b2
        else:
            if self.b4:
                return self.fonk12()
            else:
                return self.fonk13()
    def fonk16(self):
        if self.fonk5():
            if self.b3:
                return self.fonk11()
            else:
                return None
        elif self.fonk2():
            if self.b3:
                return self.fonk11()
            else:
                return self.fonk14()
        else:
            if self.b3:
                return self.fonk11()
            else:
                return self.b2
    def fonk17(self, delegateTree, b1):
        if self.b1 = = b1:
            self.a1 += 1
            return None
        elif self.b1 > b1:
            if not self.b3:
                self.b3 = class1(b1)
                self.b3.b2 = self
                self.b3.a2 = self.a2 + 1
                delegateTree.a5 += 1
                return self.b3
            else:
                return self.b3.fonk25(delegateTree, b1)
        else:
            if not self.b4:
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
                delegateTree.b10 = None
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
    def fonk19(self, delegateTree, b20):
        b20.b2 = self.b2
        b20.b3 = self.b3
        b20.b4 = self.b4
        b20.a3 = self.a3
        b20.a2 = self.a2
        if self.b3:
            self.b3.b2 = b20
        if self.b4:
            self.b4.b2 = b20
        if self.fonk2():
            self.b2.b3 = b20
        if self.fonk3():
            self.b2.b4 = b20
        if self.fonk5():
            delegateTree.b10 = b20
    def fonk20(self, delegateTree):
        self.a3 = self.fonk9() + 1
        if not self.fonk10():
            self.fonk21(delegateTree)
        if self.b2:
            self.b2.fonk20(delegateTree)
    def fonk21(self, delegateTree):
        b11 = self.b2
        if self.fonk7() > self.fonk8():
            if self.b3.fonk7() > self.b3.fonk8():
                b12 = self
                b13 = self.b3
                b14 = self.b3.b3
                b15 = b14.b3
                b16 = b14.b4
                b17 = b13.b4
                b18 = b12.b4
            else:
                b12 = self
                b13 = self.b3.b4
                b14 = self.b3
                b15 = b14.b3
                b16 = b13.b3
                b17 = b13.b4
                b18 = b12.b4
            if b12.fonk2():
                b11.b3 = b13
            elif b12.fonk3():
                b11.b4 = b13
            else:
                delegateTree.b10 = b13
        else:
            if self.b4.fonk8() > self.b4.fonk7():
                b12 = self.b4.b4
                b13 = self.b4
                b14 = self
                b15 = b14.b3
                b16 = b13.b3
                b17 = b12.b3
                b18 = b12.b4
            else:
                b12 = self.b4
                b13 = self.b4.b3
                b14 = self
                b15 = b14.b3
                b16 = b13.b3
                b17 = b13.b4
                b18 = b12.b4
            if b14.fonk2():
                b11.b3 = b13
            elif b14.fonk3():
                b11.b4 = b13
            else:
                delegateTree.b10 = b13
        b13.b2 = b11
        b13.b3 = b14
        b13.b4 = b12
        b14.b2 = b13
        b12.b2 = b13
        if b15:
            b15.b2 = b14
        if b16:
            b16.b2 = b14
        if b17:
            b17.b2 = b12
        if b18:
            b18.b2 = b12
        b14.b3 = b15
        b14.b4 = b16
        b12.b3 = b17
        b12.b4 = b18
        b14.a3 = b14.fonk9() + 1
        b12.a3 = b12.fonk9() + 1
        b13.a3 = b13.fonk9() + 1
        if b11:
            b13.fonk22(b11.a2 + 1)
        else:
            b13.fonk22(0)
    def fonk22(self, a2):
        if self.b3:
            self.b3.fonk22(a2 + 1)
        self.a2 = a2
        if self.b4:
            self.b4.fonk22(a2 + 1)
class class2:
    def fonk23(self):
        self.b10 = None
        self.a5 = 0
        self.b19 = None
    def fonk24(self, b1):
        if self.b10:
            b9 = self.b10
            while b9:
                if b9.b1 = = b1:
                    return b9
                elif b9.b1 > b1:
                    b9 = b9.b3
                else:
                    b9 = b9.b4
            return b9
        else:
            return None
    def fonk25(self, b1):
        if not self.b10:
            self.b10 = class1(b1)
            self.b10.a3 = 0
            self.b10.a2 = 0
            self.a5 = 1
        else:
            b20 = self.b10.fonk25(self, b1)
            if b20:
                b20.fonk20(self)
    def fonk26(self, b1):
        b21 = self.fonk24(b1)
        if b21:
            b21.fonk26(self)
            self.a5 -= 1
        return b21
    def fonk27(self):
        if self.b10:
            b9 = self.b10
            while b9.b3:
                b9 = b9.b3
            while b9:
                print(b9.b1)
                b9 = b9.fonk15()
    def fonk28(self):
        if self.b10:
            b9 = self.b10
            while b9.b3:
                b9 = b9.b3
            return b9
        else:
            return None
    def fonk29(self):
        if self.b10:
            b9 = self.fonk28()
            a6 = 0
            while b9:
                b9.a4 = a6
                a6 += 1
                b9 = b9.fonk15()