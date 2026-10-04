import math
from DataGenerator import Adjacency_List,Edge,DataGenerator
class class1():
    def fonk1(self,b17):
        self.b1 = []
        self.b2 = []
        self.b3 = []
        self.b4 = len(b17)
        for b5 in range(len(b17)):
            if (b5 = = 0):
                self.b1.append((0,0))
                self.b2.append(0)
                self.b3.append(-1)
            else:
                self.b1.append((b5,math.inf))
                self.b2.append(b5)
                self.b3.append(-1)
        self.a1 = 0
    def fonk2(self):
        for b5 in range(self.b4):
            print("(b6 = "+str(self.b1[b5][0])+" w=" + str(self.b1[b5][1])+") ",end='')
        print('')
    def fonk3(self,vertex,parent):
        self.b3[vertex] = parent
    def fonk4(self,b18,b19):
        b7 = self.b1[0][0]
        if (self.b3[b7] != -1 and b19[b7] == 0):
            b18.addEdge(Edge(self.b3[b7],b7,self.b1[0][1]))
            b19[b7] = 1
        self.b1[0] = self.b1[self.b4-1]
        self.b2[b7] = -1
        self.b2[self.b1[0][0]] = 0
        self.b4 = self.b4 - 1
        self.fonk5(0)
        return b7
    def fonk5(self,b16):
        b7 = b16
        if (2*b16 + 1 < self.b4 and self.b1[b7][1] > self.b1[2*b16 + 1][1]):
            b7 = 2*b16 + 1
        if (2*b16 + 2 < self.b4 and self.b1[b7][1] > self.b1[2*b16 + 2][1]):
            b7 = 2*b16 + 2
        if (b7 != b16):
            b8 = self.b1[b16]
            self.b1[b16] = self.b1[b7]
            self.b1[b7] = b8
            b9 = self.b1[b7][0]
            b10 = self.b1[b16][0]
            b8 = self.b2[b10]
            self.b2[b10] = self.b2[b9]
            self.b2[b9] = b8
            self.fonk5(b7)
    def fonk6(self,b16,vertex):
        b11 = False
        while (not b11):
            b12 = self.b1[int((b16-1)/2)][1]
            b13 = int((b16-1)/2)
            b14 = self.b1[int((b16-1)/2)][0]
            b15 = self.b1[b16][1]
            if (b12 > b15):
                b8 = self.b1[b16]
                self.b1[b16] = self.b1[b13]
                self.b1[b13] = b8
                b16 = b13
                b8 = self.b2[vertex]
                self.b2[vertex] = self.b2[b14]
                self.b2[b14] = b8
            else:
                b11 = True
    def fonk7(self):
        return self.b4 = = 0
    def fonk8(self,vertex):
        return self.b1[self.b2[vertex]][1]
    def fonk9(self,vertex,b22):
        b16 = self.b2[vertex]
        self.b1[b16] = (vertex,b22)
        self.fonk6(b16,vertex)
def fonk10(Adj):
    b17 = Adj.getVertices()
    b18 = Adjacency_List(b17,[])
    b19 = [0 for b5 in range(len(b17))]
    b20 = class1(b17)
    while(not b20.fonk7()):
        b21 = b20.fonk4(b18,b19)
        for b5 in range(Adj.numberOfNeighborsTo(b21)):
            neighbor,b22 = Adj.adjacentTo(b21,b5)
            if (b19[neighbor] == 0 and b20.fonk8(neighbor) > b22):
                b20.fonk3(neighbor,b21)
                b20.fonk9(neighbor,b22)
    return b18
if b23 = = '__main__':
    print("
    print("Original Adjacency b1")
    print("
    b24 = DataGenerator(100,0.1,method = 2)
    b25 = b24.generateData()
    b25.fonk2()
    b18 = fonk10(b25)
    print("
    print("b18: Prim's Algorithm")
    print("
    b18.fonk2()