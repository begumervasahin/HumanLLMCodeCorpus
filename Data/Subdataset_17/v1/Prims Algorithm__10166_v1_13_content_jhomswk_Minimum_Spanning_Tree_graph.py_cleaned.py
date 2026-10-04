from random import randint
class Graph:
    def __init__(self, fname=None, numVertices=None, numEdges=None, weightRange=None, directed=True):
        self.adjacent = {}
        self.weight = {}
        if fname is None:
            if any(arg is None for arg in (numVertices, numEdges, weightRange)):
                numVertices, numEdges, weightRange = map(int, input("numVertices, numEdges, weightRange: ").split())
            self.randomGraph(numVertices, numEdges, weightRange, directed)
        else:
            self.loadGraph(fname, directed)
    def numVertices(self):
        return len(self.adjacent)
    def vertices(self):
        return range(self.numVertices())
    def edges(self):
        return ((fromVertex, toVertex) for fromVertex in self.vertices() for toVertex in self.adjacent[fromVertex])
    def addDirectedEdge(self, fromVertex, toVertex, weight):
        self.adjacent.setdefault(fromVertex, set()).add(toVertex)
        self.weight[(fromVertex, toVertex)] = weight
    def addUndirectedEdge(self, fromVertex, toVertex, weight):
        self.addDirectedEdge(fromVertex, toVertex, weight)
        self.addDirectedEdge(toVertex, fromVertex, weight)
    def randomGraph(self, numVertices, numEdges, weightRange, directed):
        addEdge = self.addDirectedEdge if directed else self.addUndirectedEdge
        for vertex in range(numVertices):
            self.adjacent[vertex] = set()
        for edge in range(numEdges):
            fromVertex = toVertex = None
            while fromVertex == toVertex:
                fromVertex = randint(0, numVertices - 1)
                toVertex = randint(0, numVertices - 1)
            weight = randint(0, weightRange)
            addEdge(fromVertex, toVertex, weight)
    def loadGraph(self, fname, directed):
        addEdge = self.addDirectedEdge if directed else self.addUndirectedEdge
        with open(fname, 'r') as f:
            for vertex in range(int(f.readline())):
                self.adjacent[vertex] = set()
            for line in f.readlines():
                fromVertex, toVertex, weight = map(int, line.split())
                addEdge(fromVertex, toVertex, weight)
    def adjacentStr(self, fromVertex):
        return ", ".join(f"({toVertex}, {self.weight[(fromVertex, toVertex)]})" for toVertex in self.adjacent[fromVertex])
    def __str__(self):
        return "\n".join(f"{vertex}: {self.adjacentStr(vertex)}" for vertex in range(self.numVertices()))
    def __repr__(self):
        return str(self)
if __name__ == "__main__":
    graph = Graph(numVertices=5, numEdges=10, weightRange=10, directed=True)
    print(graph)