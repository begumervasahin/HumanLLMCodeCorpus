import math
from DataGenerator import Adjacency_List,Edge,DataGenerator
class class1:
    def fonk1(self,b1,b2):
        self.b1 = b1
        self.b2 = b2
        self.a1 = 1
    def fonk2(self,b2):
        self.b2 = b2
    def fonk3(self,b5):
        if (self.b2 = = None):
            return self
        else:
            b5.append(self)
            b3 = self.b2.fonk3(b5)
            return b3
class class2:
    def fonk4(self,numVertices):
        self.b4 = []
        for i in range(numVertices):
            self.b4.append(class1(i,None))
    def fonk5(self,i):
        b5 = []
        b3 = self.b4[i].fonk3(b5)
        for nodes in b5:
            nodes.b2 = b3
        return b3
    def fonk6(self,rootX,rootY,edge,b6):
        b6.addEdge(edge)
        if (rootX.a1 <= rootY.a1):
            rootY.fonk2(rootX)
            rootY.a1 = rootY.a1+1
        else:
            rootX.fonk2(rootY)
            rootX.a1 = rootX.a1+1
def fonk7(Adj):
    b6 = Adjacency_List(Adj.getVertices(),[])
    b7 = class2(Adj.getNumberOfVertices())
    b8 = Adj.getNumberOfVertices()
    while (b8 > 1):
        b9 = []
        for i in range(Adj.getNumberOfVertices()):
            b9.append(Edge(-1,-1,math.inf))
        for edge in Adj.getEdges():
            b10 = b7.fonk5(edge.u)
            b11 = b7.fonk5(edge.v)
            if (b10 != b11):
                if (b9[b10.b1].weight >= edge.weight):
                    b9[b10.b1] = edge
                if (b9[b11.b1].weight >= edge.weight):
                    b9[b11.b1] = edge
        for edge in b9:
            if (edge.weight != math.inf):
                b10 = b7.fonk5(edge.u)
                b11 = b7.fonk5(edge.v)
                if (b10 != b11):
                    b7.fonk6(b10,b11,edge,b6)
                    b8 = b8 - 1
    return b6
if b12 = = '__main__':
    print("
    print("Original Adjacency list")
    print("
    b13 = DataGenerator(100,0.1,method = 2)
    b14 = b13.generateData()
    b14.printMe()
    b6 = fonk7(b14)
    print("
    print("b6: Sollin's Algorithm")
    print("
    b6.printMe()