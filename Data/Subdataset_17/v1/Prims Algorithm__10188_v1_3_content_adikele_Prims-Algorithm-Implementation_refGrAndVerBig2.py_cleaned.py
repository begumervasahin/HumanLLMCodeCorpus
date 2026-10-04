class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
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
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
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
    def NeighboursJoo(self, a, b):
        if a not in self.vertList or b not in self.vertList:
            return False
        for i in self.vertList[a].connectedTo.keys():
            if i.id == b:
                costo = self.vertList[a].connectedTo[i]
                if costo < 6:
                    return True
        return False
    def __iter__(self):
        return iter(self.vertList.values())
    def connectedOrNot(self, a, b):
        if a not in self.vertList or b not in self.vertList:
            return False
        for i in self.vertList[a].connectedTo.keys():
            if i.id == b:
                return True
        return False
    def LagiWalaCostDivpi(self, a):
        if a not in self.vertList:
            return False
        listo = [self.vertList[a].getWeight(i) for i in self.vertList[a].connectedTo.keys()]
        if listo:
            return min(listo)
        return None
    def LagiWalaIdDivpi(self, a):
        if a not in self.vertList:
            return False
        min_cost = float('inf')
        min_id = None
        for i in self.vertList[a].connectedTo.keys():
            tmp = self.vertList[a].getWeight(i)
            if tmp < min_cost:
                min_cost = tmp
                min_id = i.id
        return min_id
    def getWeight(self, a, b):
        if a not in self.vertList or b not in self.vertList:
            return False
        return self.vertList[a].getWeight(self.vertList[b])
if __name__ == "__main__":
    g = Graph()
    g.addVertex(1)
    g.addVertex(2)
    g.addVertex(3)
    g.addEdge(1, 2, 5)
    g.addEdge(1, 3, 3)
    print(g.LagiWalaCostDivpi(1))
    print(g.LagiWalaIdDivpi(1))
    print(g.getWeight(1, 3))
    print(g.connectedOrNot(1, 3))
    print(g.NeighboursJoo(1, 2))
