class Graph:
    def __init__(self):
        self.adjacency_list = {}
    def get_vertices(self):
        return list(self.adjacency_list.keys())
    def get_neighbours(self, vertex):
        return self.adjacency_list.get(vertex, [])
    def print_vertices(self):
        print("Vertices:")
        for vertex in self.get_vertices():
            print(vertex)
        print()
    def print_neighbours(self, vertex):
        print(f"Neighbours of {vertex}:")
        for neighbour in self.get_neighbours(vertex):
            print(neighbour)
        print()
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    def add_undirected_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        if v not in self.adjacency_list[u]:
            self.adjacency_list[u].append(v)
        if u not in self.adjacency_list[v]:
            self.adjacency_list[v].append(u)
    def add_directed_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        if v not in self.adjacency_list[u]:
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