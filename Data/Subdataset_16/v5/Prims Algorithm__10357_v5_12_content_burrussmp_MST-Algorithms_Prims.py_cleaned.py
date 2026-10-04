import math
from DataGenerator import Adjacency_List, Edge, DataGenerator
class class1:
    def fonk1(self, b13):
        self.b1 = []
        self.b2 = []
        self.b3 = []
        self.b4 = len(b13)
        for b5 in range(len(b13)):
            if b5 = = 0:
                self.b1.append((0, 0))
                self.b2.append(0)
            else:
                self.b1.append((b5, math.inf))
                self.b2.append(b5)
            self.b3.append(-1)
        self.a1 = 0
    def fonk2(self):
        for vertex, b18 in self.b1:
            print(f"(b6 = {vertex} w={b18}) ", end='')
        print('')
    def fonk3(self, vertex, parent):
        self.b3[vertex] = parent
    def fonk4(self, b14, b15):
        b7 = self.b1[0][0]
        if self.b3[b7] != -1 and not b15[b7]:
            b14.addEdge(Edge(self.b3[b7], b7, self.b1[0][1]))
            b15[b7] = 1
        self.b1[0] = self.b1[self.b4 - 1]
        self.b2[b7] = -1
        self.b2[self.b1[0][0]] = 0
        self.b4 -= 1
        self.fonk5(0)
        return b7
    def fonk5(self, b12):
        b8 = b12
        b9 = 2 * b12 + 1
        b10 = 2 * b12 + 2
        if b9 < self.b4 and self.b1[b8][1] > self.b1[b9][1]:
            b8 = b9
        if b10 < self.b4 and self.b1[b8][1] > self.b1[b10][1]:
            b8 = b10
        if b8 != b12:
            self.fonk6(b12, b8)
            self.fonk5(b8)
    def fonk6(self, b5, j):
        self.b1[b5], self.b1[j] = self.b1[j], self.b1[b5]
        self.b2[self.b1[b5][0]], self.b2[self.b1[j][0]] = self.b2[self.b1[j][0]], self.b2[self.b1[b5][0]]
    def fonk7(self, b12, vertex):
        while b12 > 0:
            b11 = (b12 - 1)
            if self.b1[b11][1] > self.b1[b12][1]:
                self.fonk6(b12, b11)
                b12 = b11
            else:
                break
    def fonk8(self):
        return self.b4 = = 0
    def fonk9(self, vertex):
        return self.b1[self.b2[vertex]][1]
    def fonk10(self, vertex, b18):
        b12 = self.b2[vertex]
        self.b1[b12] = (vertex, b18)
        self.fonk7(b12, vertex)
def fonk11(Adj):
    b13 = Adj.getVertices()
    b14 = Adjacency_List(b13, [])
    b15 = [0] * len(b13)
    b16 = class1(b13)
    while not b16.fonk8():
        b17 = b16.fonk4(b14, b15)
        for b5 in range(Adj.numberOfNeighborsTo(b17)):
            neighbor, b18 = Adj.adjacentTo(b17, b5)
            if not b15[neighbor] and b16.fonk9(neighbor) > b18:
                b16.fonk3(neighbor, b17)
                b16.fonk10(neighbor, b18)
    return b14
if b19 = = '__main__':
    print("Original Adjacency List")
    b20 = DataGenerator(100, 0.1, method=2)
    b21 = b20.generateData()
    b21.print_me()
    b14 = fonk11(b21)
    print("b14: Prim's Algorithm")
    b14.print_me()