import numpy as np
class class1:
    def fonk1(self, b2, b1 = None, b3=None, b4=0):
        self.b1 = b1
        self.b2 = np.array(b2)
        self.b3 = b3
        self.b4 = b4
        self.b5 = self.fonk5()
        self.b6 = self.b4 + self.fonk6()
    def fonk2(self, other):
        if self.b6 != other.b6:
            return self.b6 < other.b6
        else:
            b7 = {'Up': 0, 'Down': 1, 'Left': 2, 'Right': 3}
            return b7[self.b3] < b7[other.b3]
    def fonk3(self):
        return f"{self.b2[:3]}\n{self.b2[3:6]}\n{self.b2[6:]} {self.b4} {self.b3}\n"
    def fonk4(self):
        return np.array_equal(self.b2, np.arange(9))
    def fonk5(self):
        return np.where(self.b2 = = 0)[0][0]
    def fonk6(self):
        b8 = self.fonk7(self.b2)
        b9 = self.fonk7(np.arange(9))
        return sum((abs(b8
    @staticmethod
    def fonk7(b2):
        b10 = np.zeros(9, dtype=int)
        for x, y in enumerate(b2):
            b10[y] = x
        return b10
    def fonk8(self, i, j):
        b11 = self.b2.copy()
        b11[i], b11[j] = b11[j], b11[i]
        return b11
    def fonk9(self):
        if self.b5 > 2:
            return class1(self.fonk8(self.b5, self.b5 - 3), self, 'Up', self.b4 + 1)
        return None
    def fonk10(self):
        if self.b5 < 6:
            return class1(self.fonk8(self.b5, self.b5 + 3), self, 'Down', self.b4 + 1)
        return None
    def fonk11(self):
        if self.b5 % 3 != 0:
            return class1(self.fonk8(self.b5, self.b5 - 1), self, 'Left', self.b4 + 1)
        return None
    def fonk12(self):
        if (self.b5 + 1) % 3 != 0:
            return class1(self.fonk8(self.b5, self.b5 + 1), self, 'Right', self.b4 + 1)
        return None
    def fonk13(self):
        b12 = [self.fonk9(), self.fonk10(), self.fonk11(), self.fonk12()]
        return [neighbor for neighbor in b12 if neighbor is not None]
    b13 = __str__
if b14 = = "__main__":
    b15 = [1, 2, 5, 3, 4, 0, 6, 7, 8]
    b16 = class1(b15)
    print("Initial class1 State:")
    print(b16)
    print("\nIs Goal State:", b16.fonk4())
    print("\nManhattan Distance:", b16.fonk6())
    print("\nPossible Moves and States:")
    for neighbor in b16.fonk13():
        print(neighbor)