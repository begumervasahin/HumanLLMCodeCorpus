import math
from DataGenerator import Adjacency_List,Edge,DataGenerator
class class1:
    def fonk1(self,numVertices):
        self.b1 = []
        for b13 in range(numVertices):
            self.b1.append(class2(b13,None))
    def fonk2(self,b13):
        b2 = []
        b3 = self.b1[b13].fonk5(b2)
        for nodes in b2:
            nodes.b4 = b3
        return b3
    def fonk3(self,rootX,rootY,edge,b16):
        b16.addEdge(edge)
        if (rootX.b5 <= rootY.b5):
            rootY.fonk7(rootX)
            rootY.b5 = rootY.b5+1
        else:
            rootX.fonk7(rootY)
            rootX.b5 = rootX.b5+1
class class2:
    def fonk4(self,b6,b4):
        self.b6 = b6
        self.b4 = b4
        if (b4 = = None):
            self.b5 = 1
        else:
            self.b5 = self.b4.b5 + 1
    def fonk5(self,b2):
        if (self.b4 = = None):
            return self
        else:
            b2.append(self)
            b3 = self.b4.fonk5(b2)
            return b3
    def fonk6(self):
        if (self.b4 = = None):
            return
        else:
            print(str(self.b6)+ "--",b7 = '')
            self.b4.fonk6()
    def fonk7(self,b4):
        self.b4 = b4
def fonk8(b18,low,high):
    if (low < high):
        b8 = low+(high-low)/2
        fonk8(b18,int(low),int(b8))
        fonk8(b18,int(b8+1),int(high))
        fonk9(b18,int(low),int(b8),int(high))
def fonk9(b18,low,b8,high):
    b9 = b8 - low + 1
    b10 = high - b8
    b11 = []
    b12 = []
    for b13 in range(b9):
        b11.append(b18[low+b13])
    for b15 in range(b10):
        b12.append(b18[b8+1+b15])
    b13 = b15 = 0
    b14 = low
    while(b13 < b9 and b15 < b10):
        if (b11[b13].weight <= b12[b15].weight):
            b18[b14] = b11[b13]
            b13 = b13 +1
        else:
            b18[b14] = b12[b15]
            b15 = b15 +1
        b14 = b14 +1
    while(b13 < b9):
        b18[b14] = b11[b13]
        b13 = b13 +1
        b14 = b14 +1
    while(b15 < b10):
        b18[b14] = b12[b15]
        b15 = b15 +1
        b14 = b14 +1
def fonk10(Adj):
    b16 = Adjacency_List(Adj.getVertices(),[])
    b17 = class1(Adj.getNumberOfVertices())
    b18 = Adj.getEdges()
    fonk8(b18,0,len(b18)-1)
    for edge in b18:
        b19 = b17.fonk2(edge.u)
        b20 = b17.fonk2(edge.v)
        if (b19.b6 != b20.b6):
            b17.fonk3(b19,b20,edge,b16)
    return b16
if b21 = = '__main__':
    print("
    print("Original Adjacency list")
    print("
    b22 = DataGenerator(100,0.1,method = 2)
    b23 = b22.generateData()
    b23.printMe()
    b16 = fonk10(b23)
    print("
    print("b16: Kruskal Algorithm")
    print("
    b16.printMe()