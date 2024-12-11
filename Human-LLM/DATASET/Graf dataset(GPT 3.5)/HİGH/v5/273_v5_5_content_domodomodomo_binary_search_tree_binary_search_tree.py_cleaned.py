class class1:
    def fonk1(self):
        self.b1 = None
    def fonk2(self, b4):
        if self.b1:
            self.fonk3(b4, self.b1)
        else:
            self.b1 = class2(b4)
    def fonk3(self, b4, b15):
        if b4 < b15.b4:
            if b15.b2:
                self.fonk3(b4, b15.b2)
            else:
                b15.b2 = class2(b4)
        elif b4 >= b15.b4:
            if b15.b3:
                self.fonk3(b4, b15.b3)
            else:
                b15.b3 = class2(b4)
    def fonk4(self, b4):
        if self.b1:
            return self.fonk5(b4, self.b1)
        else:
            raise ValueError("Tree is empty")
    def fonk5(self, b4, b15):
        if not b15:
            raise ValueError("Value not found")
        if b4 = = b15.b4:
            return b15
        elif b4 < b15.b4:
            return self.fonk5(b4, b15.b2)
        else:
            return self.fonk5(b4, b15.b3)
    def fonk6(self):
        if self.b1:
            return self.b1.fonk12()
        else:
            return []
    def fonk7(self):
        if self.b1:
            return self.b1.fonk13()
        else:
            return []
    def fonk8(self, b4):
        if self.b1:
            self.b1 = self.b1.fonk14(b4, b9='b2')
        else:
            raise ValueError("Tree is empty")
    def fonk9(self, b4):
        if self.b1:
            self.b1 = self.b1.fonk14(b4, b9='b3')
        else:
            raise ValueError("Tree is empty")
    def fonk10(self):
        if self.b1:
            return iter(self.b1)
        else:
            return iter([])
class class2:
    def fonk11(self, b4):
        self.b4 = b4
        self.b2 = None
        self.b3 = None
    def fonk12(self):
        b5 = self.b2.fonk12() if self.b2 else []
        b6 = self.b3.fonk12() if self.b3 else []
        return b5 + [self.b4] + b6
    def fonk13(self):
        b7 = []
        b8 = class3(self)
        while True:
            try:
                b4 = next(b8)
            except StopIteration:
                break
            else:
                b7.append(b4)
        return b7
    def fonk14(self, b4, b9):
        if b4 < self.b4:
            if self.b2:
                self.b2 = self.b2.fonk14(b4, b9)
            else:
                raise ValueError(f"Value {b4} not found")
        elif b4 > self.b4:
            if self.b3:
                self.b3 = self.b3.fonk14(b4, b9)
            else:
                raise ValueError(f"Value {b4} not found")
        elif b4 = = self.b4:
            if b9 = = 'b2':
                return self.fonk15()
            elif b9 = = 'b3':
                return self.fonk16()
    def fonk15(self):
        if self.b2:
            b10 = self.b2.fonk17()
            b11 = b10.b4
            self.b2 = self.b2.fonk14(b11, b9='b2')
            self.b4 = b11
            return self
        else:
            return self.b3
    def fonk16(self):
        if self.b3:
            b12 = self.b3.fonk18()
            b13 = b12.b4
            self.b3 = self.b3.fonk14(b13, b9='b3')
            self.b4 = b13
            return self
        else:
            return self.b2
    def fonk17(self):
        if self.b3:
            return self.b3.fonk17()
        else:
            return self
    def fonk18(self):
        if self.b2:
            return self.b2.fonk18()
        else:
            return self
    def fonk19(self):
        return class3(self)
class class3:
    def fonk20(self, b1):
        self.b14 = []
        self.fonk21(b1)
    def fonk21(self, b15):
        while b15:
            self.b14.append(b15)
            b15 = b15.b2
    def fonk22(self):
        if not self.b14:
            raise StopIteration
        b16 = self.b14.pop()
        if b16.b3:
            self.fonk21(b16.b3)
        return b16.b4
    def fonk23(self):
        return self
if b17 = = '__main__':
    pass