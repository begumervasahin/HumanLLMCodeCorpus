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
        return (
            str(self.b2[:3]) + '\n' +
            str(self.b2[3:6]) + '\n' +
            str(self.b2[6:]) + ' ' +
            str(self.b4) + str(self.b3) + '\n'
        )
    def fonk4(self):
        return np.array_equal(self.b2, np.arange(9))
    def fonk5(self):
        return np.where(self.b2 = = 0)[0][0]
    def fonk6(self):
        b2 = self.fonk7(self.b2)
        b8 = self.fonk7(np.arange(9))
        return sum((abs(b2
    @staticmethod
    def fonk7(b2):
        b9 = np.array(range(9))
        for x, y in enumerate(b2):
            b9[y] = x
        return b9
    def fonk8(self, i, j):
        b10 = np.array(self.b2)
        b10[i], b10[j] = b10[j], b10[i]
        return b10
    def fonk9(self):
        if self.b5 > 2:
            return class1(self.fonk8(self.b5, self.b5 - 3), self, 'Up', self.b4 + 1)
        else:
            return None
    def fonk10(self):
        if self.b5 < 6:
            return class1(self.fonk8(self.b5, self.b5 + 3), self, 'Down', self.b4 + 1)
        else:
            return None
    def fonk11(self):
        if self.b5 % 3 != 0:
            return class1(self.fonk8(self.b5, self.b5 - 1), self, 'Left', self.b4 + 1)
        else:
            return None
    def fonk12(self):
        if (self.b5 + 1) % 3 != 0:
            return class1(self.fonk8(self.b5, self.b5 + 1), self, 'Right', self.b4 + 1)
        else:
            return None
    def fonk13(self):
        b11 = [self.fonk9(), self.fonk10(), self.fonk11(), self.fonk12()]
        return list(filter(None, b11))
    def fonk14(self):
        return self.fonk3()