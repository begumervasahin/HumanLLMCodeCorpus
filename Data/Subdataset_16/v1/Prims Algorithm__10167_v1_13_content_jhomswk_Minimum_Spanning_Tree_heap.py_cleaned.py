class class1:
    def fonk1(self, k, v):
        self.b1 = k
        self.b2 = v
    def fonk2(self):
        return "({},{})".format(self.b1, self.b2)
class class2:
    def fonk3(self):
        self.b3 = []
        self.b4 = {}
    def fonk4(self, v):
        return self.b3[self.b4[v]].b1
    def fonk5(self, b9):
        return 2*b9+1
    def fonk6(self, b9):
        return 2*(b9+1)
    def fonk7(self, b9):
        return (b9-1)
    def fonk8(self, b9):
        b5 = self.fonk5(b9)
        b6 = self.fonk6(b9)
        b7 = b9
        if b5 < len(self) and self.b3[b5].b1 < self.b3[b7].b1:
            b7 = b5
        if b6 < len(self) and self.b3[b6].b1 < self.b3[b7].b1:
            b7 = b6
        if b7 != b9:
            self.fonk12(b9, b7)
            self.fonk8(b7)
    def fonk9(self):
        if not self:
            return None
        self.fonk12(0, len(self)-1)
        b8 = self.b3.pop()
        del self.b4[b8.b2]
        self.fonk8(0)
        return (b8.b1, b8.b2)
    def fonk10(self, k, v):
        self.b3.append(class1(k, v))
        self.b4[v] = len(self)-1
        self.fonk11(v, k)
    def fonk11(self, v, k):
        b9 = self.b4[v]
        b10 = self.b3[b9]
        b10.b1 = k
        b11 = self.fonk7(b9)
        while b9 > 0 and k < self.b3[b11].b1:
            self.b3[b9] = self.b3[b11]
            self.b4[self.b3[b11].b2] = b9
            b9, b11 = b11, self.fonk7(b11)
        self.b3[b9] = b10
        self.b4[b10.b2] = b9
    def fonk12(self, b9, j):
        self.b4[self.b3[b9].b2], self.b4[self.b3[j].b2] = j, b9
        self.b3[b9], self.b3[j] = self.b3[j], self.b3[b9]
    def fonk13(self):
        return len(self.b3)
    def fonk14(self):
        return len(self.b3) > 0
    def fonk15(self, v):
        return v in self.b4
if b12 = = "__main__":
    b3 = class2()
    b3.fonk10(3, "apple")
    b3.fonk10(1, "banana")
    b3.fonk10(2, "cherry")
    print("Heap after inserts:", b3.b3)
    print("Extracting b7:", b3.fonk9())
    print("Heap after extracting b7:", b3.b3)
    b3.fonk11("cherry", 0)
    print("Heap after decreasing b1:", b3.b3)