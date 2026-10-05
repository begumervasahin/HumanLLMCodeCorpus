from copy import deepcopy
from math import sqrt
from queue import Queue
from heapq import heappush, heappop
class class1:
    def fonk1(self):
        self.b1 = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
    def fonk2(self):
        return self.b1
    def fonk3(self, b5):
        b2 = []
        b3 = [(ix, iy) for ix, row in enumerate(b5) for iy, i in enumerate(row) if i == 0]
        i_index, b4 = b3[0]
        if i_index > 0:
            b2.append('U')
        if i_index < 2:
            b2.append('D')
        if b4 > 0:
            b2.append('L')
        if b4 < 2:
            b2.append('R')
        return b2
    def fonk4(self, states, b6):
        b5 = deepcopy(states)
        b3 = [(ix, iy) for ix, row in enumerate(b5) for iy, i in enumerate(row) if i == 0]
        i_index, b4 = b3[0]
        if b6 = = 'R':
            b5[i_index][b4] = b5[i_index][b4 + 1]
            b5[i_index][b4 + 1] = 0
        elif b6 = = 'L':
            b5[i_index][b4] = b5[i_index][b4 - 1]
            b5[i_index][b4 - 1] = 0
        elif b6 = = 'U':
            b5[i_index][b4] = b5[i_index - 1][b4]
            b5[i_index - 1][b4] = 0
        elif b6 = = 'D':
            b5[i_index][b4] = b5[i_index + 1][b4]
            b5[i_index + 1][b4] = 0
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
def fonk7(b15):
    b8 = b15.fonk2()
    if b15.fonk5(b8):
        return b8
    b9 = Queue()
    b9.put(b8)
    b10 = set()
    while not b9.empty():
        b1 = b9.get()
        b10.add(tuple(map(tuple, b1)))
        for move in b15.fonk3(b1):
            b11 = b15.fonk4(b1, move)
            if tuple(map(tuple, b11)) not in b10:
                if b15.fonk5(b11):
                    return b11
                b9.put(b11)
    return None
def fonk8(b15, b12 = 10):
    b8 = b15.fonk2()
    if b15.fonk5(b8):
        return b8
    return fonk9(b15, b8, set(), b12)
def fonk9(b15, b1, b10, b12):
    if b15.fonk5(b1):
        return b1
    if b12 = = 0:
        return None
    b10.add(tuple(map(tuple, b1)))
    for move in b15.fonk3(b1):
        b11 = b15.fonk4(b1, move)
        if tuple(map(tuple, b11)) not in b10:
            b13 = fonk9(b15, b11, b10, b12 - 1)
            if b13 is not None:
                return b13
    return None
def fonk10(b15):
    b8 = b15.fonk2()
    if b15.fonk5(b8):
        return b8
    b9 = []
    heappush(b9, (0, b8))
    b10 = set()
    while b9:
        cost, b1 = heappop(b9)
        if b15.fonk5(b1):
            return b1
        b10.add(tuple(map(tuple, b1)))
        for move in b15.fonk3(b1):
            b11 = b15.fonk4(b1, move)
            if tuple(map(tuple, b11)) not in b10:
                b14 = cost + 1
                heappush(b9, (b14, b11))
    return None
def fonk11(b15):
    b8 = b15.fonk2()
    if b15.fonk5(b8):
        return b8
    b9 = []
    heappush(b9, (b15.fonk6(b8), b8))
    b10 = set()
    while b9:
        _, b1 = heappop(b9)
        if b15.fonk5(b1):
            return b1
        b10.add(tuple(map(tuple, b1)))
        for move in b15.fonk3(b1):
            b11 = b15.fonk4(b1, move)
            if tuple(map(tuple, b11)) not in b10:
                b14 = b15.fonk6(b11) + len(b10)
                heappush(b9, (b14, b11))
    return None
def fonk12():
    b15 = class1()
    print("BFS:", fonk7(b15))
    print("DFS:", fonk8(b15))
    print("UCS:", fonk10(b15))
    print("A*:", fonk11(b15))
if b16 = = "__main__":
    fonk12()