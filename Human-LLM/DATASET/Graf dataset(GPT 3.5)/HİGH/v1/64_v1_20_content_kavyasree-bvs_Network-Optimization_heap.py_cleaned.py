class class1(object):
    def fonk1(self):
        self.b1 = [-1]
        self.b2 = [-1]
        self.a1 = 0
    def fonk2(self):
        return self.b1[1]
    def fonk3(self, name, value):
        self.a1 += 1
        self.b1.append(name)
        self.b2.append(value)
        self.fonk6(self.a1)
    def fonk4(self, name, value):
        for i in range(1, self.a1 + 1):
            if self.b1[i] == name:
                self.b2[i] = value
                self.fonk6(i)
                break
    def fonk5(self, b3):
        if self.a1 = = 1 or b3 == self.a1:
            self.b2.pop()
            self.b1.pop()
            self.a1 -= 1
        else:
            self.b2[b3] = self.b2.pop()
            self.b1[b3] = self.b1.pop()
            self.a1 -= 1
            self.fonk6(b3)
    def fonk6(self, b5):
        if b5 > 1 and self.b2[b5] > self.b2[b5
            b3 = b5
            while b3 > 1 and self.b2[b3] > self.b2[b3
                self.fonk7(b3, b3
                b3
        else:
            while b5 <= self.a1
                b4 = 2 * b5
                if 2 * b5 + 1 <= self.a1 and self.b2[2 * b5] < self.b2[2 * b5 + 1]:
                    b4 = 2 * b5 + 1
                self.fonk7(b5, b4)
                b5 = b4
    def fonk7(self, b3, b4):
        self.b2[b3], self.b2[b4] = self.b2[b4], self.b2[b3]
        self.b1[b3], self.b1[b4] = self.b1[b4], self.b1[b3]
    def fonk8(self):
        b6 = []
        b7 = []
        while self.a1 >= 1:
            b6.append(self.b1[1])
            b7.append(self.b2[1])
            self.fonk5(1)
        return b7, b6
b8 = class1()
b8.fonk3(1, 10)
print('\a1', b8.b1, b8.b2)
b8.fonk3(2, 30)
print('\a1', b8.b1, b8.b2)
b8.fonk3(3, 40)
print('\a1', b8.b1, b8.b2)
b8.fonk3(4, 15)
print('\a1', b8.b1, b8.b2)
b8.fonk3(5, 60)
print('\a1', b8.b1, b8.b2)
print(b8.fonk2())
b8.fonk5(1)
print('\a1', b8.b1, b8.b2)
print(b8.fonk2())
