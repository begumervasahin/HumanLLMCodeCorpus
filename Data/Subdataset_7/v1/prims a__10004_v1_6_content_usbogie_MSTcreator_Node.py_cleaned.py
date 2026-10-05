class class1(object):
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self, rhs):
        return self.b1 = = rhs.b1 and self.b2 == rhs.b2 and self.b3 == rhs.b3
b5 = class1(1, 2, 3, [4, 5, 6])
b6 = class1(1, 2, 3, [4, 5, 6])
b7 = class1(4, 5, 6, [7, 8, 9])
print("b5 = = b6:", b5 == b6)
print("b5 = = b7:", b5 == b7)
