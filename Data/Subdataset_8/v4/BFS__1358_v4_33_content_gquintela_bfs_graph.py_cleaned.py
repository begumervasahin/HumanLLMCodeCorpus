class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.size = 0
    def get_vertices(self):
        return list(self.adjacency_list.keys())
    def get_neighbours(self, v):
        return self.adjacency_list[v] if v in self.adjacency_list else []
    def print_vertices(self):
        print("Vertices:")
        for vertex in self.adjacency_list:
            print(vertex)
        print('\n')
    def print_neighbours(self, v):
        print("Neighbours of " + v)
        for neighbour in self.adjacency_list.get(v, []):
            print(neighbour[0] + ", weight of edge: " + str(neighbour[1]))
    def add_vertex(self, v):
        self.adjacency_list[v] = []
    def add_undirected_edge(self, u, v):
        if u not in self.adjacency_list:
            self.add_vertex(u)
        if v not in self.adjacency_list:
            self.add_vertex(v)
        self.adjacency_list[u].append(v)
    def add_directed_edge(self, u, v):
        self.add_undirected_edge(u, v)
        self.add_undirected_edge(v, u)