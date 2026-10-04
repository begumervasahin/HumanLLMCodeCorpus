class Graph:
    def __init__(self, n):
        '''
        Creates a graph with n vertices (numbered from 0 to n-1) and no edges
        '''
        self.nrVertices = n
        self.nrEdges = 0
        self._dictOut = {i: [] for i in range(n)}
    def isVertex(self, x):
        '''
        Returns True if x is a vertex and False otherwise
        '''
        return x in self._dictOut
    def parseAll(self):
        '''
        Returns a list containing all the vertices
        '''
        return list(self._dictOut.keys())
    def parseNeighbours(self, x):
        '''
        Returns a list containing the neighbours of x
        '''
        if self.isVertex(x):
            return self._dictOut[x]
        else:
            return False
    def isEdge(self, x, y):
        '''
        Returns True if there is an edge from x to y, False otherwise. Also returns False if one or both of
        the vertices do not exist.
        '''
        if self.isVertex(x):
            return y in self._dictOut[x]
        else:
            return False
    def addEdge(self, x, y):
        '''
        Adds an edge from x to y
        '''
        if not self.isEdge(x, y):
            self._dictOut[x].append(y)
            self._dictOut[y].append(x)
            self.nrEdges += 1
            return True
        else:
            return False
    def getNrVertices(self):
        '''
        Returns the number of vertices.
        '''
        return self.nrVertices
    def getNrEdges(self):
        '''
        Returns the number of edges.
        '''
        return self.nrEdges
    def getDegree(self, x):
        '''
        Returns the degree of the vertex x, False if it does not exist.
        '''
        if self.isVertex(x):
            return len(self._dictOut[x])
        else:
            return False
g = Graph(5)
print(g.parseAll())
print(g.addEdge(0, 1))
print(g.addEdge(0, 2))
print(g.addEdge(1, 2))
print(g.addEdge(1, 3))
print(g.isEdge(0, 1))
print(g.isEdge(0, 3))
print(g.getNrEdges())
print(g.getNrVertices())
print(g.getDegree(1))
print(g.getDegree(4))
print(g.parseNeighbours(1))
