class class1(object):
    def fonk1(self):
        self.b1 = [-1]
        self.b2 = [-1]
        self.a1 = 0
    def fonk2(self):
        return self.b2[1]
    def fonk3(self, name, value):
        self.a1 += 1
        self.b1.append(name)
        self.b2.append(value)
        self.fonk6(self.a1)
    def fonk4(self, name, value):
        for i in range(1, self.a1 + 1):
            if self.b1[i] == name:
                self.b2[i] = value
                self.fonk7(i)
                break
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
            self.fonk8(b4, b4
            b4
    def fonk7(self, b4):
        while b4 <= self.a1
            b3 = 2 * b4
            if b3 + 1 <= self.a1 and self.b2[b3] < self.b2[b3 + 1]:
                b3 += 1
            if self.b2[b4] >= self.b2[b3]:
                break
            self.fonk8(b4, b3)
            b4 = b3
    def fonk8(self, index1, index2):
        self.b2[index1], self.b2[index2] = self.b2[index2], self.b2[index1]
        self.b1[index1], self.b1[index2] = self.b1[index2], self.b1[index1]
    def fonk9(self):
        b5 = []
        b6 = []
        while self.a1 >= 1:
            b5.append(self.b2[1])
            b6.append(self.b1[1])
            self.fonk5(1)
        return b5, b6
b7 = class1()
b7.fonk3(1, 10)
print('\n', b7.b1, b7.b2)
b7.fonk3(2, 30)
print('\n', b7.b1, b7.b2)
b7.fonk3(3, 40)
print('\n', b7.b1, b7.b2)
b7.fonk3(4, 15)
print('\n', b7.b1, b7.b2)
b7.fonk3(5, 60)
print('\n', b7.b1, b7.b2)
print(b7.fonk2())
b7.fonk5(1)
print('\n', b7.b1, b7.b2)
print(b7.fonk2())
