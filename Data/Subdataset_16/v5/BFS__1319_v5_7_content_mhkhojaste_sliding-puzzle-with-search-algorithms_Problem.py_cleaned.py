from copy import deepcopy
from math import sqrt
class class1:
    def fonk1(self):
        self.b1 = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
    def fonk2(self):
        return self.b1
    def fonk3(self, b1):
        b2 = []
        i, b3 = self.fonk7(b1)
        if i > 0:
            b2.append('U')
        if i < 2:
            b2.append('D')
        if b3 > 0:
            b2.append('L')
        if b3 < 2:
            b2.append('R')
        return b2
    def fonk4(self, b1, b5):
        b4 = deepcopy(b1)
        i, b3 = self.fonk7(b1)
        if b5 = = 'U':
            b4[i][b3], b4[i-1][b3] = b4[i-1][b3], b4[i][b3]
        elif b5 = = 'D':
            b4[i][b3], b4[i+1][b3] = b4[i+1][b3], b4[i][b3]
        elif b5 = = 'L':
            b4[i][b3], b4[i][b3-1] = b4[i][b3-1], b4[i][b3]
        elif b5 = = 'R':
            b4[i][b3], b4[i][b3+1] = b4[i][b3+1], b4[i][b3]
        return b4
    def fonk5(self, b1):
        return b1 = = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    def fonk6(self, b1):
        a1 = 0
        b6 = {(i * 3 + b3 + 1) % 9: (i, b3) for i in range(3) for b3 in range(3)}
        for i in range(3):
            for b3 in range(3):
                b7 = b1[i][b3]
                if b7 != 0:
                    goal_i, b8 = b6[b7]
                    a1 += sqrt((i - goal_i) ** 2 + (b3 - b8) ** 2)
        return round(a1, 2)
    def fonk7(self, b1):
        for i, row in enumerate(b1):
            for b3, b9 in enumerate(row):
                if b9 = = 0:
                    return i, b3
if b10 = = "__main__":
    b11 = class1()
    b12 = b11.fonk2()
    print("Initial State:", b12)
    print("Possible Moves:", b11.fonk3(b12))
    b4 = b11.fonk4(b12, 'D')
    print("State after moving down:", b4)
    print("Is goal b1:", b11.fonk5(b4))
    print("Heuristic value:", b11.fonk6(b4))