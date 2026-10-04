class class1:
    def fonk1(self, b1 = 'max'):
        self.fonk10(b1)
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
        b5 = (len(self.b2) - 2)
        for i in range(b5, -1, -1):
            self.fonk7(i)
    def fonk6(self, b7):
        while b7 > 0:
            b6 = (b7 - 1)
            if self.fonk8(self.b2[b7], self.b2[b6]):
                self.fonk9(b7, b6)
                b7 = b6
            else:
                break
    def fonk7(self, b7):
        while True:
            b8 = 2 * b7 + 1
            b9 = 2 * b7 + 2
            b10 = b7
            if b8 < len(self.b2) and self.fonk8(self.b2[b8], self.b2[b10]):
                b10 = b8
            if b9 < len(self.b2) and self.fonk8(self.b2[b9], self.b2[b10]):
                b10 = b9
            if b10 != b7:
                self.fonk9(b7, b10)
                b7 = b10
            else:
                break
    def fonk8(self, child, b6):
        if self.b1 = = 'max':
            return child > b6
        return child < b6
    def fonk9(self, i, j):
        self.b2[i], self.b2[j] = self.b2[j], self.b2[i]
    def fonk10(self, b1):
        if b1 not in {'max', 'min'}:
            raise ValueError("class1 type must be 'max' or 'min'")
if b11 = = "__main__":
    b12 = class1('max')
    b12.fonk3(10)
    b12.fonk3(20)
    b12.fonk3(5)
    b12.fonk3(15)
    print("Max class1:", b12.b2)
    print("Popped from Max class1:", b12.fonk4())
    print("Max class1 after pop:", b12.b2)
    b13 = class1('min')
    b13.fonk3(10)
    b13.fonk3(20)
    b13.fonk3(5)
    b13.fonk3(15)
    print("Min class1:", b13.b2)
    print("Popped from Min class1:", b13.fonk4())
    print("Min class1 after pop:", b13.b2)