import math
from DataGenerator import Adjacency_List,Edge,DataGenerator
class minHeapPrim():
    def __init__(self,vertices):
        self.list = []
        self.positions = []
        self.parents = []
        self.size = len(vertices)
        for i in range(len(vertices)):
            if (i == 0):
                self.list.append((0,0))
                self.positions.append(0)
                self.parents.append(-1)
            else:
                self.list.append((i,math.inf))
                self.positions.append(i)
                self.parents.append(-1)
        self.totalCost = 0
    def printMe(self):
        for i in range(self.size):
            print("(v="+str(self.list[i][0])+" w=" + str(self.list[i][1])+") ",end='')
        print('')
    def setParent(self,vertex,parent):
        self.parents[vertex] = parent
    def getMinNode(self,MST,addedVertices):
        smallest = self.list[0][0]
        if (self.parents[smallest] != -1 and addedVertices[smallest] == 0):
            MST.addEdge(Edge(self.parents[smallest],smallest,self.list[0][1]))
            addedVertices[smallest] = 1
        self.list[0] = self.list[self.size-1]
        self.positions[smallest] = -1
        self.positions[self.list[0][0]] = 0
        self.size = self.size - 1
        self.minHeapify(0)
        return smallest
    def minHeapify(self,index):
        smallest = index
        if (2*index + 1 < self.size and self.list[smallest][1] > self.list[2*index + 1][1]):
            smallest = 2*index + 1
        if (2*index + 2 < self.size and self.list[smallest][1] > self.list[2*index + 2][1]):
            smallest = 2*index + 2
        if (smallest != index):
            tmp = self.list[index]
            self.list[index] = self.list[smallest]
            self.list[smallest] = tmp
            othervertex = self.list[smallest][0]
            myvertex = self.list[index][0]
            tmp = self.positions[myvertex]
            self.positions[myvertex] = self.positions[othervertex]
            self.positions[othervertex] = tmp
            self.minHeapify(smallest)
    def decreaseKeyValue(self,index,vertex):
        positionFound = False
        while (not positionFound):
            parentWeight = self.list[int((index-1)/2)][1]
            parentIndex = int((index-1)/2)
            parentVertex = self.list[int((index-1)/2)][0]
            mweight = self.list[index][1]
            if (parentWeight > mweight):
                tmp = self.list[index]
                self.list[index] = self.list[parentIndex]
                self.list[parentIndex] = tmp
                index = parentIndex
                tmp = self.positions[vertex]
                self.positions[vertex] = self.positions[parentVertex]
                self.positions[parentVertex] = tmp
            else:
                positionFound = True
    def isEmpty(self):
        return self.size == 0
    def getWeight(self,vertex):
        return self.list[self.positions[vertex]][1]
    def updateHeap(self,vertex,weight):
        index = self.positions[vertex]
        self.list[index] = (vertex,weight)
        self.decreaseKeyValue(index,vertex)
def Prim(Adj):
    vertices = Adj.getVertices()
    MST = Adjacency_List(vertices,[])
    addedVertices = [0 for i in range(len(vertices))]
    minheap = minHeapPrim(vertices)
    while(not minheap.isEmpty()):
        u = minheap.getMinNode(MST,addedVertices)
        for i in range(Adj.numberOfNeighborsTo(u)):
            neighbor,weight = Adj.adjacentTo(u,i)
            if (addedVertices[neighbor] == 0 and minheap.getWeight(neighbor) > weight):
                minheap.setParent(neighbor,u)
                minheap.updateHeap(neighbor,weight)
    return MST
if __name__ == '__main__':
    print("
    print("Original Adjacency list")
    print("
    dg = DataGenerator(100,0.1,method = 2)
    G = dg.generateData()
    G.printMe()
    MST = Prim(G)
    print("
    print("MST: Prim's Algorithm")
    print("
    MST.printMe()