class class1:
    def fonk1(self):
        self.b1 = [0]
        self.a1 = 0
    def fonk2(self, key):
        self.b1.append(key)
        self.a1 += 1
        self.fonk5(self.a1)
    def fonk3(self):
        if self.a1 = = 0:
            return None
        b2 = self.b1[1]
        self.b1[1] = self.b1[self.a1]
        self.a1 -= 1
        self.b1.pop()
        self.fonk6(1)
        return b2
    def fonk4(self, alist):
        self.a1 = len(alist)
        self.b1 = [0] + alist[:]
        b3 = len(alist)
        for b5 in range(b3, 0, -1):
            self.fonk6(b5)
    def fonk5(self, b5):
        while b5
            if self.b1[b5] < self.b1[b5
                self.fonk8(b5, b5
            b5
    def fonk6(self, b5):
        while b5 * 2 <= self.a1:
            b4 = self.fonk7(b5)
            if self.b1[b5] > self.b1[b4]:
                self.fonk8(b5, b4)
            b5 = b4
    def fonk7(self, b5):
        b6 = b5 * 2
        b7 = b6 + 1
        if b7 > self.a1:
            return b6
        else:
            return b6 if self.b1[b6] < self.b1[b7] else b7
    def fonk8(self, b5, j):
        self.b1[b5], self.b1[j] = self.b1[j], self.b1[b5]
b8 = class1()
b8.fonk4([9, 5, 6, 2, 3])
print(b8.fonk3())
print(b8.fonk3())
print(b8.fonk3())
print(b8.fonk3())
print(b8.fonk3())