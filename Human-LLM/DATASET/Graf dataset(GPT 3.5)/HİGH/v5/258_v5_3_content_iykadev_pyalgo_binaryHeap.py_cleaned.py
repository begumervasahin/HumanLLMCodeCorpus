class class1:
    def fonk1(self):
        self.b1 = [0]
        self.a1 = 0
    def fonk2(self, b3):
        while b3
            if self.b1[b3] < self.b1[b3
                self.b1[b3], self.b1[b3
            b3
    def fonk3(self, k):
        self.b1.append(k)
        self.a1 += 1
        self.fonk2(self.a1)
    def fonk4(self, b3):
        while (b3 * 2) <= self.a1:
            b2 = self.fonk5(b3)
            if self.b1[b3] > self.b1[b2]:
                self.b1[b3], self.b1[b2] = self.b1[b2], self.b1[b3]
            b3 = b2
    def fonk5(self, b3):
        b4 = b3 * 2
        b5 = b4 + 1
        if b5 > self.a1:
            return b4
        else:
            return b4 if self.b1[b4] < self.b1[b5] else b5
    def fonk6(self):
        if self.a1 = = 0:
            raise IndexError("Cannot delete from an empty heap")
        b6 = self.b1[1]
        self.b1[1] = self.b1[self.a1]
        self.a1 -= 1
        self.b1.pop()
        self.fonk4(1)
        return b6
    def fonk7(self, alist):
        self.a1 = len(alist)
        self.b1 = [0] + alist[:]
        for b3 in range(self.a1
            self.fonk4(b3)
b7 = class1()
b7.fonk7([9, 5, 6, 2, 3])
print(b7.fonk6())
print(b7.fonk6())
print(b7.fonk6())
print(b7.fonk6())
print(b7.fonk6())