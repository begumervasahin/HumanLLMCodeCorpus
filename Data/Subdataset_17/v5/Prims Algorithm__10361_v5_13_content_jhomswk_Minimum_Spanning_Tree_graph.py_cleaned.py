from random import randint
class Graph:
    def __init__(self, fname=None, num_vertices=None, num_edges=None, weight_range=None, directed=True):
        self.adjacency_list = {}
        self.edge_weights = {}
        self.directed = directed
        if fname is None:
            if any(arg is None for arg in (num_vertices, num_edges, weight_range)):
                num_vertices, num_edges, weight_range = map(int, input("Enter num_vertices, num_edges, weight_range: ").split())
            self._generate_random_graph(num_vertices, num_edges, weight_range)
        else:
            self._load_graph_from_file(fname)
    def num_vertices(self):
        return len(self.adjacency_list)
    def vertices(self):
        return range(self.num_vertices())
    def edges(self):
        return ((from_vertex, to_vertex) for from_vertex in self.vertices() for to_vertex in self.adjacency_list[from_vertex])
    def add_directed_edge(self, from_vertex, to_vertex, weight):
        self.adjacency_list.setdefault(from_vertex, set()).add(to_vertex)
        self.edge_weights[(from_vertex, to_vertex)] = weight
    def add_undirected_edge(self, from_vertex, to_vertex, weight):
        self.add_directed_edge(from_vertex, to_vertex, weight)
        self.add_directed_edge(to_vertex, from_vertex, weight)
    def _generate_random_graph(self, num_vertices, num_edges, weight_range):
        add_edge = self.add_directed_edge if self.directed else self.add_undirected_edge
        for vertex in range(num_vertices):
            self.adjacency_list[vertex] = set()
        for _ in range(num_edges):
            from_vertex, to_vertex = None, None
            while from_vertex == to_vertex:
                from_vertex = randint(0, num_vertices - 1)
                to_vertex = randint(0, num_vertices - 1)
            weight = randint(0, weight_range)
            add_edge(from_vertex, to_vertex, weight)
    def _load_graph_from_file(self, fname):
        add_edge = self.add_directed_edge if self.directed else self.add_undirected_edge
        with open(fname, 'r') as file:
            num_vertices = int(file.readline().strip())
            for vertex in range(num_vertices):
                self.adjacency_list[vertex] = set()
            for line in file:
                from_vertex, to_vertex, weight = map(int, line.split())
                add_edge(from_vertex, to_vertex, weight)
    def adjacent_str(self, from_vertex):
        return ", ".join(f"({to_vertex}, {self.edge_weights[(from_vertex, to_vertex)]})" for to_vertex in self.adjacency_list[from_vertex])
    def __str__(self):
        return "\n".join(f"{vertex}: {self.adjacent_str(vertex)}" for vertex in self.vertices())
    def __repr__(self):
        return str(self)