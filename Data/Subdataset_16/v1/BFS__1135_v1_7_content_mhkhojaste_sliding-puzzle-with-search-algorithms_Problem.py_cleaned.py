from copy import deepcopy
from math import sqrt
class class1:
    def fonk1(self):
        self.b1 = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
    def fonk2(self):
        return self.b1
    def fonk3(self, b2):
        if b2[0][0] == 0:
            return ['R', 'D']
        elif b2[0][1] == 0:
            return ['L', 'R', 'D']
        elif b2[0][2] == 0:
            return ['L', 'D']
        elif b2[1][0] == 0:
            return ['R', 'D', 'U']
        elif b2[1][1] == 0:
            return ['L', 'R', 'D', 'U']
        elif b2[1][2] == 0:
            return ['L', 'D', 'U']
        elif b2[2][0] == 0:
            return ['R', 'U']
        elif b2[2][1] == 0:
            return ['L', 'R', 'U']
        elif b2[2][2] == 0:
            return ['L', 'U']
    def fonk4(self, states, b5):
        b2 = deepcopy(states)
        b3 = [(ix, iy) for ix, row in enumerate(b2) for iy, i in enumerate(row) if i == 0]
        i_index, b4 = b3[0]
        if b5 = = 'R':
            b2[i_index][b4], b2[i_index][b4 + 1] = b2[i_index][b4 + 1], b2[i_index][b4]
        elif b5 = = 'L':
            b2[i_index][b4], b2[i_index][b4 - 1] = b2[i_index][b4 - 1], b2[i_index][b4]
        elif b5 = = 'U':
            b2[i_index][b4], b2[i_index - 1][b4] = b2[i_index - 1][b4], b2[i_index][b4]
        elif b5 = = 'D':
            b2[i_index][b4], b2[i_index + 1][b4] = b2[i_index + 1][b4], b2[i_index][b4]
        return b2
    def fonk5(self, b2):
        return b2 = = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    def fonk6(self, my_matrix):
        a1 = 0
        for i in range(3):
            for j in range(3):
                b6 = (i * 3 + j + 1) % 9
                b3 = [(ix, iy) for ix, row in enumerate(my_matrix) for iy, i in enumerate(row) if i == b6]
                a1 += sqrt((i - b3[0][0]) ** 2 + (j - b3[0][1]) ** 2)
        return round(a1, 2)
if b7 = = "__main__":
    b8 = class1()
    b9 = b8.fonk2()
    print("Initial State:")
    print(b9)
    b10 = b8.fonk3(b9)
    print("\nPossible Moves:")
    print(b10)
    b11 = b8.fonk4(b9, b10[0])
    print("\nNew State after move", b10[0], ":")
    print(b11)
    b12 = b8.fonk5(b11)
    print("\nIs Goal State:", b12)
    b13 = b8.fonk6(b11)
    print("\nHeuristic Value of New State:")
    print(b13)