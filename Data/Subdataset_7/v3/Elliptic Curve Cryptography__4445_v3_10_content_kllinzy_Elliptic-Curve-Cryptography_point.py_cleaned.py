class class1:
    def fonk1(self, x_coord, y_coord, z_coord, modulus):
        self.b1 = x_coord
        self.b2 = y_coord
        self.b3 = z_coord
        self.b4 = modulus
    def fonk2(self):
        return f"({self.b1}, {self.b2}, {self.b3})"
    def fonk3(self, other_point):
        return (
            self.b1 = = other_point.b1
            and self.b2 = = other_point.b2
            and self.b3 = = other_point.b3
            and self.b4 = = other_point.b4
        )
    def fonk4(self):
        self.b2 = (-self.b2) % self.b4
        return self
    @staticmethod
    def fonk5(x_coord, y_coord, z_coord, modulus):
        return class1(x_coord, y_coord, z_coord, modulus)
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
