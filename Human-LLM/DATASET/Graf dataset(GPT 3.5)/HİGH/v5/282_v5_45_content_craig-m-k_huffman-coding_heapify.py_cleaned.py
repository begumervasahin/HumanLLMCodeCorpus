class class1:
    def fonk1(self, b2):
        if b2 not in ('max', 'min'):
            raise ValueError('Invalid heap type. Allowed values are "max" or "min".')
        self.b1 = []
        self.a1 = 0
        self.b2 = b2
    def fonk2(self):
        return len(self.b1)
    def fonk3(self, i):
        return (i - 1)
    def fonk4(self, i):
        return 2 * i + 1
    def fonk5(self, i):
        return 2 * i + 2
    def fonk6(self, parent_idx, child_idx):
        b3 = self.b1[parent_idx]
        b4 = self.b1[child_idx]
        if self.b2 = = 'min':
            return b4 < b3
        else:
            return b4 > b3
    def fonk7(self, b10):
        b5 = self.fonk4(b10)
        b6 = self.fonk5(b10)
        b7 = min if self.b2 == 'min' else max
        if b5 < self.a1 and self.fonk6(b10, b5):
            b8 = b5
        else:
            b8 = b10
        if b6 < self.a1 and self.fonk6(b8, b6):
            b8 = b6
        if b8 != b10:
            self.b1[b10], self.b1[b8] = self.b1[b8], self.b1[b10]
            self.fonk7(b8)
    def fonk8(self, b10):
        b9 = self.fonk3(b10)
        b7 = min if self.b2 == 'min' else max
        while b10 > 0 and self.fonk6(b9, b10):
            self.b1[b10], self.b1[b9] = self.b1[b9], self.b1[b10]
            b10 = b9
            b9 = self.fonk3(b10)
    def fonk9(self, key):
        self.b1.append(key)
        self.a1 += 1
        self.fonk8(self.a1 - 1)
    def fonk10(self):
        if not self.b1:
            raise IndexError("class1 is empty")
        b11 = self.b1[0]
        self.b1[0] = self.b1.fonk10()
        self.a1 -= 1
        if self.a1 > 0:
            self.fonk7(0)
        return b11
    def fonk11(self):
        for i in range(self.a1
            self.fonk7(i)