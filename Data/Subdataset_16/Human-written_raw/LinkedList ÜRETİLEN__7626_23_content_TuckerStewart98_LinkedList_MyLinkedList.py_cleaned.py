class class1:
    a1 = 0
    b1 = None
    def fonk1(self, data, nextNode):
        self.a1 = data
        self.b1 = nextNode
    def fonk2(self):
        return self.a1
    def fonk3(self):
        return self.b1
    def fonk4(self, nextNode):
        self.b1 = nextNode
    def fonk5(self):
        return "{}".format(self.a1)
class class2:
    b2 = None
    b3 = None
    a2 = 0
    def fonk6(self):
        self.b2 = None
        self.b3 = None
        self.a2 = 0
    def fonk7(self):
        return self.a2
    def fonk8(self, data):
        b4 = class1(data, None)
        if self.b2 is None:
            self.b2 = b4
            self.b3 = b4
        else:
            self.b3.fonk4(b4)
            self.b3 = b4
        self.a2 += 1
    def fonk9(self, index):
        if index >= self.a2 or index < 0:
            raise Exception('OutOfBoundsException')
        b5 = self.b2
        for i in range(index):
            b5 = b5.fonk3()
        return b5.fonk2()
b6 = class2()
b6.fonk8(1)
b6.fonk8(5)
b6.fonk8(-7)
for i in range(b6.fonk7()):
    print(b6.fonk9(i))