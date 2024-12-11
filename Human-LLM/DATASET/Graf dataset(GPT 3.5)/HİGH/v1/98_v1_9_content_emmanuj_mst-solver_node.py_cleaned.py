class class1:
    def fonk1(self, val):
        self.b1 = val
        self.b2 = self
        self.a1 = 0
    def fonk2(self):
        return "n " + str(self.b1) + " r " + str(self.a1) + " p " + str(self.b2.b1)
b3 = class1('A')
b4 = class1('B')
b5 = class1('C')
print(b3)
print(b4)
print(b5)
