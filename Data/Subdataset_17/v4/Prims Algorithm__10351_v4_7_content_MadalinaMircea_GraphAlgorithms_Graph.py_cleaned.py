class Graph:
    def __init__(self, n):
        self.nrVertices = n
        self.nrEdges = 0
        self._dictOut = {i: [] for i in range(n)}
    def isVertex(self, x):
        return x in self._dictOut
    def parseAll(self):
        return list(self._dictOut.keys())
    def parseNeighbours(self, x):
        if self.isVertex(x):
            return self._dictOut[x]
        return False
    def isEdge(self, x, y):
        if self.isVertex(x):
            return y in self._dictOut[x]
        return False
    def addEdge(self, x, y):
        if not self.isEdge(x, y):
            self._dictOut[x].append(y)
            self._dictOut[y].append(x)
            self.nrEdges += 1
            return True
        return False
    def getNrVertices(self):
        return self.nrVertices
    def getNrEdges(self):
        return self.nrEdges
    def getDegree(self, x):
        if self.isVertex(x):
            return len(self._dictOut[x])
        return False