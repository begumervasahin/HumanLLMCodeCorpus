from copy import deepcopy
from math import sqrt
class class1:
    def fonk1(self):
        self.b1 = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
    def fonk2(self):
        return self.b1
    def fonk3(self, b6):
        zero_row, b2 = self.fonk7(b6)
        b3 = []
        if zero_row > 0:
            b3.append('U')
        if zero_row < 2:
            b3.append('D')
        if b2 > 0:
            b3.append('L')
        if b2 < 2:
            b3.append('R')
        return b3
    def fonk4(self, b6, b5):
        b4 = deepcopy(b6)
        zero_row, b2 = self.fonk7(b4)
        if b5 = = 'R':
            b4[zero_row][b2], b4[zero_row][b2 + 1] = b4[zero_row][b2 + 1], 0
        elif b5 = = 'L':
            b4[zero_row][b2], b4[zero_row][b2 - 1] = b4[zero_row][b2 - 1], 0
        elif b5 = = 'U':
            b4[zero_row][b2], b4[zero_row - 1][b2] = b4[zero_row - 1][b2], 0
        elif b5 = = 'D':
            b4[zero_row][b2], b4[zero_row + 1][b2] = b4[zero_row + 1][b2], 0
        return b4
    def fonk5(self, b6):
        return b6 = = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    def fonk6(self, b6):
        a1 = 0
        for i in range(3):
            for j in range(3):
                b7 = (i * 3 + j + 1) % 9
                number_row, b8 = self.fonk8(b6, b7)
                a1 += sqrt((i - number_row) ** 2 + (j - b8) ** 2)
        return round(a1, 2)
    def fonk7(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j
    def fonk8(self, state, b7):
        for i in range(3):
            for j in range(3):
                if state[i][j] == b7:
                    return i, j