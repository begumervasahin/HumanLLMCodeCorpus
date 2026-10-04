import math
from DataGenerator import Adjacency_List, Edge, DataGenerator
class class1:
    def fonk1(self, b2, b1 = None):
        self.b2 = b2
        self.b1 = b1
        self.a1 = 1
    def fonk2(self, b1):
        self.b1 = b1
    def fonk3(self, b4):
        if self.b1 is None:
            return self
        b4.append(self)
        return self.b1.fonk3(b4)
class class2:
    def fonk4(self, num_vertices):
        self.b3 = [class1(i) for i in range(num_vertices)]
    def fonk5(self, i):
        b4 = []
        b5 = self.b3[i].fonk3(b4)
        for node in b4:
            node.b1 = b5
        return b5
    def fonk6(self, root_x, root_y, edge, b6):
        b6.addEdge(edge)
        if root_x.a1 <= root_y.a1:
            root_y.fonk2(root_x)
            root_y.a1 += 1
        else:
            root_x.fonk2(root_y)
            root_x.a1 += 1
def fonk7(adj):
    b6 = Adjacency_List(adj.getVertices(), [])
    b7 = class2(adj.getNumberOfVertices())
    b8 = adj.getNumberOfVertices()
    while b8 > 1:
        b9 = [Edge(-1, -1, math.inf) for _ in range(adj.getNumberOfVertices())]
        for edge in adj.getEdges():
            b10 = b7.fonk5(edge.u)
            b11 = b7.fonk5(edge.v)
            if b10 != b11:
                if b9[b10.b2].weight >= edge.weight:
                    b9[b10.b2] = edge
                if b9[b11.b2].weight >= edge.weight:
                    b9[b11.b2] = edge
        for edge in b9:
            if edge.weight != math.inf:
                b10 = b7.fonk5(edge.u)
                b11 = b7.fonk5(edge.v)
                if b10 != b11:
                    b7.fonk6(b10, b11, edge, b6)
                    b8 -= 1
    return b6
if b12 = = '__main__':
    print("Original Adjacency List")
    b13 = DataGenerator(100, 0.1, method=2)
    b14 = b13.generateData()
    b14.printMe()
    print("\nMST: Sollin's Algorithm")
    b6 = fonk7(b14)
    b6.printMe()