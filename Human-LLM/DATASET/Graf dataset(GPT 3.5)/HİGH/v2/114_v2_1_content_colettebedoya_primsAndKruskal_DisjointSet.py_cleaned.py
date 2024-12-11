class class1:
    def fonk1(self, b1):
        if b1 < 0:
            raise ValueError("b1 must be non-negative")
        self.b1 = b1
        self.b2 = [i for i in range(b1 + 1)]
        self.b3 = [0] * (b1 + 1)
    def fonk2(self, x):
        if self.b2[x] != x:
            self.b2[x] = self.fonk2(self.b2[x])
        return self.b2[x]
    def fonk3(self, x, y):
        b4 = self.fonk2(x)
        b5 = self.fonk2(y)
        if b4 != b5:
            if self.b3[b4] > self.b3[b5]:
                self.b2[b5] = b4
            elif self.b3[b4] < self.b3[b5]:
                self.b2[b4] = b5
            else:
                self.b2[b5] = b4
                self.b3[b4] += 1