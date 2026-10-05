import sys
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.distance = sys.maxsize
        self.pred = None
    def addNeighbor(self, neighbor, weight=0):
        self.connectedTo[neighbor] = weight
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]
    def setDistance(self, dist):
        self.distance = dist
    def getDistance(self):
        return self.distance
    def setPred(self, pred):
        self.pred = pred
    def getPred(self):
        return self.pred
class PriorityQueue:
    def __init__(self):
        self.heapList = [(0, None)]
        self.currentSize = 0
    def buildHeap(self, alist):
        self.currentSize = len(alist)
        self.heapList = [(0, None)]
        for item in alist:
            self.heapList.append(item)
        index = len(alist)
        while index > 0:
            self.percDown(index)
            index -= 1
    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            minChildIndex = self.minChild(i)
            if self.heapList[i][0] > self.heapList[minChildIndex][0]:
                self.swap(i, minChildIndex)
            i = minChildIndex
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2][0] < self.heapList[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1
    def add(self, item):
        self.heapList.append(item)
        self.currentSize += 1
        self.percUp(self.currentSize)
    def percUp(self, i):
        while i
            if self.heapList[i][0] < self.heapList[i
                self.swap(i, i
            i
    def delMin(self):
        minItem = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return minItem
    def isEmpty(self):
        return self.currentSize == 0
    def decreaseKey(self, vertex, newDist):
        for i in range(1, len(self.heapList)):
            if self.heapList[i][1] == vertex:
                self.heapList[i] = (newDist, vertex)
                self.percUp(i)
                break
    def swap(self, i, j):
        self.heapList[i], self.heapList[j] = self.heapList[j], self.heapList[i]
def prim(G, start):
    pq = PriorityQueue()
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in G])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert[1].getConnections():
            newCost = currentVert[1].getWeight(nextVert)
            if newCost < nextVert.getDistance():
                nextVert.setPred(currentVert[1])
                nextVert.setDistance(newCost)
                pq.decreaseKey(nextVert, newCost)
vertexA = Vertex('A')
vertexB = Vertex('B')
vertexC = Vertex('C')
vertexD = Vertex('D')
vertexE = Vertex('E')
vertexA.addNeighbor(vertexB, 2)
vertexA.addNeighbor(vertexC, 3)
vertexB.addNeighbor(vertexC, 1)
vertexB.addNeighbor(vertexD, 1)
vertexC.addNeighbor(vertexD, 2)
vertexC.addNeighbor(vertexE, 1)
vertexD.addNeighbor(vertexE, 3)
graph = [vertexA, vertexB, vertexC, vertexD, vertexE]
prim(graph, vertexA)
for vertex in graph:
    print("Vertex:", vertex.getId())
    print("Distance:", vertex.getDistance())
    if vertex.getPred():
        print("Predecessor:", vertex.getPred().getId())
    else:
        print("Predecessor: None")
    print()