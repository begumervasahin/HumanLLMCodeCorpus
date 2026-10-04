import math
import random
class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight
class Adjacency_List:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
    def getVertices(self):
        return self.vertices
    def getNumberOfVertices(self):
        return len(self.vertices)
    def getEdges(self):
        return self.edges
    def addEdge(self, edge):
        self.edges.append(edge)
    def printMe(self):
        for edge in self.edges:
            print(f"({edge.u}, {edge.v}) - Weight: {edge.weight}")
class Node:
    def __init__(self, vertex, parent):
        self.vertex = vertex
        self.parent = parent
        self.rank = 1
    def makeChildOf(self, parent):
        self.parent = parent
    def getRoot(self, path):
        if self.parent is None:
            return self
        else:
            path.append(self)
            root = self.parent.getRoot(path)
            return root
class UnionFind:
    def __init__(self, numVertices):
        self.trees = [Node(i, None) for i in range(numVertices)]
    def find(self, i):
        path = []
        root = self.trees[i].getRoot(path)
        for node in path:
            node.parent = root
        return root
    def union(self, rootX, rootY, edge, MST):
        MST.addEdge(edge)
        if rootX.rank <= rootY.rank:
            rootY.makeChildOf(rootX)
            rootY.rank += 1
        else:
            rootX.makeChildOf(rootY)
            rootX.rank += 1
def Sollins(Adj):
    MST = Adjacency_List(Adj.getVertices(), [])
    UF = UnionFind(Adj.getNumberOfVertices())
    numberOfComponents = Adj.getNumberOfVertices()
    while numberOfComponents > 1:
        cheapEdge = [Edge(-1, -1, math.inf) for _ in range(Adj.getNumberOfVertices())]
        for edge in Adj.getEdges():
            setX = UF.find(edge.u)
            setY = UF.find(edge.v)
            if setX != setY:
                if cheapEdge[setX.vertex].weight >= edge.weight:
                    cheapEdge[setX.vertex] = edge
                if cheapEdge[setY.vertex].weight >= edge.weight:
                    cheapEdge[setY.vertex] = edge
        for edge in cheapEdge:
            if edge.weight != math.inf:
                setX = UF.find(edge.u)
                setY = UF.find(edge.v)
                if setX != setY:
                    UF.union(setX, setY, edge, MST)
                    numberOfComponents -= 1
    return MST
class DataGenerator:
    def __init__(self, numVertices, edgeProbability, method=2):
        self.numVertices = numVertices
        self.edgeProbability = edgeProbability
        self.method = method
    def generateData(self):
        vertices = list(range(self.numVertices))
        edges = []
        for i in range(self.numVertices):
            for j in range(i + 1, self.numVertices):
                if random.random() < self.edgeProbability:
                    weight = random.randint(1, 100)
                    edges.append(Edge(i, j, weight))
        return Adjacency_List(vertices, edges)
if __name__ == '__main__':
    print("Original Adjacency List")
    dg = DataGenerator(100, 0.1, method=2)
    G = dg.generateData()
    G.printMe()
    MST = Sollins(G)
    print("\nMST: Sollin's Algorithm")
    MST.printMe()