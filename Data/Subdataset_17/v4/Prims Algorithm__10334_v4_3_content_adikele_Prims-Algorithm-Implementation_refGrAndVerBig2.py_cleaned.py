class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    def __str__(self):
        return f"{self.id} connectedTo: {[x.id for x in self.connectedTo]}"
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self, nbr):
        return self.connectedTo[nbr]
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    def getVertex(self, n):
        return self.vertList.get(n)
    def __contains__(self, n):
        return n in self.vertList
    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
    def getVertices(self):
        return self.vertList.keys()
    def areNeighbors(self, a, b):
        if a not in self.vertList or b not in self.vertList:
            return False
        return any(neighbor.id == b and self.vertList[a].getWeight(neighbor) < 6 for neighbor in self.vertList[a].getConnections())
    def __iter__(self):
        return iter(self.vertList.values())
    def isConnected(self, a, b):
        if a not in self.vertList or b not in self.vertList:
            return False
        return any(neighbor.id == b for neighbor in self.vertList[a].getConnections())
    def minCostNeighbor(self, a):
        if a not in self.vertList:
            return False
        return min(self.vertList[a].getWeight(neighbor) for neighbor in self.vertList[a].getConnections())
    def minCostNeighborId(self, a):
        if a not in self.vertList:
            return False
        min_cost = float('inf')
        min_cost_id = None
        for neighbor in self.vertList[a].getConnections():
            cost = self.vertList[a].getWeight(neighbor)
            if cost < min_cost:
                min_cost = cost
                min_cost_id = neighbor.id
        return min_cost_id
    def getEdgeWeight(self, a, b):
        if a not in self.vertList or b not in self.vertList:
            return False
        return self.vertList[a].getWeight(self.vertList[b])