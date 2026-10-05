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
    def fonk6(self, b8):
        b3 = self.fonk4(b8)
        b4 = self.fonk5(b8)
        if self.b2 = = 'min':
            b5 = b8
            if b3 < self.a1 and self.b1[b3] < self.b1[b8]:
                b5 = b3
            if b4 < self.a1 and self.b1[b4] < self.b1[b5]:
                b5 = b4
            if b5 != b8:
                self.b1[b8], self.b1[b5] = self.b1[b5], self.b1[b8]
                self.fonk6(b5)
        else:
            b6 = b8
            if b3 < self.a1 and self.b1[b3] > self.b1[b8]:
                b6 = b3
            if b4 < self.a1 and self.b1[b4] > self.b1[b6]:
                b6 = b4
            if b6 != b8:
                self.b1[b8], self.b1[b6] = self.b1[b6], self.b1[b8]
                self.fonk6(b6)
    def fonk7(self, b8):
        b7 = self.fonk3(b8)
        if self.b2 = = 'min':
            while b8 > 0 and self.b1[b7] > self.b1[b8]:
                self.b1[b8], self.b1[b7] = self.b1[b7], self.b1[b8]
                b8 = b7
                b7 = self.fonk3(b8)
        else:
            while b8 > 0 and self.b1[b7] < self.b1[b8]:
                self.b1[b8], self.b1[b7] = self.b1[b7], self.b1[b8]
                b8 = b7
                b7 = self.fonk3(b8)
    def fonk8(self, key):
        self.b1.append(key)
        self.a1 += 1
        self.fonk7(self.a1 - 1)
    def fonk9(self):
        if not self.b1:
            raise IndexError("class1 is empty")
        b9 = self.b1[0]
        self.b1[0] = self.b1.fonk9()
        self.a1 -= 1
        if self.a1 > 0:
            self.fonk6(0)
        return b9
    def fonk10(self):
        for i in range(self.a1
            self.fonk6(i)