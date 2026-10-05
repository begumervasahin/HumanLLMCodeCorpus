class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.size = 0
    def get_vertices(self):
        return list(self.adjacency_list.keys())
    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex] if vertex in self.adjacency_list else []
    def print_vertices(self):
        print("Vertices:")
        for vertex in self.adjacency_list:
            print(vertex)
        print('\n')
    def print_neighbors(self, vertex):
        print("Neighbors of " + vertex)
        for neighbor in self.adjacency_list.get(vertex, []):
            print(neighbor)
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    def add_undirected_edge(self, u, v):
        if u not in self.adjacency_list:
            self.add_vertex(u)
        if v not in self.adjacency_list:
            self.add_vertex(v)
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)
    def add_directed_edge(self, u, v):
        if u not in self.adjacency_list:
            self.add_vertex(u)
        if v not in self.adjacency_list:
            self.add_vertex(v)
        self.adjacency_list[u].append(v)