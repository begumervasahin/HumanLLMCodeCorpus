class class1:
    def fonk1(self):
        self.b1 = None
    def fonk2(self, b2):
        if self.b1:
            self.b1.fonk10(b2)
        else:
            self.b1 = class2(b2)
    def fonk3(self, b2):
        if self.b1:
            return self.b1.fonk11(b2)
        else:
            raise ValueError("Value not found in the tree")
    def fonk4(self):
        return self.b1.fonk14() if self.b1 else []
    def fonk5(self):
        return self.b1.fonk15() if self.b1 else []
    def fonk6(self, b2):
        if self.b1:
            self.b1 = self.b1.fonk16(b2)
        else:
            raise ValueError("Value not found in the tree")
    def fonk7(self, b2):
        if self.b1:
            self.b1 = self.b1.fonk17(b2)
        else:
            raise ValueError("Value not found in the tree")
    def fonk8(self):
        return iter(self.b1) if self.b1 else iter([])
class class2:
    def fonk9(self, b2):
        self.b2 = b2
        self.b3 = None
        self.b4 = None
    def fonk10(self, b2):
        if b2 < self.b2:
            if self.b3:
                self.b3.fonk10(b2)
            else:
                self.b3 = class2(b2)
        else:
            if self.b4:
                self.b4.fonk10(b2)
            else:
                self.b4 = class2(b2)
    def fonk11(self, b2):
        if b2 < self.b2:
            if self.b3:
                return self.b3.fonk11(b2)
            else:
                raise ValueError("Value not found in the tree")
        elif b2 > self.b2:
            if self.b4:
                return self.b4.fonk11(b2)
            else:
                raise ValueError("Value not found in the tree")
        else:
            return self
    def fonk12(self):
        return self.b4.fonk12() if self.b4 else self
    def fonk13(self):
        return self.b3.fonk13() if self.b3 else self
    def fonk14(self):
        b5 = self.b3.fonk14() if self.b3 else []
        b6 = self.b4.fonk14() if self.b4 else []
        return b5 + [self.b2] + b6
    def fonk15(self):
        return fonk14(class3(self))
    def fonk16(self, b2):
        if b2 < self.b2:
            if self.b3:
                self.b3 = self.b3.fonk16(b2)
            else:
                raise ValueError("Value not found in the tree")
        elif b2 > self.b2:
            if self.b4:
                self.b4 = self.b4.fonk16(b2)
            else:
                raise ValueError("Value not found in the tree")
        else:
            if self.b3:
                b7 = self.b3.fonk12()
                self.b2 = b7.b2
                self.b3 = self.b3.fonk18()
            else:
                return self.b4
        return self
    def fonk17(self, b2):
        if b2 < self.b2:
            if self.b3:
                self.b3 = self.b3.fonk17(b2)
            else:
                raise ValueError("Value not found in the tree")
        elif b2 > self.b2:
            if self.b4:
                self.b4 = self.b4.fonk17(b2)
            else:
                raise ValueError("Value not found in the tree")
        else:
            if self.b4:
                b8 = self.b4.fonk13()
                self.b2 = b8.b2
                self.b4 = self.b4.fonk19()
            else:
                return self.b3
        return self
    def fonk18(self):
        if self.b4:
            self.b4 = self.b4.fonk18()
        else:
            return self.b3
        return self
    def fonk19(self):
        if self.b3:
            self.b3 = self.b3.fonk19()
        else:
            return self.b4
        return self
    def fonk20(self):
        return fonk27(self)
class class3:
    def fonk21(self, b1):
        b9 = class2(None)
        b9.b4 = b1
        self.b10 = [b9]
    def fonk22(self):
        if self.fonk25().b4:
            self.fonk23()
        else:
            self.fonk24()
        return self.fonk25().b2
    def fonk23(self):
        self.b10.append(self.fonk25().b4)
        while self.fonk25().b3:
            self.b10.append(self.fonk25().b3)
    def fonk24(self):
        try:
            while self.b10.pop() == self.fonk25().b4:
                pass
        except IndexError:
            raise StopIteration
    def fonk25(self):
        return self.b10[-1]
    def fonk26(self):
        return self
def fonk27(node):
    if node.b3:
        yield from fonk27(node.b3)
    yield node.b2
    if node.b4:
        yield from fonk27(node.b4)
if b11 = = "__main__":
    b12 = class1()
    b12.fonk10(5)
    b12.fonk10(3)
    b12.fonk10(7)
    b12.fonk10(2)
    b12.fonk10(4)
    b12.fonk10(6)
    b12.fonk10(8)
    print("Tree list:", b12.fonk14())
    print("Tree list sequentially:", b12.fonk15())
    b12.fonk16(3)
    print("Tree list after deleting 3 (b3):", b12.fonk14())
    b12.fonk17(7)
    print("Tree list after deleting 7 (b4):", b12.fonk14())