class class1(Exception):
    pass
class class2:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
class class3:
    def fonk2(self):
        return len(self) == 0
class class4(class3):
    def fonk3(self):
        self.b3 = []
    def fonk4(self):
        return len(self.b3)
    def fonk5(self, j):
        return (j - 1)
    def fonk6(self, j):
        return 2 * j + 1
    def fonk7(self, j):
        return 2 * j + 2
    def fonk8(self, j):
        return self.fonk6(j) < len(self.b3)
    def fonk9(self, j):
        return self.fonk7(j) < len(self.b3)
    def fonk10(self, i, j):
        self.b3[i], self.b3[j] = self.b3[j], self.b3[i]
    def fonk11(self, j):
        b4 = self.fonk5(j)
        if j > 0 and self.b3[j].b1 < self.b3[b4].b1:
            self.fonk10(j, b4)
            self.fonk11(b4)
    def fonk12(self, j):
        if self.fonk8(j):
            b5 = self.fonk6(j)
            b6 = b5
            if self.fonk9(j):
                b7 = self.fonk7(j)
                if self.b3[b7].b1 < self.b3[b5].b1:
                    b6 = b7
            if self.b3[b6].b1 < self.b3[j].b1:
                self.fonk10(j, b6)
                self.fonk12(b6)
    def fonk13(self, b1, b2):
        self.b3.append(class2(b1, b2))
        self.fonk11(len(self.b3) - 1)
    def fonk14(self):
        if self.fonk2():
            raise class1('Priority queue is empty.')
        b8 = self.b3[0]
        return (b8.b1, b8.b2)
    def fonk15(self):
        if self.fonk2():
            raise class1('Priority queue is empty.')
        self.fonk10(0, len(self.b3) - 1)
        b8 = self.b3.pop()
        self.fonk12(0)
        return (b8.b1, b8.b2)
b9 = class4()
b9.fonk13(4, 'Four')
b9.fonk13(2, 'Two')
b9.fonk13(1, 'One')
print(b9.fonk14())
print(b9.fonk15())
print(len(b9))
