import math
from DataGenerator import Adjacency_List, Edge, DataGenerator
class class1:
    def fonk1(self, numVertices):
        self.b1 = [class2(b10, None) for b10 in range(numVertices)]
    def fonk2(self, b10):
        b2 = []
        b3 = self.b1[b10].fonk5(b2)
        for node in b2:
            node.b4 = b3
        return b3
    def fonk3(self, rootX, rootY, edge, b12):
        b12.addEdge(edge)
        if rootX.b6 <= rootY.b6:
            rootY.fonk6(rootX)
            rootY.b6 += 1
        else:
            rootX.fonk6(rootY)
            rootX.b6 += 1
class class2:
    def fonk4(self, b5, b4):
        self.b5 = b5
        self.b4 = b4
        self.b6 = 1 if b4 is None else b4.b6 + 1
    def fonk5(self, b2):
        if self.b4 is None:
            return self
        b2.append(self)
        return self.b4.fonk5(b2)
    def fonk6(self, b4):
        self.b4 = b4
def fonk7(b14, low, high):
    if low < high:
        b7 = (low + high)
        fonk7(b14, low, b7)
        fonk7(b14, b7 + 1, high)
        fonk8(b14, low, b7, high)
def fonk8(b14, low, b7, high):
    b8 = b14[low:b7 + 1]
    b9 = b14[b7 + 1:high + 1]
    b10 = j = 0
    b11 = low
    while b10 < len(b8) and j < len(b9):
        if b8[b10].weight <= b9[j].weight:
            b14[b11] = b8[b10]
            b10 += 1
        else:
            b14[b11] = b9[j]
            j += 1
        b11 += 1
    while b10 < len(b8):
        b14[b11] = b8[b10]
        b10 += 1
        b11 += 1
    while j < len(b9):
        b14[b11] = b9[j]
        j += 1
        b11 += 1
def fonk9(Adj):
    b12 = Adjacency_List(Adj.getVertices(), [])
    b13 = class1(Adj.getNumberOfVertices())
    b14 = Adj.getEdges()
    fonk7(b14, 0, len(b14) - 1)
    for edge in b14:
        b15 = b13.fonk2(edge.u)
        b16 = b13.fonk2(edge.v)
        if b15.b5 != b16.b5:
            b13.fonk3(b15, b16, edge, b12)
    return b12
if b17 = = '__main__':
    print("Original Adjacency List")
    b18 = DataGenerator(100, 0.1, method=2)
    b19 = b18.generateData()
    b19.printMe()
    b12 = fonk9(b19)
    print("b12: Kruskal Algorithm")
    b12.printMe()