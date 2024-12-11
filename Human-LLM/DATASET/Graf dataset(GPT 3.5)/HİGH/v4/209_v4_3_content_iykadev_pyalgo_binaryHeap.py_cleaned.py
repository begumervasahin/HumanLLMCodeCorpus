class class1:
    def fonk1(self):
        self.b1 = [0]
        self.a1 = 0
    def fonk2(self, b2):
        while b2
            if self.b1[b2] < self.b1[b2
                self.b1[b2], self.b1[b2
            b2 = b2
    def fonk3(self, k):
        self.b1.append(k)
        self.a1 += 1
        self.fonk2(self.a1)
    def fonk4(self, b2):
        while (b2 * 2) <= self.a1:
            b3 = self.fonk5(b2)
            if self.b1[b2] > self.b1[b3]:
                self.b1[b2], self.b1[b3] = self.b1[b3], self.b1[b2]
            b2 = b3
    def fonk5(self, b2):
        if b2 * 2 + 1 > self.a1:
            return b2 * 2
        else:
            if self.b1[b2 * 2] < self.b1[b2 * 2 + 1]:
                return b2 * 2
            else:
                return b2 * 2 + 1
    def fonk6(self):
        b4 = self.b1[1]
        self.b1[1] = self.b1[self.a1]
        self.a1 -= 1
        self.b1.pop()
        self.fonk4(1)
        return b4
    def fonk7(self, alist):
        b2 = len(alist)
        self.a1 = len(alist)
        self.b1 = [0] + alist[:]
        while b2 > 0:
            self.fonk4(b2)
            b2 -= 1
b5 = class1()
b5.fonk7([9, 5, 6, 2, 3])
print(b5.fonk6())
print(b5.fonk6())
print(b5.fonk6())
print(b5.fonk6())
print(b5.fonk6())