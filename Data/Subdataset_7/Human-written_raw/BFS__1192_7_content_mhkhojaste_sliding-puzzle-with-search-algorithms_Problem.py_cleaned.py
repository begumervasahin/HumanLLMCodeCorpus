7. Repository: mhkhojaste/sliding-puzzle-with-search-algorithms
   File: Problem.py
   URL: https:
   Code Content:
from copy import deepcopy
from math import sqrt
class class1:
    def fonk1(self):
        self.b1 = []
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
    def fonk4(self, states, b6):
        b2 = deepcopy(states)
        b3 = [(ix, iy) for ix, row in enumerate(b2) for iy, i in enumerate(row) if i == 0]
        b4 = b3[0][0]
        b5 = b3[0][1]
        if b6 = = 'R':
            b2[b4][b5] = b2[b4][b5 + 1]
            b2[b4][b5 + 1] = 0
        elif b6 = = 'L':
            b2[b4][b5] = b2[b4][b5 - 1]
            b2[b4][b5 - 1] = 0
        elif b6 = = 'U':
            b2[b4][b5] = b2[b4 - 1][b5]
            b2[b4 - 1][b5] = 0
        elif b6 = = 'D':
            b2[b4][b5] = b2[b4 + 1][b5]
            b2[b4 + 1][b5] = 0
        return b2
    def fonk5(self, b2):
        if b2 = = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            return True
        else:
            return False
    def fonk6(self, my_matrix):
        a1 = 0
        for i in range(3):
            for j in range(3):
                b7 = (i * 3 + j + 1) % 9
                b3 = [(ix, iy) for ix, row in enumerate(my_matrix) for iy, i in enumerate(row) if i == b7]
                a1 += sqrt((i - b3[0][0]) ** 2 + (j - b3[0][1]) ** 2)
        return round(a1, 2)
   README Content:
In this project I solve sliding puzzle using search algorithms : bfs, dfs, dls, ids, bidirectional, ucs, a*
