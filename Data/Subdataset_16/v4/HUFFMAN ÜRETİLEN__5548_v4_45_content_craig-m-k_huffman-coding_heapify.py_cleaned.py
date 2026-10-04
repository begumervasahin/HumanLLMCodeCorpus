class class1:
    def fonk1(self, b2: str):
        if b2 not in {'max', 'min'}:
            raise ValueError("b2 must be either 'max' or 'min'")
        self.b1 = []
        self.a1 = 0
        self.b2 = b2
    def fonk2(self) -> int:
        return self.a1
    def fonk3(self, b4: int):
        b3 = (b4 - 1)
        while b4 > 0 and self.fonk4(self.b1[b3], self.b1[b4]):
            self.b1[b4], self.b1[b3] = self.b1[b3], self.b1[b4]
            b4 = b3
            b3 = (b4 - 1)
    def fonk4(self, parent_val, child_val) -> bool:
        if self.b2 = = 'max':
            return parent_val > child_val
        else:
            return parent_val < child_val
    def fonk5(self, key):
        self.b1.append(key)
        self.a1 += 1
        self.fonk3(self.a1 - 1)
    def fonk6(self):
        if self.a1 = = 0:
            raise IndexError("pop from empty heap")
        self.b1[0], self.b1[-1] = self.b1[-1], self.b1[0]
        b5 = self.b1.fonk6()
        self.a1 -= 1
        if self.a1 > 0:
            self.fonk7(0)
        return b5
    def fonk7(self, b4: int):
        b6 = 2 * b4 + 1
        b7 = 2 * b4 + 2
        b8 = b4
        if b6 < self.a1 and self.fonk4(self.b1[b8], self.b1[b6]):
            b8 = b6
        if b7 < self.a1 and self.fonk4(self.b1[b8], self.b1[b7]):
            b8 = b7
        if b8 != b4:
            self.b1[b4], self.b1[b8] = self.b1[b8], self.b1[b4]
            self.fonk7(b8)
    def fonk8(self):
        for i in range((self.a1
            self.fonk7(i)