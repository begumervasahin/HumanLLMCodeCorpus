class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.size = 0
    def get_vertices(self):
        return list(self.adjacency_list.keys())
    def get_neighbours(self, vertex):
        return self.adjacency_list.get(vertex, [])
    def print_vertices(self):
        print("Vertices:")
        for vertex in self.adjacency_list:
            print(vertex)
        print('\n')
    def print_neighbours(self, vertex):
        print("Neighbours of", vertex)
        neighbours = self.adjacency_list.get(vertex, [])
        for neighbour, weight in neighbours:
            print(neighbour + ", weight of edge:", weight)
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    def add_undirected_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacency_list[u].append((v, 0))
        self.adjacency_list[v].append((u, 0))
    def add_directed_edge(self, u, v):
        self.add_undirected_edge(u, v)
        self.adjacency_list[v].append((u, 0))
