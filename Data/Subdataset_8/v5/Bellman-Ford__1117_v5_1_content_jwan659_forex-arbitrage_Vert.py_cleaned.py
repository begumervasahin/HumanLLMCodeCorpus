class Vertex:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.min_distance = float('inf')
        self.adjacencies = []
        self.previous_vertex = None
        self.visited = False
    def get_min_distance(self):
        return self.min_distance
    def set_min_distance(self, distance):
        self.min_distance = distance
    def get_previous_vertex(self):
        return self.previous_vertex
    def set_previous_vertex(self, prev_vertex):
        self.previous_vertex = prev_vertex
    def add_edge(self, edge):
        self.adjacencies.append(edge)
    def get_adjacent_edges(self):
        return self.adjacencies
    def is_visited(self):
        return self.visited
    def set_visited(self, visited):
        self.visited = visited
    def __str__(self):
        return self.vertex_id
if __name__ == "__main__":
    vertex_a = Vertex('A')
    vertex_b = Vertex('B')
    vertex_c = Vertex('C')
    edge_ab = Edge(vertex_a, vertex_b, 10)
    edge_bc = Edge(vertex_b, vertex_c, 5)
    edge_ca = Edge(vertex_c, vertex_a, -15)
    vertex_a.add_edge(edge_ab)
    vertex_b.add_edge(edge_bc)
    vertex_c.add_edge(edge_ca)
    print("Vertex ID:", vertex_a)
    print("Adjacent Vertices:", [str(edge.target_vertex) for edge in vertex_a.get_adjacent_edges()])
    print("Minimum Distance:", vertex_a.get_min_distance())
    print("Previous Vertex:", vertex_a.get_previous_vertex())
    print("Visited:", vertex_a.is_visited())
    vertex_a.set_min_distance(20)
    vertex_a.set_previous_vertex(vertex_c)
    vertex_a.set_visited(True)
    print("Updated Minimum Distance:", vertex_a.get_min_distance())
    print("Updated Previous Vertex:", vertex_a.get_previous_vertex())
    print("Updated Visited:", vertex_a.is_visited())