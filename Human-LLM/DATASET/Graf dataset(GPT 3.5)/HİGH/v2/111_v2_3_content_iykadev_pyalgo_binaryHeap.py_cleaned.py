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
        b4 = b2 * 2
        b5 = (b2 * 2) + 1
        if b5 > self.a1:
            return b4
        else:
            if self.b1[b4] < self.b1[b5]:
                return b4
            else:
                return b5
    def fonk6(self):
        if self.a1 = = 0:
            return None
        b6 = self.b1[1]
        self.b1[1] = self.b1[self.a1]
        self.a1 -= 1
        self.b1.pop()
        self.fonk4(1)
        return b6
    def fonk7(self, alist):
        b7 = len(alist)
        self.a1 = len(alist)
        self.b1 = [0] + alist[:]
        for b2 in range(b7, 0, -1):
            self.fonk4(b2)
b8 = class1()
b8.fonk7([9, 5, 6, 2, 3])
print(b8.fonk6())
print(b8.fonk6())
print(b8.fonk6())
print(b8.fonk6())
print(b8.fonk6())