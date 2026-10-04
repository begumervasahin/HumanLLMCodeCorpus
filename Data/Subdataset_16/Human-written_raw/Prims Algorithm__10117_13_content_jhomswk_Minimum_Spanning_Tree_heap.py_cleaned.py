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
    def fonk5(self, b8):
        return 2*b8+1
    def fonk6(self, b8):
        return 2*(b8+1)
    def fonk7(self, b8):
        return (b8-1)
    def fonk8(self, b8):
        b5 = self.fonk5(b8)
        b6 = self.fonk6(b8)
        b7 = b8
        if b5 < len(self) and self.b3[b5].b1 < self.b3[b7].b1:
            b7 = b5
        if b6 < len(self) and self.b3[b6].b1 < self.b3[b7].b1:
            b7 = b6
        if b7 != b8:
            self.fonk12(b8, b7)
            self.fonk8(b7)
    def fonk9(self):
        if not self:
            return None
        self.fonk12(0, len(self)-1)
        b7 = self.b3.pop()
        del self.b4[b7.b2]
        self.fonk8(0)
        return (b7.b1, b7.b2)
    def fonk10(self, k, v):
        self.b3.append(class1(k,v))
        self.b4[v] = len(self)-1
        self.fonk11(v,k)
    def fonk11(self, v, k):
        b8 = self.b4[v]
        b9 = self.b3[b8]
        b9.b1 = k
        b10 = self.fonk7(b8)
        while b8 > 0 and k < self.b3[b10].b1:
            self.b3[b8] = self.b3[b10]
            self.b4[self.b3[b10].b2] = b8
            b8, b10 = b10, self.fonk7(b10)
        self.b3[b8] = b9
        self.b4[b9.b2] = b8
    def fonk12(self, b8, j):
        self.b4[self.b3[b8].b2], self.b4[self.b3[j].b2] = j, b8
        self.b3[b8], self.b3[j] = self.b3[j], self.b3[b8]
    def fonk13(self):
        return len(self.b3)
    def fonk14(self):
        return len(self.b3) > 0
    def fonk15(self, v):
        return v in self.b4