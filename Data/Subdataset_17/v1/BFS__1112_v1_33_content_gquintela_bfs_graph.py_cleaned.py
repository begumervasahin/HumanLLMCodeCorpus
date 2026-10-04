class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.size = 0
    def get_vertices(self):
        return list(self.adjacency_list.keys())
    def get_neighbours(self, v):
        return self.adjacency_list[v]
    def print_vertices(self):
        print("Vertices:")
        for vertex in self.adjacency_list:
            print(vertex)
        print('\n')
    def print_neighbours(self, v):
        print("Neighbours of " + v)
        for neighbour in self.adjacency_list[v]:
            print(neighbour)
        print('\n')
    def add_vertex(self, v):
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
    def add_undirected_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)
    def add_directed_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacency_list[u].append(v)
if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_undirected_edge('A', 'B')
    graph.add_undirected_edge('A', 'C')
    graph.add_directed_edge('B', 'C')
    graph.print_vertices()
    graph.print_neighbours('A')
    graph.print_neighbours('B')
    graph.print_neighbours('C')