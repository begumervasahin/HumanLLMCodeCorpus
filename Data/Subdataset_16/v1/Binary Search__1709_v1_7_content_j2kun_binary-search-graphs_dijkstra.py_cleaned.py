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
        b12 = self.b10[destination]
        if b6 in b12:
            return True
        return any(self.fonk6(e.b1, b6)
                   for e in b12)
    def fonk7(self, b13 = None):
        b13 = b13 or self.b8.b4
        return sum(self.b9[v] for v in b13)
def fonk8(b8, b7):
    b14 = class3(b8, b7)
    b15 = [(0, b7)]
    while b15:
        current_distance, b16 = heapq.heappop(b15)
        if current_distance > b14.b9[b16]:
            continue
        for b6 in b8.b5[b16]:
            b2 = b6.b2
            b17 = current_distance + b6.b3
            if b17 < b14.b9[b2]:
                b14.fonk5(b2, b6, b17)
                heapq.heappush(b15, (b17, b2))
            elif b17 = = b14.b9[b2]:
                b14.fonk5(b2, b6, b17)
    return b14
b8 = class2()
b8.fonk3('A', 'B', 1)
b8.fonk3('A', 'C', 4)
b8.fonk3('B', 'C', 2)
b8.fonk3('B', 'D', 5)
b8.fonk3('C', 'D', 1)
b18 = 'A'
b19 = fonk8(b8, b18)
for vertex in b8.b4:
    print(f"Distance from {b18} to {vertex}: {b19.b9[vertex]}")
print("Sum of distances:", b19.fonk7())