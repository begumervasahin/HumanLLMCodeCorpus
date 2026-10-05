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
            return self.fonk14(other)
    def fonk3(self):
        return (
            f"{self.b2[:3]}\n"
            f"{self.b2[3:6]}\n"
            f"{self.b2[6:]} {self.b4}{self.b3}\n"
        )
    def fonk4(self):
        return np.array_equal(self.b2, np.arange(9))
    def fonk5(self):
        return np.where(self.b2 = = 0)[0][0]
    def fonk6(self):
        b2 = self.fonk7(self.b2)
        b7 = self.fonk7(np.arange(9))
        return sum((abs(b2
    @staticmethod
    def fonk7(b2):
        b8 = np.zeros(9, dtype=int)
        for x, y in enumerate(b2):
            b8[y] = x
        return b8
    def fonk8(self, i, j):
        b9 = np.array(self.b2)
        b9[i], b9[j] = b9[j], b9[i]
        return b9
    def fonk9(self):
        if self.b5 > 2:
            return self.fonk15(self.b5 - 3, 'Up')
    def fonk10(self):
        if self.b5 < 6:
            return self.fonk15(self.b5 + 3, 'Down')
    def fonk11(self):
        if self.b5 % 3 != 0:
            return self.fonk15(self.b5 - 1, 'Left')
    def fonk12(self):
        if (self.b5 + 1) % 3 != 0:
            return self.fonk15(self.b5 + 1, 'Right')
    def fonk13(self):
        return [neighbor for neighbor in [self.fonk9(), self.fonk10(), self.fonk11(), self.fonk12()] if neighbor]
    def fonk14(self, other):
        b10 = {'Up': 0, 'Down': 1, 'Left': 2, 'Right': 3}
        return b10[self.b3] < b10[other.b3]
    def fonk15(self, new_zero, direction):
        return class1(self.fonk8(self.b5, new_zero), self, direction, self.b4 + 1)
    def fonk16(self):
        return self.fonk3()