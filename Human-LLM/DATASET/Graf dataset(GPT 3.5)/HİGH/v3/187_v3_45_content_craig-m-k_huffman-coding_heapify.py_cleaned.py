class class1:
    def fonk1(self, b1):
        if b1 not in ('max', 'min'):
            raise ValueError('Invalid heap type. Use "max" or "min".')
        self.b1 = b1
        self.b2 = []
        self.a1 = 0
    def fonk2(self):
        return len(self.b2)
    def fonk3(self, b4):
        b3 = (b4 + 1)
        while b4 > 0 and ((self.b1 = = 'max' and self.b2[b3] < self.b2[b4]) or
                             (self.b1 = = 'min' and self.b2[b3] > self.b2[b4])):
            self.b2[b4], self.b2[b3] = self.b2[b3], self.b2[b4]
            b4 = b3
            b3 = (b4 + 1)
    def fonk4(self, key):
        self.b2.append(key)
        self.a1 += 1
        self.fonk3(self.a1 - 1)
    def fonk5(self):
        b5 = self.a1 - 1
        self.b2[b5], self.b2[0] = self.b2[0], self.b2[b5]
        b6 = self.b2.fonk5()
        self.a1 -= 1
        self.fonk6(0)
        return b6
    def fonk6(self, b4):
        b7 = 2 * b4 + 1
        b8 = 2 * b4 + 2
        b9 = self.a1
        if self.b1 = = 'max':
            b10 = b4
            if b7 < b9 and self.b2[b7] > self.b2[b10]:
                b10 = b7
            if b8 < b9 and self.b2[b8] > self.b2[b10]:
                b10 = b8
            if b10 != b4:
                self.b2[b4], self.b2[b10] = self.b2[b10], self.b2[b4]
                self.fonk6(b10)
        else:
            b11 = b4
            if b7 < b9 and self.b2[b7] < self.b2[b11]:
                b11 = b7
            if b8 < b9 and self.b2[b8] < self.b2[b11]:
                b11 = b8
            if b11 != b4:
                self.b2[b4], self.b2[b11] = self.b2[b11], self.b2[b4]
                self.fonk6(b11)
    def fonk7(self):
        b9 = self.a1
        for i in range(b9
            self.fonk6(i)
b12 = class1('max')
b12.fonk4(4)
b12.fonk4(1)
b12.fonk4(7)
b12.fonk4(3)
print("Max class1:", b12.b2)
b13 = class1('min')
b13.fonk4(4)
b13.fonk4(1)
b13.fonk4(7)
b13.fonk4(3)
print("Min class1:", b13.b2)