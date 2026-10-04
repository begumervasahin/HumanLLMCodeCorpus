from copy import deepcopy
from math import sqrt
class class1:
    def fonk1(self):
        self.b1 = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
    def fonk2(self):
        return self.b1
    def fonk3(self, b1):
        b2 = []
        i, b3 = [(ix, iy) for ix, row in enumerate(b1) for iy, val in enumerate(row) if val == 0][0]
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
        i, b3 = [(ix, iy) for ix, row in enumerate(b1) for iy, val in enumerate(row) if val == 0][0]
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
        for i in range(3):
            for b3 in range(3):
                b6 = (i * 3 + b3 + 1) % 9
                x, b7 = [(ix, iy) for ix, row in enumerate(b1) for iy, val in enumerate(row) if val == b6][0]
                a1 += sqrt((i - x) ** 2 + (b3 - b7) ** 2)
        return round(a1, 2)
if b8 = = "__main__":
    b9 = class1()
    b10 = b9.fonk2()
    print("Initial State:", b10)
    print("Possible Moves:", b9.fonk3(b10))
    b4 = b9.fonk4(b10, 'D')
    print("State after moving down:", b4)
    print("Is goal b1:", b9.fonk5(b4))
    print("Heuristic value:", b9.fonk6(b4))