from copy import deepcopy
from math import sqrt
from queue import Queue
from heapq import heappush, heappop
class class1:
    def fonk1(self):
        self.b1 = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
    def fonk2(self):
        return self.b1
    def fonk3(self, b7):
        b2 = []
        b3 = self.fonk7(b7)
        i, b4 = b3
        if i > 0:
            b2.append('U')
        if i < 2:
            b2.append('D')
        if b4 > 0:
            b2.append('L')
        if b4 < 2:
            b2.append('R')
        return b2
    def fonk4(self, b7, b6):
        b5 = deepcopy(b7)
        b3 = self.fonk7(b5)
        i, b4 = b3
        if b6 = = 'R':
            b5[i][b4], b5[i][b4 + 1] = b5[i][b4 + 1], 0
        elif b6 = = 'L':
            b5[i][b4], b5[i][b4 - 1] = b5[i][b4 - 1], 0
        elif b6 = = 'U':
            b5[i][b4], b5[i - 1][b4] = b5[i - 1][b4], 0
        elif b6 = = 'D':
            b5[i][b4], b5[i + 1][b4] = b5[i + 1][b4], 0
        return b5
    def fonk5(self, b7):
        return b7 = = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    def fonk6(self, b7):
        a1 = 0
        for i in range(3):
            for b4 in range(3):
                b8 = (i * 3 + b4 + 1) % 9
                b9 = self.fonk8(b7, b8)
                a1 += sqrt((i - b9[0]) ** 2 + (b4 - b9[1]) ** 2)
        return round(a1, 2)
    def fonk7(self, b7):
        for i in range(3):
            for b4 in range(3):
                if b7[i][b4] == 0:
                    return i, b4
    def fonk8(self, b7, b8):
        for i in range(3):
            for b4 in range(3):
                if b7[i][b4] == b8:
                    return i, b4
def fonk9(b16):
    b10 = b16.fonk2()
    if b16.fonk5(b10):
        return b10
    b11 = Queue()
    b11.put(b10)
    b12 = set()
    while not b11.empty():
        b7 = b11.get()
        b12.add(tuple(map(tuple, b7)))
        for move in b16.fonk3(b7):
            b5 = b16.fonk4(b7, move)
            if tuple(map(tuple, b5)) not in b12:
                if b16.fonk5(b5):
                    return b5
                b11.put(b5)
    return None
def fonk10(b16, b13 = 10):
    b10 = b16.fonk2()
    if b16.fonk5(b10):
        return b10
    return fonk11(b16, b10, set(), b13)
def fonk11(b16, b7, b12, b13):
    if b16.fonk5(b7):
        return b7
    if b13 = = 0:
        return None
    b12.add(tuple(map(tuple, b7)))
    for move in b16.fonk3(b7):
        b5 = b16.fonk4(b7, move)
        if tuple(map(tuple, b5)) not in b12:
            b14 = fonk11(b16, b5, b12, b13 - 1)
            if b14 is not None:
                return b14
    return None
def fonk12(b16):
    b10 = b16.fonk2()
    if b16.fonk5(b10):
        return b10
    b11 = []
    heappush(b11, (0, b10))
    b12 = set()
    while b11:
        cost, b7 = heappop(b11)
        if b16.fonk5(b7):
            return b7
        b12.add(tuple(map(tuple, b7)))
        for move in b16.fonk3(b7):
            b5 = b16.fonk4(b7, move)
            if tuple(map(tuple, b5)) not in b12:
                b15 = cost + 1
                heappush(b11, (b15, b5))
    return None
def fonk13(b16):
    b10 = b16.fonk2()
    if b16.fonk5(b10):
        return b10
    b11 = []
    heappush(b11, (b16.fonk6(b10), b10))
    b12 = set()
    while b11:
        _, b7 = heappop(b11)
        if b16.fonk5(b7):
            return b7
        b12.add(tuple(map(tuple, b7)))
        for move in b16.fonk3(b7):
            b5 = b16.fonk4(b7, move)
            if tuple(map(tuple, b5)) not in b12:
                b15 = b16.fonk6(b5) + len(b12)
                heappush(b11, (b15, b5))
    return None
def fonk14():
    b16 = class1()
    print("BFS:", fonk9(b16))
    print("DFS:", fonk10(b16))
    print("UCS:", fonk12(b16))
    print("A*:", fonk13(b16))
if b17 = = "__main__":
    fonk14()