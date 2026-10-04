class class1:
    def fonk1(self, b2: str):
        if b2 not in {'max', 'min'}:
            raise ValueError("b2 must be either 'max' or 'min'")
        self.b1 = []
        self.b2 = b2
    def fonk2(self) -> int:
        return len(self.b1)
    def fonk3(self, key):
        self.b1.append(key)
        self.fonk6(len(self.b1) - 1)
    def fonk4(self):
        if not self.b1:
            raise IndexError("pop from empty heap")
        self.fonk9(0, len(self.b1) - 1)
        b3 = self.b1.fonk4()
        if self.b1:
            self.fonk7(0)
        return b3
    def fonk5(self):
        for i in range((len(self.b1)
            self.fonk7(i)
    def fonk6(self, b5: int):
        b4 = (b5 - 1)
        while b5 > 0 and self.fonk8(self.b1[b4], self.b1[b5]):
            self.fonk9(b5, b4)
            b5 = b4
            b4 = (b5 - 1)
    def fonk7(self, b5: int):
        b6 = 2 * b5 + 1
        b7 = 2 * b5 + 2
        b8 = b5
        if b6 < len(self.b1) and self.fonk8(self.b1[b8], self.b1[b6]):
            b8 = b6
        if b7 < len(self.b1) and self.fonk8(self.b1[b8], self.b1[b7]):
            b8 = b7
        if b8 != b5:
            self.fonk9(b5, b8)
            self.fonk7(b8)
    def fonk8(self, parent_val, child_val) -> bool:
        if self.b2 = = 'max':
            return parent_val < child_val
        return parent_val > child_val
    def fonk9(self, i: int, j: int):
        self.b1[i], self.b1[j] = self.b1[j], self.b1[i]