import math
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = [b2]
class class2:
    def fonk2(self, b5, b6, b3 = "division", collision_method="linear"):
        self.b4 = [None] * b5
        self.b5 = b5
        self.b6 = b6
        self.b7 = []
        self.b8 = self._hash_division if b3 == "division" else self._hash_multiplication
        self.b9 = self._collision_linear if collision_method == "linear" else self._collision_quadratic
    def fonk3(self):
        return self.b4
    def fonk4(self):
        return self.b7
    def fonk5(self, b1, b2):
        if len(b1) < self.b6:
            return False
        b10 = self.b8(b1)
        if b1 not in self.b7:
            self.b7.append(b1)
        a1 = 0
        while True:
            if self.b4[b10] is None:
                self.b4[b10] = class1(b1, b2)
                return True
            elif self.b4[b10].b1 = = b1:
                self.b4[b10].b2.append(b2)
                return True
            else:
                b10 = self.b9(b10, a1)
                a1 += 1
    def fonk6(self, b1):
        if len(b1) < self.b6:
            return None
        b10 = self.b8(b1)
        a1 = 0
        while self.b4[b10] is not None:
            if self.b4[b10].b1 = = b1:
                return self.b4[b10].b2
            b10 = self.b9(b10, a1)
            a1 = (a1 + 1) % self.b5
        return None
    def fonk7(self, b1):
        b10 = sum(ord(char) for char in b1[:self.b6]) % self.b5
        return b10
    def fonk8(self, b1):
        b11 = (math.sqrt(5) - 1) / 2
        b10 = sum(ord(char) for char in b1[:self.b6])
        return math.floor(self.b5 * ((b11 * b10) % 1))
    def fonk9(self, b1, a1):
        return (b1 + a1) % self.b5
    def fonk10(self, b1, a1):
        return (b1 + a1 ** 2) % self.b5