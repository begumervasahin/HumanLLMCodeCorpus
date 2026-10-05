import math
import heapq
class class1:
    def fonk1(self, b2, b1):
        self.b1 = b1
        self.b2 = b2
        self.b3 = {vertex: math.inf for vertex in b2.b15}
        self.b3[b1] = 0
        self.b4 = {vertex: [] for vertex in b2.b15}
    def fonk2(self, vertex, b17, new_distance):
        self.b3[vertex] = new_distance
        self.b4[vertex].append(b17)
    def fonk3(self, destination, b17):
        b5 = self.b4[destination]
        return b17 in b5 or any(
            self.fonk3(pre.b13, b17) for pre in b5
        )
    def fonk4(self, b6 = None):
        b6 = b6 or self.b2.b15
        return sum(self.b3[vertex] for vertex in b6)
def fonk5(b2, b1):
    b7 = class1(b2, b1)
    b8 = [(0, b1)]
    while b8:
        priority, b9 = heapq.heappop(b8)
        for b17 in b2.b16[b9]:
            b10 = b17.b14
            b11 = b17.b11
            b12 = b7.b3[b9] + b11
            if b12 < b7.b3[b10]:
                b7.fonk2(b10, b17, b12)
                heapq.heappush(b8, (b12, b10))
    return b7
class class2:
    def fonk6(self, b13, b14, b11):
        self.b13 = b13
        self.b14 = b14
        self.b11 = b11
class class3:
    def fonk7(self, b15):
        self.b15 = b15
        self.b16 = {vertex: [] for vertex in b15}
    def fonk8(self, b13, b14, b11):
        b17 = class2(b13, b14, b11)
        self.b16[b13].append(b17)
b15 = ['A', 'B', 'C', 'D', 'E']
b2 = class3(b15)
b2.fonk8('A', 'B', 2)
b2.fonk8('A', 'C', 4)
b2.fonk8('B', 'C', 1)
b2.fonk8('B', 'D', 7)
b2.fonk8('C', 'D', 3)
b2.fonk8('C', 'E', 5)
b2.fonk8('D', 'E', 2)
b7 = fonk5(b2, 'A')
print("Shortest distances from 'A' to each vertex:", b7.b3)
print("Predecessor edges for each vertex:", b7.b4)
print("Total distance:", b7.fonk4())