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
        b8 = str(self.b2[:3]) + '\n' + str(self.b2[3:6]) + '\n' + str(self.b2[6:])
        return f"{b8} Depth: {self.b4} Operator: {self.b3}\n"
    def fonk4(self):
        return np.array_equal(self.b2, np.arange(9))
    def fonk5(self):
        return np.where(self.b2 = = 0)[0][0]
    def fonk6(self):
        b9 = self.fonk7(self.b2)
        b10 = self.fonk7(np.arange(9))
        return sum((abs(b9
    @staticmethod
    def fonk7(b2):
        b11 = np.zeros_like(b2)
        for index, value in enumerate(b2):
            b11[value] = index
        return b11
    def fonk8(self, i, j):
        b12 = self.b2.copy()
        b12[i], b12[j] = b12[j], b12[i]
        return b12
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
        b13 = [self.fonk9(), self.fonk10(), self.fonk11(), self.fonk12()]
        return list(filter(None, b13))
    b14 = __str__
if b15 = = "__main__":
    b16 = [1, 2, 5, 3, 4, 0, 6, 7, 8]
    b17 = class1(b16)
    print("Initial State:")
    print(b17)
    print("Is goal b2:", b17.fonk4())
    print("Possible moves:")
    for neighbor in b17.fonk13():
        print(neighbor)
    print("Manhattan distance:", b17.fonk6())