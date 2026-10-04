from random import randint
class Graph:
    def __init__(self, fname=None, numVertices=None, numEdges=None, weightRange=None, directed=True):
        self.adjacent = {}
        self.weight = {}
        if fname is None:
            if any(arg is None for arg in (numVertices, numEdges, weightRange)):
                numVertices, numEdges, weightRange = map(int, input("numVertices, numEdges, weightRange: ").split())
            self._generate_random_graph(numVertices, numEdges, weightRange, directed)
        else:
            self._load_graph_from_file(fname, directed)
    def num_vertices(self):
        return len(self.adjacent)
    def vertices(self):
        return range(self.num_vertices())
    def edges(self):
        return ((from_vertex, to_vertex) for from_vertex in self.vertices() for to_vertex in self.adjacent[from_vertex])
    def add_directed_edge(self, from_vertex, to_vertex, weight):
        self.adjacent.setdefault(from_vertex, set()).add(to_vertex)
        self.weight[(from_vertex, to_vertex)] = weight
    def add_undirected_edge(self, from_vertex, to_vertex, weight):
        self.add_directed_edge(from_vertex, to_vertex, weight)
        self.add_directed_edge(to_vertex, from_vertex, weight)
    def _generate_random_graph(self, numVertices, numEdges, weightRange, directed):
        add_edge = self.add_directed_edge if directed else self.add_undirected_edge
        for vertex in range(numVertices):
            self.adjacent[vertex] = set()
        for _ in range(numEdges):
            from_vertex, to_vertex = randint(0, numVertices - 1), randint(0, numVertices - 1)
            while from_vertex == to_vertex:
                to_vertex = randint(0, numVertices - 1)
            weight = randint(1, weightRange)
            add_edge(from_vertex, to_vertex, weight)
    def _load_graph_from_file(self, fname, directed):
        add_edge = self.add_directed_edge if directed else self.add_undirected_edge
        with open(fname, 'r') as f:
            num_vertices = int(f.readline().strip())
            for vertex in range(num_vertices):
                self.adjacent[vertex] = set()
            for line in f:
                from_vertex, to_vertex, weight = map(int, line.split())
                add_edge(from_vertex, to_vertex, weight)
    def adjacent_str(self, from_vertex):
        return ", ".join(f"({to_vertex}, {self.weight[(from_vertex, to_vertex)]})" for to_vertex in self.adjacent[from_vertex])
    def __str__(self):
        return "\n".join(f"{vertex}: {self.adjacent_str(vertex)}" for vertex in self.vertices())
    def __repr__(self):
        return str(self)
if __name__ == "__main__":
    graph = Graph(numVertices=5, numEdges=10, weightRange=10, directed=True)
    print(graph)