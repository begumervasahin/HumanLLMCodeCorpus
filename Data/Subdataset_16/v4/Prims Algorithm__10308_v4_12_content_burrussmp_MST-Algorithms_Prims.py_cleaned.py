import math
from DataGenerator import Adjacency_List, Edge, DataGenerator
class class1:
    def fonk1(self, b12):
        self.b1 = []
        self.b2 = []
        self.b3 = []
        self.b4 = len(b12)
        for b5 in range(len(b12)):
            if b5 = = 0:
                self.b1.append((0, 0))
                self.b2.append(0)
                self.b3.append(-1)
            else:
                self.b1.append((b5, math.inf))
                self.b2.append(b5)
                self.b3.append(-1)
        self.a1 = 0
    def fonk2(self):
        for vertex, b17 in self.b1:
            print(f"(b6 = {vertex} w={b17}) ", end='')
        print('')
    def fonk3(self, vertex, parent):
        self.b3[vertex] = parent
    def fonk4(self, b13, b14):
        b7 = self.b1[0][0]
        if self.b3[b7] != -1 and b14[b7] == 0:
            b13.addEdge(Edge(self.b3[b7], b7, self.b1[0][1]))
            b14[b7] = 1
        self.b1[0] = self.b1[self.b4 - 1]
        self.b2[b7] = -1
        self.b2[self.b1[0][0]] = 0
        self.b4 -= 1
        self.fonk5(0)
        return b7
    def fonk5(self, b11):
        b7 = b11
        b8 = 2 * b11 + 1
        b9 = 2 * b11 + 2
        if b8 < self.b4 and self.b1[b7][1] > self.b1[b8][1]:
            b7 = b8
        if b9 < self.b4 and self.b1[b7][1] > self.b1[b9][1]:
            b7 = b9
        if b7 != b11:
            self.fonk6(b11, b7)
            self.fonk5(b7)
    def fonk6(self, index1, index2):
        self.b1[index1], self.b1[index2] = self.b1[index2], self.b1[index1]
        self.b2[self.b1[index1][0]], self.b2[self.b1[index2][0]] = self.b2[self.b1[index2][0]], self.b2[self.b1[index1][0]]
    def fonk7(self, b11, vertex):
        while b11 > 0:
            b10 = (b11 - 1)
            if self.b1[b10][1] > self.b1[b11][1]:
                self.fonk6(b11, b10)
                b11 = b10
            else:
                break
    def fonk8(self):
        return self.b4 = = 0
    def fonk9(self, vertex):
        return self.b1[self.b2[vertex]][1]
    def fonk10(self, vertex, b17):
        b11 = self.b2[vertex]
        self.b1[b11] = (vertex, b17)
        self.fonk7(b11, vertex)
def fonk11(Adj):
    b12 = Adj.getVertices()
    b13 = Adjacency_List(b12, [])
    b14 = [0] * len(b12)
    b15 = class1(b12)
    while not b15.fonk8():
        b16 = b15.fonk4(b13, b14)
        for b5 in range(Adj.numberOfNeighborsTo(b16)):
            neighbor, b17 = Adj.adjacentTo(b16, b5)
            if b14[neighbor] == 0 and b15.fonk9(neighbor) > b17:
                b15.fonk3(neighbor, b16)
                b15.fonk10(neighbor, b17)
    return b13
if b18 = = '__main__':
    print("Original Adjacency List")
    b19 = DataGenerator(100, 0.1, method=2)
    b20 = b19.generateData()
    b20.fonk2()
    b13 = fonk11(b20)
    print("b13: Prim's Algorithm")
    b13.fonk2()