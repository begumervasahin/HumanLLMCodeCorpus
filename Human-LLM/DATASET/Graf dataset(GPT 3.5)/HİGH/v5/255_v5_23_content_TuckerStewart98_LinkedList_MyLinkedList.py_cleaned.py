class class1:
    def fonk1(self, b2, b1 = None):
        self.b2 = b2
        self.b1 = b1
    def fonk2(self):
        return str(self.b2)
class class2:
    def fonk3(self):
        self.b3 = None
        self.b4 = None
        self.a1 = 0
    def fonk4(self):
        return self.a1
    def fonk5(self, b2):
        b5 = class1(b2)
        if not self.b3:
            self.b3 = b5
        else:
            self.b4.b1 = b5
        self.b4 = b5
        self.a1 += 1
    def fonk6(self, index):
        if index < 0 or index >= self.a1:
            raise IndexError('Index out of bounds')
        b6 = self.b3
        for _ in range(index):
            b6 = b6.b1
        return b6.b2
b7 = class2()
b7.fonk5(1)
b7.fonk5(5)
b7.fonk5(-7)
for i in range(len(b7)):
    print(b7.fonk6(i))