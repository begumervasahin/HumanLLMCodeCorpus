class class1:
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
        print(value)
        print(self.a1)
    def fonk5(self, b4):
        if self.a1 = = 1 or b4 == self.a1:
            self.b2.pop()
            self.b1.pop()
            self.a1 -= 1
        else:
            self.b2[b4] = self.b2.pop()
            self.b1[b4] = self.b1.pop()
            self.a1 -= 1
            self.fonk7(b4)
    def fonk6(self, b4):
        while b4 > 1 and self.b2[b4] > self.b2[b4
            self.fonk9(b4, b4
            b4
    def fonk7(self, b4):
        while b4 <= self.a1
            b3 = self.fonk8(b4)
            if self.b2[b4] < self.b2[b3]:
                self.fonk9(b4, b3)
                b4 = b3
            else:
                break
    def fonk8(self, b4):
        b5 = 2 * b4
        b6 = 2 * b4 + 1 if 2 * b4 + 1 <= self.a1 else None
        if b6 and self.b2[b5] < self.b2[b6]:
            return b6
        else:
            return b5
    def fonk9(self, index1, index2):
        self.b2[index1], self.b2[index2] = self.b2[index2], self.b2[index1]
        self.b1[index1], self.b1[index2] = self.b1[index2], self.b1[index1]
    def fonk10(self):
        b7 = []
        b8 = []
        while self.a1 >= 1:
            b7.append(self.b1[1])
            b8.append(self.b2[1])
            self.fonk5(1)
        return [b8, b7]
b9 = class1()
b9.fonk3(1, 10)
print('\n', b9.b1, b9.b2)
b9.fonk3(2, 30)
print('\n', b9.b1, b9.b2)
b9.fonk3(3, 40)
print('\n', b9.b1, b9.b2)
b9.fonk3(4, 15)
print('\n', b9.b1, b9.b2)
b9.fonk3(5, 60)
print('\n', b9.b1, b9.b2)
print(b9.fonk2())
b9.fonk5(1)
print('\n', b9.b1, b9.b2)
print(b9.fonk2())