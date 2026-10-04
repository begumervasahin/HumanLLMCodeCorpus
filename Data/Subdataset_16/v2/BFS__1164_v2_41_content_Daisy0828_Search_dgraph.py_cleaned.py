from collections import deque
from heapq import heappop, heappush
class class1:
    def fonk1(self, b2, b3, b1 = 0):
        self.b2 = b2
        self.b3 = b3
        self.b1 = b1
    def fonk2(self):
        return self.b1
    def fonk3(self, b7):
        return b7 in self.b3
    def fonk4(self, b7):
        b4 = self.b2[b7]
        return {index: cost for index, cost in enumerate(b4) if cost is not None}
def fonk5(b12):
    b1 = b12.fonk2()
    b5 = deque([b1])
    b6 = set()
    while b5:
        b7 = b5.popleft()
        if b12.fonk3(b7):
            return b7
        b6.add(b7)
        for successor in b12.fonk4(b7):
            if successor not in b6 and successor not in b5:
                b5.append(successor)
    return None
def fonk6(b12):
    b1 = b12.fonk2()
    b5 = [b1]
    b6 = set()
    while b5:
        b7 = b5.pop()
        if b12.fonk3(b7):
            return b7
        b6.add(b7)
        for successor in b12.fonk4(b7):
            if successor not in b6 and successor not in b5:
                b5.append(successor)
    return None
def fonk7(b12):
    def fonk8(b7, b8):
        if b8 = = 0 and b12.fonk3(b7):
            return b7
        if b8 > 0:
            for successor in b12.fonk4(b7):
                b9 = fonk8(successor, b8 - 1)
                if b9 is not None:
                    return b9
        return None
    b8 = 0
    while True:
        b9 = fonk8(b12.fonk2(), b8)
        if b9 is not None:
            return b9
        b8 += 1
def fonk9(b12, heuristic):
    b1 = b12.fonk2()
    b5 = [(0, b1)]
    b6 = set()
    while b5:
        cost, b7 = heappop(b5)
        if b12.fonk3(b7):
            return b7
        b6.add(b7)
        for successor, step_cost in b12.fonk4(b7).items():
            if successor not in b6:
                b10 = cost + step_cost + fonk10(successor)
                heappush(b5, (b10, successor))
    return None
def fonk10(b7):
    return 0
if b11 = = "__main__":
    b2 = [
        [None, 1, None, None, None],
        [None, None, 1, None, None],
        [None, None, None, 1, None],
        [None, None, None, None, 1],
        [None, None, None, None, None],
    ]
    b3 = {4}
    b12 = class1(b2, b3)
    b13 = fonk5(b12)
    print("BFS Result:", b13)
    b14 = fonk6(b12)
    print("DFS Result:", b14)
    b15 = fonk7(b12)
    print("IDS Result:", b15)
    b16 = fonk9(b12, heuristic)
    print("A* Result:", b16)