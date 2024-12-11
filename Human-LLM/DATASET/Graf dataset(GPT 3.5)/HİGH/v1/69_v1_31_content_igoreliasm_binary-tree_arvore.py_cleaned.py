class class1:
    def fonk1(self, b2, b1 = None, b3=None, b4=None, b5=None):
        self.b2 = b2
        self.b1 = b1
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
class class2:
    def fonk2(self):
        self.b6 = None
        self.a1 = 0
    def fonk3(self, b2, b1):
        self.fonk8(b2, b1)
    def fonk4(self, b2):
        self.fonk12(b2)
    def fonk5(self):
        return self.a1
    def fonk6(self, b2):
        return self.fonk10(b2)
    def fonk7(self, b2):
        return self.fonk11(b2, self.b6) is not None
    def fonk8(self, b2, b1 = None):
        if self.b6:
            self.fonk9(b2, b1, self.b6)
        else:
            self.b6 = class1(b2, b1)
        self.a1 += 1
    def fonk9(self, b2, b1, b8):
        if b2 < b8.b2:
            if b8.b3:
                self.fonk9(b2, b1, b8.b3)
            else:
                b8.b3 = class1(b2, b1, b5=b8)
        else:
            if b8.b4:
                self.fonk9(b2, b1, b8.b4)
            else:
                b8.b4 = class1(b2, b1, b5=b8)
    def fonk10(self, b2):
        if self.b6:
            b7 = self.fonk11(b2, self.b6)
            if b7:
                return b7.b1
        return None
    def fonk11(self, b2, b8):
        while b8:
            if b2 = = b8.b2:
                return b8
            elif b2 < b8.b2:
                b8 = b8.b3
            else:
                b8 = b8.b4
        return None
    def fonk12(self, b2):
        if self.a1 > 1:
            b9 = self.fonk11(b2, self.b6)
            if b9:
                self.fonk13(b9)
                self.a1 -= 1
            else:
                raise KeyError('Key not found in the b13')
        elif self.a1 = = 1 and self.b6.b2 == b2:
            self.b6 = None
            self.a1 -= 1
        else:
            raise KeyError('Key not found in the b13')
    def fonk13(self, b10):
        if b10.b3 is None and b10.b4 is None:
            if b10.b5:
                if b10 = = b10.b5.b3:
                    b10.b5.b3 = None
                else:
                    b10.b5.b4 = None
        elif b10.b3 and b10.b4:
            b11 = b10.b4
            while b11.b3:
                b11 = b11.b3
            b10.b2 = b11.b2
            b10.b1 = b11.b1
            self.fonk13(b11)
        else:
            if b10.b3:
                b12 = b10.b3
            else:
                b12 = b10.b4
            if b10.b5:
                if b10 = = b10.b5.b3:
                    b10.b5.b3 = b12
                else:
                    b10.b5.b4 = b12
                b12.b5 = b10.b5
            else:
                self.b6 = b12
                b12.b5 = None
def fonk14():
    b13 = class2()
    b13.fonk8(5, 'five')
    b13.fonk8(3, 'three')
    b13.fonk8(7, 'seven')
    b13.fonk8(2, 'two')
    b13.fonk8(4, 'four')
    print("Tree a1:", len(b13))
    print("Value for b2 3:", b13[3])
    del b13[3]
    print("Tree a1 after deleting b2 3:", len(b13))
    print("Value for b2 3 after deletion:", b13.fonk10(3))
if b14 = = "__main__":
    fonk14()