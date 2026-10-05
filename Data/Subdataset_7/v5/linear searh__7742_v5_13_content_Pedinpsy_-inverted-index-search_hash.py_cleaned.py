import math
class class1:
    def fonk1(self, b2, value):
        self.b1 = [value]
        self.b2 = b2
class class2:
    def fonk2(self, b5, b6, b3 = "division", collision_method='linear'):
        self.b4 = [None] * b5
        self.b5 = b5
        self.b6 = b6
        self.a1 = 0
        self.b7 = []
        self.b8 = self.get_value_multiplication if b3 == 'multiplication' else self.get_value_division
        self.b9 = self.get_quadratic_value if collision_method == 'quadratic' else self.get_linear_value
    def fonk3(self):
        return self.b4
    def fonk4(self):
        return self.b7
    def fonk5(self, b2, value):
        if len(b2) < self.b6:
            return False
        a1 = 0
        b10 = self.b8(b2)
        if b2 not in self.b7:
            self.b7.append(b2)
        while True:
            b11 = class1(b2, value)
            if self.b4[b10] is not None:
                if self.b4[b10].b2 != b2:
                    b10 = self.b9(b10, a1)
                    a1 += 1
                else:
                    self.b4[b10].b1.append(value)
                    break
            else:
                self.b4[b10] = b11
                self.a1 += 1
                break
        return True
    def fonk6(self, b2):
        if len(b2) < self.b6:
            return None
        a1 = 0
        b10 = self.b8(b2)
        while True:
            if self.b4[b10] is None:
                return None
            if self.b4[b10].b2 = = b2:
                return self.b4[b10].b1
            else:
                b10 = self.b9(b10, a1)
                a1 = (a1 + 1) % self.b5
    def fonk7(self, b2):
        b10 = sum(ord(char) for char in b2) % self.b5
        return b10
    def fonk8(self, b2):
        b12 = (math.sqrt(5) - 1) / 2
        b10 = sum(ord(char) for char in b2)
        b10 = math.floor(self.b5 * ((b12 * b10) % 1))
        return b10
    def fonk9(self, b2, a1):
        b13 = (b2 + a1 * a1) % self.b5
        return b13
    def fonk10(self, b2, adictionator):
        return (b2 + adictionator) % self.b5