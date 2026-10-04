class class1:
    def fonk1(self, data, b1 = None):
        self.b2 = data
        self.b3 = b1
    def fonk2(self):
        return self.b2
    def fonk3(self):
        return self.b3
    def fonk4(self, b1):
        self.b3 = b1
    def fonk5(self):
        return "{}".format(self.b2)
class class2:
    def fonk6(self):
        self.b4 = None
        self.b5 = None
        self.a1 = 0
    def fonk7(self):
        return self.a1
    def fonk8(self, data):
        b6 = class1(data)
        if self.b4 is None:
            self.b4 = b6
            self.b5 = b6
        else:
            self.b5.fonk4(b6)
            self.b5 = b6
        self.a1 += 1
    def fonk9(self, index):
        if index >= self.a1 or index < 0:
            raise Exception('OutOfBoundsException')
        b7 = self.b4
        for i in range(index):
            b7 = b7.fonk3()
        return b7.fonk2()
if b8 = = "__main__":
    b9 = class2()
    b9.fonk8(1)
    b9.fonk8(5)
    b9.fonk8(-7)
    for i in range(b9.fonk7()):
        print(b9.fonk9(i))