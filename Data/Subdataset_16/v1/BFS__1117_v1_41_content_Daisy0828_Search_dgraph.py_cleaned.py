class class1:
    def fonk1(self, b2, b3, b1 = 0):
        self.b2 = b2
        self.b3 = b3
        self.b1 = b1
    def fonk2(self):
        return self.b1
    def fonk3(self, b8):
        return b8 in self.b3
    def fonk4(self, b8):
        b4 = self.b2[b8]
        b5 = {}
        a1 = 0
        for cost in b4:
            if cost is not None:
                b5[a1] = cost
            a1 += 1
        return b5
def fonk5(b13):
    from collections import deque
    b1 = b13.fonk2()
    b6 = deque([b1])
    b7 = set()
    while b6:
        b8 = b6.popleft()
        if b13.fonk3(b8):
            return b8
        b7.add(b8)
        for successor in b13.fonk4(b8):
            if successor not in b7 and successor not in b6:
                b6.append(successor)
    return None
def fonk6(b13):
    b1 = b13.fonk2()
    b6 = [b1]
    b7 = set()
    while b6:
        b8 = b6.pop()
        if b13.fonk3(b8):
            return b8
        b7.add(b8)
        for successor in b13.fonk4(b8):
            if successor not in b7 and successor not in b6:
                b6.append(successor)
    return None
def fonk7(b13):
    def fonk8(b8, b9):
        if b9 = = 0 and b13.fonk3(b8):
            return b8
        if b9 > 0:
            for successor in b13.fonk4(b8):
                b10 = fonk8(successor, b9 - 1)
                if b10 is not None:
                    return b10
        return None
    b9 = 0
    while True:
        b10 = fonk8(b13.fonk2(), b9)
        if b10 is not None:
            return b10
        b9 += 1
def fonk9(b13, heuristic):
    from heapq import heappop, heappush
    b1 = b13.fonk2()
    b6 = [(0, b1)]
    b7 = set()
    while b6:
        cost, b8 = heappop(b6)
        if b13.fonk3(b8):
            return b8
        b7.add(b8)
        for successor, step_cost in b13.fonk4(b8).items():
            if successor not in b7:
                b11 = cost + step_cost + fonk10(successor)
                heappush(b6, (b11, successor))
    return None
def fonk10(b8):
    return 0
if b12 = = "__main__":
    b2 = [
        [None, 1, None, None, None],
        [None, None, 1, None, None],
        [None, None, None, 1, None],
        [None, None, None, None, 1],
        [None, None, None, None, None],
    ]
    b3 = {4}
    b13 = class1(b2, b3)
    b14 = fonk5(b13)
    print("BFS Result:", b14)
    b15 = fonk6(b13)
    print("DFS Result:", b15)
    b16 = fonk7(b13)
    print("IDS Result:", b16)
    b17 = fonk9(b13, heuristic)
    print("A* Result:", b17)