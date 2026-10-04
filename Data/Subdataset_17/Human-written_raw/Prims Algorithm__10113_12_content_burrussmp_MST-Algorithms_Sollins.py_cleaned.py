import math
from DataGenerator import Adjacency_List,Edge,DataGenerator
class Node:
    def __init__(self,vertex,parent):
        self.vertex = vertex
        self.parent = parent
        self.rank = 1
    def makeChildOf(self,parent):
        self.parent = parent
    def getRoot(self,path):
        if (self.parent == None):
            return self
        else:
            path.append(self)
            root = self.parent.getRoot(path)
            return root
class UnionFind:
    def __init__(self,numVertices):
        self.trees = []
        for i in range(numVertices):
            self.trees.append(Node(i,None))
    def find(self,i):
        path = []
        root = self.trees[i].getRoot(path)
        for nodes in path:
            nodes.parent = root
        return root
    def union(self,rootX,rootY,edge,MST):
        MST.addEdge(edge)
        if (rootX.rank <= rootY.rank):
            rootY.makeChildOf(rootX)
            rootY.rank = rootY.rank+1
        else:
            rootX.makeChildOf(rootY)
            rootX.rank = rootX.rank+1
def Sollins(Adj):
    MST = Adjacency_List(Adj.getVertices(),[])
    UF = UnionFind(Adj.getNumberOfVertices())
    numberOfComponents = Adj.getNumberOfVertices()
    while (numberOfComponents > 1):
        cheapEdge = []
        for i in range(Adj.getNumberOfVertices()):
            cheapEdge.append(Edge(-1,-1,math.inf))
        for edge in Adj.getEdges():
            setX = UF.find(edge.u)
            setY = UF.find(edge.v)
            if (setX != setY):
                if (cheapEdge[setX.vertex].weight >= edge.weight):
                    cheapEdge[setX.vertex] = edge
                if (cheapEdge[setY.vertex].weight >= edge.weight):
                    cheapEdge[setY.vertex] = edge
        for edge in cheapEdge:
            if (edge.weight != math.inf):
                setX = UF.find(edge.u)
                setY = UF.find(edge.v)
                if (setX != setY):
                    UF.union(setX,setY,edge,MST)
                    numberOfComponents = numberOfComponents - 1
    return MST
if __name__ == '__main__':
    print("
    print("Original Adjacency list")
    print("
    dg = DataGenerator(100,0.1,method = 2)
    G = dg.generateData()
    G.printMe()
    MST = Sollins(G)
    print("
    print("MST: Sollin's Algorithm")
    print("
    MST.printMe()