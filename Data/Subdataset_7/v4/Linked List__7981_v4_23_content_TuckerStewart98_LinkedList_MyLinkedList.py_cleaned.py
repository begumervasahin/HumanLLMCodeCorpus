class class1:
    def fonk1(self, data, next_node):
        self.b1 = data
        self.b2 = next_node
    def fonk2(self):
        return self.b1
    def fonk3(self):
        return self.b2
    def fonk4(self, next_node):
        self.b2 = next_node
    def fonk5(self):
        return "{}".format(self.b1)
class class2:
    def fonk6(self):
        self.b3 = None
        self.b4 = None
        self.a1 = 0
    def fonk7(self):
        return self.a1
    def fonk8(self, data):
        b5 = class1(data, None)
        if self.b3 is None:
            self.b3 = b5
            self.b4 = b5
        else:
            self.b4.fonk4(b5)
            self.b4 = b5
        self.a1 += 1
    def fonk9(self, index):
        if index >= self.a1 or index < 0:
            raise IndexError('Index out of bounds')
        b6 = self.b3
        for i in range(index):
            b6 = b6.fonk3()
        return b6.fonk2()
b7 = class2()
b7.fonk8(1)
b7.fonk8(5)
b7.fonk8(-7)
for i in range(b7.fonk7()):
    print(b7.fonk9(i))