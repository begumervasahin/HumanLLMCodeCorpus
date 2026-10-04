class class1:
    def fonk1(self, b1 = 'max'):
        if b1 not in {'max', 'min'}:
            raise ValueError("class1 type must be 'max' or 'min'")
        self.b1 = b1
        self.b2 = []
    def fonk2(self):
        return len(self.b2)
    def fonk3(self, b4):
        b3 = (b4 - 1)
        while b4 > 0:
            if (self.b1 = = 'max' and self.b2[b4] > self.b2[b3]) or \
               (self.b1 = = 'min' and self.b2[b4] < self.b2[b3]):
                self.b2[b4], self.b2[b3] = self.b2[b3], self.b2[b4]
                b4 = b3
                b3 = (b4 - 1)
            else:
                break
    def fonk4(self, key):
        self.b2.append(key)
        self.fonk3(len(self.b2) - 1)
    def fonk5(self):
        if not self.b2:
            raise IndexError("Pop from empty heap")
        b5 = self.b2[0]
        b6 = self.b2.fonk5()
        if self.b2:
            self.b2[0] = b6
            self.fonk6(0)
        return b5
    def fonk6(self, b4):
        b7 = 2 * b4 + 1
        b8 = 2 * b4 + 2
        if self.b1 = = 'max':
            self.fonk7(b4, b7, b8)
        else:
            self.fonk8(b4, b7, b8)
    def fonk7(self, b4, b7, b8):
        b9 = b4
        if b7 < len(self.b2) and self.b2[b7] > self.b2[b9]:
            b9 = b7
        if b8 < len(self.b2) and self.b2[b8] > self.b2[b9]:
            b9 = b8
        if b9 != b4:
            self.b2[b4], self.b2[b9] = self.b2[b9], self.b2[b4]
            self.fonk6(b9)
    def fonk8(self, b4, b7, b8):
        b10 = b4
        if b7 < len(self.b2) and self.b2[b7] < self.b2[b10]:
            b10 = b7
        if b8 < len(self.b2) and self.b2[b8] < self.b2[b10]:
            b10 = b8
        if b10 != b4:
            self.b2[b4], self.b2[b10] = self.b2[b10], self.b2[b4]
            self.fonk6(b10)
    def fonk9(self):
        for i in range((len(self.b2) - 2)
            self.fonk6(i)
if b11 = = "__main__":
    b12 = class1('max')
    b12.fonk4(10)
    b12.fonk4(20)
    b12.fonk4(5)
    b12.fonk4(15)
    print("Max class1:", b12.b2)
    print("Popped from Max class1:", b12.fonk5())
    print("Max class1 after pop:", b12.b2)
    b13 = class1('min')
    b13.fonk4(10)
    b13.fonk4(20)
    b13.fonk4(5)
    b13.fonk4(15)
    print("Min class1:", b13.b2)
    print("Popped from Min class1:", b13.fonk5())
    print("Min class1 after pop:", b13.b2)