class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self):
        return f"({self.b1}, {self.b2}, {self.b3})"
    def fonk3(self, other):
        return self.b1 = = other.b1 and self.b2 == other.b2 and self.b3 == other.b3 and self.b4 == other.b4
    def fonk4(self):
        self.b2 = (-self.b2) % self.b4
        return self
    @staticmethod
    def fonk5(b1, b2, b3, b4):
        return class1(b1, b2, b3, b4)
b5 = class1(1, 2, 3, 5)
print(b5)
b6 = class1.fonk5(4, 5, 6, 7)
print(b6)
b7 = class1(1, 2, 3, 5)
print(b5 = = b7)
b8 = class1(1, 2, 4, 5)
print(b5 = = b8)
b5.fonk4()
print(b5)
