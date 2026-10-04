class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.num_edges = 0
        self.adjacency_list = {i: [] for i in range(num_vertices)}
    def is_vertex(self, vertex):
        return vertex in self.adjacency_list
    def get_all_vertices(self):
        return list(self.adjacency_list.keys())
    def get_neighbours(self, vertex):
        if self.is_vertex(vertex):
            return self.adjacency_list[vertex]
        return False
    def is_edge(self, vertex1, vertex2):
        if self.is_vertex(vertex1):
            return vertex2 in self.adjacency_list[vertex1]
        return False
    def add_edge(self, vertex1, vertex2):
        if not self.is_edge(vertex1, vertex2):
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            self.num_edges += 1
            return True
        return False
    def get_num_vertices(self):
        return self.num_vertices
    def get_num_edges(self):
        return self.num_edges
    def get_degree(self, vertex):
        if self.is_vertex(vertex):
            return len(self.adjacency_list[vertex])
        return False