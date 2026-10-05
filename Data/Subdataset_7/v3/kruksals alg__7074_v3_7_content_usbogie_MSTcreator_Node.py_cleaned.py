class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self, other):
        return (self.b1, self.b2, self.b3) == (other.b1, other.b2, other.b3)
b5 = class1(1, 2, 3, [4, 5, 6])
b6 = class1(1, 2, 3, [4, 5, 6])
b7 = class1(4, 5, 6, [7, 8, 9])
print("Are b5 and b6 equal?", b5 = = b6)
print("Are b5 and b7 equal?", b5 = = b7)
