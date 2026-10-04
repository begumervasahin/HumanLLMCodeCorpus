class Vertex:
    def __init__(self, name):
        self.name = name
        self.min_distance = float('inf')
        self.previous_vertex = None
    def set_min_distance(self, dist):
        self.min_distance = dist
    def get_min_distance(self):
        return self.min_distance
    def set_previous_vertex(self, vertex):
        self.previous_vertex = vertex
    def get_previous_vertex(self):
        return self.previous_vertex
    def __str__(self):
        return self.name
if __name__ == "__main__":
    vertex_a = Vertex('A')
    vertex_b = Vertex('B')
    vertex_c = Vertex('C')
    vertex_a.set_min_distance(0)
    vertex_b.set_min_distance(10)
    vertex_c.set_min_distance(20)
    vertex_b.set_previous_vertex(vertex_a)
    vertex_c.set_previous_vertex(vertex_b)
    print(f"Vertex {vertex_a}: Min Distance -> {vertex_a.get_min_distance()}")
    print(f"Vertex {vertex_b}: Min Distance -> {vertex_b.get_min_distance()}, Previous Vertex -> {vertex_b.get_previous_vertex()}")
    print(f"Vertex {vertex_c}: Min Distance -> {vertex_c.get_min_distance()}, Previous Vertex -> {vertex_c.get_previous_vertex()}")