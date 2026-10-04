import math
import heapq
from collections import defaultdict
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
class class2:
    def fonk2(self):
        self.b4 = set()
        self.b5 = defaultdict(list)
    def fonk3(self, b1, b2, b3):
        b6 = class1(b1, b2, b3)
        self.b4.add(b1)
        self.b4.add(b2)
        self.b5[b1].append(b6)
class class3:
    def fonk4(self, b8, b7):
        self.b7 = b7
        self.b8 = b8
        self.b9 = {v: math.inf for v in b8.b4}
        self.b9[b7] = 0
        self.b10 = {v: [] for v in b8.b4}
    def fonk5(self, vertex, b6, b11):
        if b11 < self.b9[vertex]:
            self.b9[vertex] = b11
            self.b10[vertex] = [b6]
        elif b11 = = self.b9[vertex]:
            self.b10[vertex].append(b6)
    def fonk6(self, destination, b6):
        if b6 in self.b10[destination]:
            return True
        return any(self.fonk6(e.b1, b6)
                   for e in self.b10[destination])
    def fonk7(self, b12 = None):
        b12 = b12 or self.b8.b4
        return sum(self.b9[v] for v in b12)
def fonk8(b8, b7):
    b13 = class3(b8, b7)
    b14 = [(0, b7)]
    while b14:
        current_distance, b15 = heapq.heappop(b14)
        if current_distance > b13.b9[b15]:
            continue
        for b6 in b8.b5[b15]:
            b2 = b6.b2
            b11 = current_distance + b6.b3
            if b11 < b13.b9[b2]:
                b13.fonk5(b2, b6, b11)
                heapq.heappush(b14, (b11, b2))
            elif b11 = = b13.b9[b2]:
                b13.fonk5(b2, b6, b11)
    return b13
if b16 = = "__main__":
    b8 = class2()
    b8.fonk3('A', 'B', 1)
    b8.fonk3('A', 'C', 4)
    b8.fonk3('B', 'C', 2)
    b8.fonk3('B', 'D', 5)
    b8.fonk3('C', 'D', 1)
    b17 = 'A'
    b18 = fonk8(b8, b17)
    for vertex in b8.b4:
        b19 = b18.b9[vertex]
        print(f"Distance from {b17} to {vertex}: {b19}")
    b20 = b18.fonk7()
    print(f"Sum of distances: {b20}")