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
def fonk5(b14):
    b1 = b14.fonk2()
    b5 = deque([b1])
    b6 = set()
    while b5:
        b7 = b5.popleft()
        if b14.fonk3(b7):
            return b7
        b6.add(b7)
        for successor in b14.fonk4(b7):
            if successor not in b6 and successor not in b5:
                b5.append(successor)
    return None
def fonk6(b14):
    b1 = b14.fonk2()
    b5 = [b1]
    b6 = set()
    while b5:
        b7 = b5.pop()
        if b14.fonk3(b7):
            return b7
        b6.add(b7)
        for successor in b14.fonk4(b7):
            if successor not in b6 and successor not in b5:
                b5.append(successor)
    return None
def fonk7(b14):
    def fonk8(b7, b8):
        if b8 = = 0 and b14.fonk3(b7):
            return b7
        if b8 > 0:
            for successor in b14.fonk4(b7):
                b9 = fonk8(successor, b8 - 1)
                if b9 is not None:
                    return b9
        return None
    b8 = 0
    while True:
        b9 = fonk8(b14.fonk2(), b8)
        if b9 is not None:
            return b9
        b8 += 1
def fonk9(b14, heuristic):
    b1 = b14.fonk2()
    b5 = [(0, b1)]
    b6 = set()
    b10 = {b1: 0}
    while b5:
        current_cost, b7 = heappop(b5)
        if b14.fonk3(b7):
            return b7
        b6.add(b7)
        for successor, step_cost in b14.fonk4(b7).items():
            b11 = current_cost + step_cost
            if successor not in b6 or b11 < b10.get(successor, float('inf')):
                b10[successor] = b11
                b12 = b11 + fonk10(successor)
                heappush(b5, (b12, successor))
    return None
def fonk10(b7):
    return 0
if b13 = = "__main__":
    b2 = [
        [None, 1, None, None, None],
        [None, None, 1, None, None],
        [None, None, None, 1, None],
        [None, None, None, None, 1],
        [None, None, None, None, None],
    ]
    b3 = {4}
    b14 = class1(b2, b3)
    b15 = fonk5(b14)
    print("BFS Result:", b15)
    b16 = fonk6(b14)
    print("DFS Result:", b16)
    b17 = fonk7(b14)
    print("IDS Result:", b17)
    b18 = fonk9(b14, heuristic)
    print("A* Result:", b18)