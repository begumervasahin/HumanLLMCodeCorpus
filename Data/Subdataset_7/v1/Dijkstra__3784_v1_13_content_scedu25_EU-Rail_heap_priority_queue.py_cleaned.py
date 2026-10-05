class class1(Exception):
    pass
class class2:
    def fonk1(self, key, value):
        self.b1 = key
        self.b2 = value
class class3:
    def fonk2(self):
        return len(self) == 0
class class4(class3):
    def fonk3(self, j):
        return (j-1)
    def fonk4(self, j):
        return 2*j + 1
    def fonk5(self, j):
        return 2*j + 2
    def fonk6(self, j):
        return self.fonk4(j) < len(self.b7)
    def fonk7(self, j):
        return self.fonk5(j) < len(self.b7)
    def fonk8(self, i, j):
        self.b7[i], self.b7[j] = self.b7[j], self.b7[i]
    def fonk9(self, j):
        b3 = self.fonk3(j)
        if j > 0 and self.b7[j].b1 < self.b7[b3].b1:
            self.fonk8(j, b3)
            self.fonk9(b3)
    def fonk10(self, j):
        if self.fonk6(j):
            b4 = self.fonk4(j)
            b5 = b4
            if self.fonk7(j):
                b6 = self.fonk5(j)
                if self.b7[b6].b1 < self.b7[b4].b1:
                    b5 = b6
            if self.b7[b5].b1 < self.b7[j].b1:
                self.fonk8(j, b5)
                self.fonk10(b5)
    def fonk11(self):
        self.b7 = []
    def fonk12(self):
        return len(self.b7)
    def fonk13(self, key, value):
        self.b7.append(class2(key, value))
        self.fonk9(len(self.b7) - 1)
    def fonk14(self):
        if self.fonk2():
            raise class1('Priority queue is empty.')
        b8 = self.b7[0]
        return (b8.b1, b8.b2)
    def fonk15(self):
        if self.fonk2():
            raise class1('Priority queue is empty.')
        self.fonk8(0, len(self.b7) - 1)
        b8 = self.b7.pop()
        self.fonk10(0)
        return (b8.b1, b8.b2)
b9 = class4()
b9.fonk13(4, 'Four')
b9.fonk13(2, 'Two')
b9.fonk13(1, 'One')
print(b9.fonk14())
print(b9.fonk15())
print(len(b9))
