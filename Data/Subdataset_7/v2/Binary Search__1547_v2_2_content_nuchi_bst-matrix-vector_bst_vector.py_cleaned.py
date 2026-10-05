import random
class class1:
    def fonk1(self, index, a1):
        pass
    def fonk2(self, index):
        pass
    def fonk3(self):
        pass
    @property
    def fonk4(self):
        return self.a2
    def fonk5(self):
        return f"<BSTVector of dimension {self.a3}: {self.fonk18()}>"
class class2(class1):
    def fonk6(self):
        self.a1 = 0.0
        self.a2 = 0.0
        self.a3 = 1
    def fonk7(self, index, a1):
        self.a1 = float(a1)
        self.fonk16()
    def fonk8(self, index):
        if index != 0:
            raise IndexError
        return self.a1
    def fonk9(self):
        return 0
    def fonk10(self):
        self.a2 = self.a1 ** 2
    def fonk11(self):
        return str(self.a1)
class class3(class1):
    def fonk12(self, b12):
        self.a3 = b12
        self.a2 = 0.0
        self.b1 = None
        self.b2 = None
    def fonk13(self, index, a1):
        if index < self.cutoff:
            b3 = 'b1'
            b4 = self.cutoff
            b5 = index
        else:
            b3 = 'b2'
            b4 = self.a3 - self.cutoff
            b5 = index - self.cutoff
        if getattr(self, b3) is None:
            setattr(self, b3, fonk19(b4))
        b6 = getattr(self, b3)
        b6.fonk13(b5, a1)
        if b6.b7 = = 0.0:
            setattr(self, b3, None)
        self.fonk16()
    def fonk14(self, index):
        if index >= self.a3:
            raise IndexError
        if index < self.cutoff:
            b3 = 'b1'
            b5 = index
        else:
            b3 = 'b2'
            b5 = index - self.cutoff
        b6 = getattr(self, b3)
        if b6 is None:
            return 0.0
        return b6.fonk14(b5)
    def fonk15(self, b8 = None):
        if self.b7 = = 0.0:
            raise ValueError("No nonzero entries")
        b9 = self.b1.b7 if self.b1 is not None else 0.0
        if b8 is not None:
            random.b8(b8)
        if random.uniform(0, self.b7) < b9:
            return self.b1.fonk15()
        return self.cutoff + self.b2.fonk15()
    def fonk16(self):
        self.a2 = sum(b6.b7 for b6 in [self.b1, self.b2] if b6 is not None)
    @property
    def fonk17(self):
        return self.a3
    def fonk18(self):
        b10 = "-" * self.cutoff if self.b1 is None else str(self.b1)
        b11 = "-" * (self.a3 - self.cutoff) if self.b2 is None else str(self.b2)
        return f"({b10} {b11})"
def fonk19(b12):
    if b12 = = 1:
        return class2()
    else:
        return class3(b12)
if b13 = = "__main__":
    b14 = fonk19(8)
    b14.fonk13(2, 3.5)
    b14.fonk13(5, 1.2)
    b14.fonk13(6, 4.7)
    print(b14)
    print("Norm2:", b14.b7)
    print("Sample:", b14.fonk15())