
class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.size = 0
    def get_vertices(self):
        return list(self.adjacency_list.keys())
    def get_neighbours(self, v):
        return self.adjacency_list.get(v, [])
    def print_vertices(self):
        print("Vertices:")
        for vertex in self.adjacency_list:
            print(vertex)
        print('\n')
    def print_neighbours(self, v):
        print("Neighbours of", v)
        neighbours = self.adjacency_list.get(v, [])
        for neighbour, weight in neighbours:
            print(neighbour + ", weight of edge:", weight)
    def add_vertex(self, v):
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
    def add_undirected_edge(self, u, v):
        if u not in self.adjacency_list:
            self.add_vertex(u)
        if v not in self.adjacency_list:
            self.add_vertex(v)
        self.adjacency_list[u].append((v, 0))
        self.adjacency_list[v].append((u, 0))
    def add_directed_edge(self, u, v):
        self.add_undirected_edge(u, v)
        self.adjacency_list[v].append((u, 0))
