class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self):
        return f"({self.b1}, {self.b2}, {self.b3})"
    def fonk3(self, other):
        if not isinstance(other, class1):
            return False
        return self.b1 = = other.b1 and self.b2 == other.b2 and self.b3 == other.b3 and self.b4 == other.b4
    @staticmethod
    def fonk4(b1, b2, b3, b4):
        return class1(b1, b2, b3, b4)
    def fonk5(self):
        return class1(self.b1, (-self.b2) % self.b4, self.b3, self.b4)
if b5 = = "__main__":
    b6 = class1(b8, 2, 3, 7)
    b7 = class1.fonk4(b8, 2, 3, 7)
    print(f"class1 b8: {b6}")
    print(f"class1 2: {b7}")
    print(f"class1 b8 = = class1 2: {b6 == b7}")
    b9 = b6.fonk5()
    print(f"Negated class1 b8: {b9}")