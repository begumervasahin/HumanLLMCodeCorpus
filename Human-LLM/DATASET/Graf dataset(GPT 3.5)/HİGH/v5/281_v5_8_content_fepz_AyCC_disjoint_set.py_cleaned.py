class class1:
    def fonk1(self, b1):
        self.b1 = list(b1)
        self.b2 = list(range(len(b1)))
        self.b3 = [1] * len(b1)
    def fonk2(self, x):
        b4 = self.b1.index(x)
        b5 = b4
        while self.b2[b5] != b5:
            b5 = self.b2[b5]
        while b4 != b5:
            b6 = self.b2[b4]
            self.b2[b4] = b5
            b4 = b6
        return b5
    def fonk3(self, a, b):
        if self.b3[a] == self.b3[b]:
            self.b3[a] += 1
            self.b2[b] = a
        elif self.b3[a] > self.b3[b]:
            self.b2[b] = a
        else:
            self.b2[a] = b