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
        print()
    def print_neighbours(self, vertex):
        if vertex in self.adjacency_list:
            print(f"Neighbours of {vertex}:")
            for neighbour, weight in self.adjacency_list[vertex]:
                print(f"{neighbour}, weight of edge: {weight}")
        else:
            print(f"Vertex {vertex} does not exist in the graph.")
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    def add_undirected_edge(self, vertex1, vertex2, weight=1):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.adjacency_list[vertex1].append((vertex2, weight))
        self.adjacency_list[vertex2].append((vertex1, weight))
    def add_directed_edge(self, source, destination, weight=1):
        self.add_vertex(source)
        self.adjacency_list[source].append((destination, weight))
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