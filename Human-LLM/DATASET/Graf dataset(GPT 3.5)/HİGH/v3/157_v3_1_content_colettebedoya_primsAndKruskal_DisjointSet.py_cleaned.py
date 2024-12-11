class class1:
    def fonk1(self, b1):
        if b1 < 0:
            raise ValueError("Size must be >= 0")
        self.b1 = b1
        self.b2 = [-1] * (b1 + 1)
    def fonk2(self, x, y):
        if not (0 < x <= self.b1 and 0 < y <= self.b1):
            raise ValueError("Elements out of range")
        b3 = self.fonk3(x)
        b4 = self.fonk3(y)
        if b3 != b4:
            self.b2[b4] = b3
    def fonk3(self, x):
        if not (0 < x <= self.b1):
            raise ValueError("Element out of range")
        if self.b2[x] < 0:
            return x
        else:
            return self.fonk3(self.b2[x])
if b5 = = "__main__":
    b6 = class1(10)
    b6.fonk2(1, 2)
    b6.fonk2(3, 4)
    b6.fonk2(4, 5)
    print(b6.fonk3(5))
