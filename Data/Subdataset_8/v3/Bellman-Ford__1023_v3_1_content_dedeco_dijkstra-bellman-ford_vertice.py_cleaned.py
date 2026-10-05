class Vertex:
    def __init__(self, id):
        self.id = id
        self.adjacent_vertices = {}
        self.distance = 0
        self.visited = False
        self.previous = None
    def get_id(self):
        return self.id
    def add_adjacent_vertex(self, vertex=None, weight=0):
        self.adjacent_vertices[vertex] = weight
    def get_adjacent_vertices(self):
        return list(self.adjacent_vertices.keys())
    def get_distance(self):
        return self.distance
    def set_distance(self, distance):
        self.distance = distance
    def mark_visited(self):
        self.visited = True
    def has_been_visited(self):
        return self.visited
    def get_weight_to_vertex(self, vertex):
        return self.adjacent_vertices[vertex]
    def set_previous_vertex(self, previous):
        self.previous = previous
    def get_previous_vertex(self):
        return self.previous
    def __str__(self):
        return str(self.id)
if __name__ == "__main__":
    vertex_a = Vertex('A')
    vertex_b = Vertex('B')
    vertex_c = Vertex('C')
    vertex_a.add_adjacent_vertex(vertex_b, 10)
    vertex_a.add_adjacent_vertex(vertex_c, 5)
    print("Vertex ID:", vertex_a.get_id())
    print("Adjacent Vertices:", vertex_a.get_adjacent_vertices())
    print("Distance:", vertex_a.get_distance())
    vertex_a.set_distance(20)
    print("Updated Distance:", vertex_a.get_distance())
    vertex_a.mark_visited()
    print("Visited:", vertex_a.has_been_visited())
    print("Weight to Vertex B:", vertex_a.get_weight_to_vertex(vertex_b))
    vertex_a.set_previous_vertex(vertex_c)
    print("Previous Vertex:", vertex_a.get_previous_vertex())
    print("Vertex Details:", vertex_a)