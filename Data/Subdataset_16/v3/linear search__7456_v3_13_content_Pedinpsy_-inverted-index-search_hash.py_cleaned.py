import math
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = [b2]
class class2:
    def fonk2(self, b5, b6, b3 = "division", collision_method='linear'):
        self.b4 = [None] * b5
        self.b5 = b5
        self.b6 = b6
        self.a1 = 0
        self.b7 = []
        self.b8 = self._hash_multiplication if b3 == 'multiplication' else self._hash_division
        self.b9 = self._collision_quadratic if collision_method == 'quadratic' else self._collision_linear
    def fonk3(self):
        return self.b4
    def fonk4(self):
        return self.b7
    def fonk5(self, b1, b2):
        if len(b1) < self.b6:
            return False
        b10 = self.b8(b1)
        a1 = 0
        if b1 not in self.b7:
            self.b7.append(b1)
        while True:
            b11 = class1(b1, b2)
            if self.b4[b10] is not None:
                if self.b4[b10].b1 != b1:
                    b10 = self.b9(b10, a1)
                    a1 += 1
                else:
                    self.b4[b10].b2.append(b2)
                    break
            else:
                self.b4[b10] = b11
                self.a1 += 1
                break
        return True
    def fonk6(self, b1):
        if len(b1) < self.b6:
            return None
        b10 = self.b8(b1)
        a1 = 0
        while self.b4[b10] is not None:
            if self.b4[b10].b1 = = b1:
                return self.b4[b10].b2
            else:
                b10 = self.b9(b10, a1)
                a1 = (a1 + 1) % self.b5
        return None
    def fonk7(self, b1):
        b10 = sum(ord(b1[x]) for x in range(self.b6))
        return b10 % self.b5
    def fonk8(self, b1):
        b12 = (math.sqrt(5) - 1) / 2
        b10 = sum(ord(b1[x]) for x in range(self.b6))
        return int(math.floor(self.b5 * ((b12 * b10) % 1)))
    def fonk9(self, b1, a1):
        return (b1 + a1 * a1) % self.b5
    def fonk10(self, b1, addition):
        return (b1 + addition) % self.b5
if b13 = = "__main__":
    b14 = class2(b5=10, b6=5, b3="division", collision_method='linear')
    b14.fonk5("apple", 1)
    b14.fonk5("banana", 2)
    print(b14.fonk6("apple"))
    print(b14.fonk6("banana"))
    print(b14.fonk3())
    print(b14.fonk4())