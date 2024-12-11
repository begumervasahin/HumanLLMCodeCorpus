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
    def fonk5(self, index):
        if self.a1 = = 1 or index == self.a1:
            self.b2.pop()
            self.b1.pop()
            self.a1 -= 1
        else:
            self.b2[index] = self.b2.pop()
            self.b1[index] = self.b1.pop()
            self.a1 -= 1
            self.fonk7(index)
    def fonk6(self, index):
        if index > 1 and self.b2[index] > self.b2[index
            b3 = index
            while b3 > 1 and self.b2[b3] > self.b2[b3
                self.fonk8(b3, b3
                b3
    def fonk7(self, index):
        if index <= self.a1
            b3 = index
            while b3 <= self.a1
                b4 = 2 * b3
                if (2 * b3 + 1) <= self.a1 and self.b2[2 * b3] < self.b2[2 * b3 + 1]:
                    b4 = 2 * b3 + 1
                self.fonk8(b3, b4)
                b3 = b4
    def fonk8(self, index1, index2):
        self.b2[index1], self.b2[index2] = self.b2[index2], self.b2[index1]
        self.b1[index1], self.b1[index2] = self.b1[index2], self.b1[index1]
    def fonk9(self):
        b5 = []
        b6 = []
        while self.a1 >= 1:
            b5.append(self.b1[1])
            b6.append(self.b2[1])
            self.fonk5(1)
        return [b6, b5]
'''
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
'''
'''
b7 = class1()
b7.fonk3(3)
print(b7.b2)
b7.fonk3(2)
print(b7.b2)
b7.fonk3(1)
print(b7.b2)
b7.fonk3(15)
print(b7.b2)
b7.fonk3(5)
print(b7.b2)
b7.fonk3(4)
print(b7.b2)
b7.fonk3(45)
print(b7.b2)
b7.fonk5(1)
print(b7.b2)
print(b7.fonk2())
b7.fonk3(677)
print(b7.b2)
print(b7.fonk2())
'''