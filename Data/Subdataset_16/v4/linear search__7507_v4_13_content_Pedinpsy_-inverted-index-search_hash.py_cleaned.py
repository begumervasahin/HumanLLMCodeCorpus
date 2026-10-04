import math
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = [b2]
class class2:
    def fonk2(self, b5, b6, b3 = "division", b9="linear"):
        self.b4 = [None] * b5
        self.b5 = b5
        self.b6 = b6
        self.a1 = 0
        self.b7 = []
        if b3 = = "multiplication":
            self.b8 = self._hash_multiplication
        else:
            self.b8 = self._hash_division
        if b9 = = "quadratic":
            self.b10 = self._collision_quadratic
        else:
            self.b10 = self._collision_linear
    def fonk3(self):
        return self.b4
    def fonk4(self):
        return self.b7
    def fonk5(self, b1, b2):
        if len(b1) < self.b6:
            return False
        b11 = self.b8(b1)
        if b1 not in self.b7:
            self.b7.append(b1)
        a1 = 0
        while True:
            if self.b4[b11] is not None:
                if self.b4[b11].b1 != b1:
                    b11 = self.b10(b11, a1)
                    a1 += 1
                else:
                    self.b4[b11].b2.append(b2)
                    break
            else:
                self.b4[b11] = class1(b1, b2)
                self.a1 += 1
                break
        return True
    def fonk6(self, b1):
        if len(b1) < self.b6:
            return None
        b11 = self.b8(b1)
        a1 = 0
        while True:
            if self.b4[b11] is None:
                return None
            if self.b4[b11].b1 = = b1:
                return self.b4[b11].b2
            b11 = self.b10(b11, a1)
            a1 = (a1 + 1) % self.b5
    def fonk7(self, b1):
        b11 = sum(ord(char) for char in b1[:self.b6]) % self.b5
        return b11
    def fonk8(self, b1):
        b12 = (math.sqrt(5) - 1) / 2
        b11 = sum(ord(char) for char in b1[:self.b6])
        b11 = math.floor(self.b5 * ((b12 * b11) % 1))
        return b11
    def fonk9(self, b1, a1):
        return (b1 + a1 * a1) % self.b5
    def fonk10(self, b1, a1):
        return (b1 + a1) % self.b5