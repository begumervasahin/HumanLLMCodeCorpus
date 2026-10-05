import sys
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.distance = sys.maxsize
        self.pred = None
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self, nbr):
        return self.connectedTo[nbr]
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
        for i in alist:
            self.heapList.append(i)
        i = len(alist)
        while i > 0:
            self.percDown(i)
            i = i - 1
    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i][0] > self.heapList[mc][0]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2][0] < self.heapList[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1
    def add(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
    def percUp(self, i):
        while i
            if self.heapList[i][0] < self.heapList[i
                tmp = self.heapList[i
                self.heapList[i
                self.heapList[i] = tmp
            i = i
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    def isEmpty(self):
        return self.currentSize == 0
    def decreaseKey(self, vertex, newDist):
        for i in range(1, len(self.heapList)):
            if self.heapList[i][1] == vertex:
                self.heapList[i] = (newDist, vertex)
                self.percUp(i)
                break
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
vA = Vertex('A')
vB = Vertex('B')
vC = Vertex('C')
vD = Vertex('D')
vE = Vertex('E')
vA.addNeighbor(vB, 2)
vA.addNeighbor(vC, 3)
vB.addNeighbor(vC, 1)
vB.addNeighbor(vD, 1)
vC.addNeighbor(vD, 2)
vC.addNeighbor(vE, 1)
vD.addNeighbor(vE, 3)
graph = [vA, vB, vC, vD, vE]
prim(graph, vA)
for vertex in graph:
    print("Vertex:", vertex.getId())
    print("Distance:", vertex.getDistance())
    if vertex.getPred():
        print("Predecessor:", vertex.getPred().getId())
    else:
        print("Predecessor: None")
    print()