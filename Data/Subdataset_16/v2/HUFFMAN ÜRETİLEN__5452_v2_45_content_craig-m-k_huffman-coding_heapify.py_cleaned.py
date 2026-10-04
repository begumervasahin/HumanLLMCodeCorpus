class class1:
    def fonk1(self, b1 = 'max'):
        if b1 not in {'max', 'min'}:
            raise ValueError("class1 type must be 'max' or 'min'")
        self.b1 = b1
        self.b2 = []
    def fonk2(self):
        return len(self.b2)
    def fonk3(self, key):
        self.b2.append(key)
        self.fonk6(len(self.b2) - 1)
    def fonk4(self):
        if not self.b2:
            raise IndexError("Pop from empty heap")
        b3 = self.b2[0]
        b4 = self.b2.fonk4()
        if self.b2:
            self.b2[0] = b4
            self.fonk7(0)
        return b3
    def fonk5(self, elements):
        self.b2 = elements[:]
        for i in range((len(self.b2) - 2)
            self.fonk7(i)
    def fonk6(self, b6):
        b5 = (b6 - 1)
        while b6 > 0 and self.fonk8(self.b2[b6], self.b2[b5]):
            self.b2[b6], self.b2[b5] = self.b2[b5], self.b2[b6]
            b6 = b5
            b5 = (b6 - 1)
    def fonk7(self, b6):
        b7 = 2 * b6 + 1
        b8 = 2 * b6 + 2
        b9 = b6
        if b7 < len(self.b2) and self.fonk8(self.b2[b7], self.b2[b9]):
            b9 = b7
        if b8 < len(self.b2) and self.fonk8(self.b2[b8], self.b2[b9]):
            b9 = b8
        if b9 != b6:
            self.b2[b6], self.b2[b9] = self.b2[b9], self.b2[b6]
            self.fonk7(b9)
    def fonk8(self, child, b5):
        if self.b1 = = 'max':
            return child > b5
        return child < b5
if b10 = = "__main__":
    b11 = class1('max')
    b11.fonk3(10)
    b11.fonk3(20)
    b11.fonk3(5)
    b11.fonk3(15)
    print("Max class1:", b11.b2)
    print("Popped from Max class1:", b11.fonk4())
    print("Max class1 after pop:", b11.b2)
    b12 = class1('min')
    b12.fonk3(10)
    b12.fonk3(20)
    b12.fonk3(5)
    b12.fonk3(15)
    print("Min class1:", b12.b2)
    print("Popped from Min class1:", b12.fonk4())
    print("Min class1 after pop:", b12.b2)