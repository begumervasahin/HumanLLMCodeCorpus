class class1:
    def fonk1(self):
        self.b1 = [0]
        self.a1 = 0
    def fonk2(self, b3):
        while b3
            if self.b1[b3] < self.b1[b3
                b2 = self.b1[b3
                self.b1[b3
                self.b1[b3] = b2
            b3 = b3
    def fonk3(self, k):
        self.b1.append(k)
        self.a1 = self.a1 + 1
        self.fonk2(self.a1)
    def fonk4(self, b3):
        while (b3 * 2) <= self.a1:
            b4 = self.fonk5(b3)
            if self.b1[b3] > self.b1[b4]:
                b2 = self.b1[b3]
                self.b1[b3] = self.b1[b4]
                self.b1[b4] = b2
            b3 = b4
    def fonk5(self, b3):
        if b3 * 2 + 1 > self.a1:
            return b3 * 2
        else:
            if self.b1[b3*2] < self.b1[b3*2+1]:
                return b3 * 2
            else:
                return b3 * 2 + 1
    def fonk6(self):
        if self.a1 = = 0:
            return None
        b5 = self.b1[1]
        self.b1[1] = self.b1[self.a1]
        self.a1 = self.a1 - 1
        self.b1.pop()
        self.fonk4(1)
        return b5
    def fonk7(self, alist):
        b3 = len(alist)
        self.a1 = len(alist)
        self.b1 = [0] + alist[:]
        while b3 > 0:
            self.fonk4(b3)
            b3 = b3 - 1
b6 = class1()
b6.fonk7([9, 5, 6, 2, 3])
print(b6.fonk6())
print(b6.fonk6())
print(b6.fonk6())
print(b6.fonk6())
print(b6.fonk6())