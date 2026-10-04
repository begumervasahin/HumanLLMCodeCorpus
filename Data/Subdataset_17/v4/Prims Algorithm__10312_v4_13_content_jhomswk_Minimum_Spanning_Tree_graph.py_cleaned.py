from random import randint
class Graph:
    def __init__(self, fname=None, numVertices=None, numEdges=None, weightRange=None, directed=True):
        self.adjacent = {}
        self.weight = {}
        if fname is None:
            if any(arg is None for arg in (numVertices, numEdges, weightRange)):
                numVertices, numEdges, weightRange = map(int, input("Enter numVertices, numEdges, weightRange: ").split())
            self._generate_random_graph(numVertices, numEdges, weightRange, directed)
        else:
            self._load_graph_from_file(fname, directed)
    def num_vertices(self):
        return len(self.adjacent)
    def vertices(self):
        return range(self.num_vertices())
    def edges(self):
        return ((fromVertex, toVertex) for fromVertex in self.vertices() for toVertex in self.adjacent[fromVertex])
    def add_directed_edge(self, fromVertex, toVertex, weight):
        self.adjacent.setdefault(fromVertex, set()).add(toVertex)
        self.weight[(fromVertex, toVertex)] = weight
    def add_undirected_edge(self, fromVertex, toVertex, weight):
        self.add_directed_edge(fromVertex, toVertex, weight)
        self.add_directed_edge(toVertex, fromVertex, weight)
    def _generate_random_graph(self, numVertices, numEdges, weightRange, directed):
        add_edge = self.add_directed_edge if directed else self.add_undirected_edge
        for vertex in range(numVertices):
            self.adjacent[vertex] = set()
        for _ in range(numEdges):
            fromVertex = toVertex = None
            while fromVertex == toVertex:
                fromVertex = randint(0, numVertices - 1)
                toVertex = randint(0, numVertices - 1)
            weight = randint(0, weightRange)
            add_edge(fromVertex, toVertex, weight)
    def _load_graph_from_file(self, fname, directed):
        add_edge = self.add_directed_edge if directed else self.add_undirected_edge
        with open(fname, 'r') as f:
            for vertex in range(int(f.readline().strip())):
                self.adjacent[vertex] = set()
            for line in f:
                fromVertex, toVertex, weight = map(int, line.split())
                add_edge(fromVertex, toVertex, weight)
    def adjacent_str(self, fromVertex):
        return ", ".join(f"({toVertex}, {self.weight[(fromVertex, toVertex)]})" for toVertex in self.adjacent[fromVertex])
    def __str__(self):
        return "\n".join(f"{vertex}: {self.adjacent_str(vertex)}" for vertex in range(self.num_vertices()))
    def __repr__(self):
        return str(self)