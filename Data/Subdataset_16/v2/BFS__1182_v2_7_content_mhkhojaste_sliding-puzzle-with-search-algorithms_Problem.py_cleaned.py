from copy import deepcopy
from math import sqrt
class class1:
    def fonk1(self):
        self.b1 = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
    def fonk2(self):
        return self.b1
    def fonk3(self, b5):
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
        b3 = [(ix, iy) for ix, row in enumerate(b5) for iy, i in enumerate(row) if i == 0]
        i_index, b4 = b3[0]
        return b2[(i_index, b4)]
    def fonk4(self, states, b6):
        b5 = deepcopy(states)
        b3 = [(ix, iy) for ix, row in enumerate(b5) for iy, i in enumerate(row) if i == 0]
        i_index, b4 = b3[0]
        if b6 = = 'R':
            b5[i_index][b4], b5[i_index][b4 + 1] = b5[i_index][b4 + 1], b5[i_index][b4]
        elif b6 = = 'L':
            b5[i_index][b4], b5[i_index][b4 - 1] = b5[i_index][b4 - 1], b5[i_index][b4]
        elif b6 = = 'U':
            b5[i_index][b4], b5[i_index - 1][b4] = b5[i_index - 1][b4], b5[i_index][b4]
        elif b6 = = 'D':
            b5[i_index][b4], b5[i_index + 1][b4] = b5[i_index + 1][b4], b5[i_index][b4]
        return b5
    def fonk5(self, b5):
        return b5 = = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    def fonk6(self, my_matrix):
        a1 = 0
        for i in range(3):
            for j in range(3):
                b7 = (i * 3 + j + 1) % 9
                b3 = [(ix, iy) for ix, row in enumerate(my_matrix) for iy, i in enumerate(row) if i == b7]
                a1 += sqrt((i - b3[0][0]) ** 2 + (j - b3[0][1]) ** 2)
        return round(a1, 2)
if b8 = = "__main__":
    b9 = class1()
    b10 = b9.fonk2()
    print("Initial State:")
    print(b10)
    b2 = b9.fonk3(b10)
    print("\nPossible Moves:")
    print(b2)
    b11 = b9.fonk4(b10, b2[0])
    print("\nNew State after move", b2[0], ":")
    print(b11)
    b12 = b9.fonk5(b11)
    print("\nIs Goal State:", b12)
    b13 = b9.fonk6(b11)
    print("\nHeuristic Value of New State:")
    print(b13)