from copy import deepcopy
from math import sqrt
class class1:
    def fonk1(self):
        self.b1 = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
    def fonk2(self):
        return self.b1
    def fonk3(self, b1):
        b2 = {
            (0, 0): ['R', 'D'],
            (0, 1): ['L', 'R', 'D'],
            (0, 2): ['L', 'D'],
            (1, 0): ['R', 'D', 'U'],
            (1, 1): ['L', 'R', 'D', 'U'],
            (1, 2): ['L', 'D', 'U'],
            (2, 0): ['R', 'U'],
            (2, 1): ['L', 'R', 'U'],
            (2, 2): ['L', 'U']
        }
        b3 = [(ix, iy) for ix, row in enumerate(b1) for iy, i in enumerate(row) if i == 0][0]
        return b2[b3]
    def fonk4(self, b1, b6):
        b4 = deepcopy(b1)
        b3 = [(ix, iy) for ix, row in enumerate(b4) for iy, i in enumerate(row) if i == 0][0]
        i, b5 = b3
        if b6 = = 'R':
            b4[i][b5], b4[i][b5 + 1] = b4[i][b5 + 1], b4[i][b5]
        elif b6 = = 'L':
            b4[i][b5], b4[i][b5 - 1] = b4[i][b5 - 1], b4[i][b5]
        elif b6 = = 'U':
            b4[i][b5], b4[i - 1][b5] = b4[i - 1][b5], b4[i][b5]
        elif b6 = = 'D':
            b4[i][b5], b4[i + 1][b5] = b4[i + 1][b5], b4[i][b5]
        return b4
    def fonk5(self, b1):
        return b1 = = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    def fonk6(self, b1):
        a1 = 0
        for i in range(3):
            for b5 in range(3):
                b7 = (i * 3 + b5 + 1) % 9
                b8 = [(ix, iy) for ix, row in enumerate(b1) for iy, val in enumerate(row) if val == b7][0]
                a1 += sqrt((i - b8[0]) ** 2 + (b5 - b8[1]) ** 2)
        return round(a1, 2)
if b9 = = "__main__":
    b10 = class1()
    b11 = b10.fonk2()
    print("Initial State:")
    print(b11)
    b2 = b10.fonk3(b11)
    print("\nPossible Moves:")
    print(b2)
    b4 = b10.fonk4(b11, b2[0])
    print("\nNew State after b6", b2[0], ":")
    print(b4)
    b12 = b10.fonk5(b4)
    print("\nIs Goal State:", b12)
    b13 = b10.fonk6(b4)
    print("\nHeuristic Value of New State:")
    print(b13)