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
        print()
    def print_neighbours(self, v):
        if v in self.adjacency_list:
            print(f"Neighbours of {v}:")
            for neighbour, weight in self.adjacency_list[v]:
                print(f"{neighbour}, weight of edge: {weight}")
        else:
            print(f"Vertex {v} does not exist in the graph.")
    def add_vertex(self, v):
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
    def add_undirected_edge(self, u, v, weight=1):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))
    def add_directed_edge(self, u, v, weight=1):
        self.add_vertex(u)
        self.adjacency_list[u].append((v, weight))
if __name__ == "__main__":
    graph = Graph()
    graph.add_undirected_edge('A', 'B')
    graph.add_undirected_edge('A', 'C')
    graph.add_directed_edge('B', 'D')
    graph.print_vertices()
    graph.print_neighbours('A')
    graph.print_neighbours('B')
    graph.print_neighbours('C')
    graph.print_neighbours('D')