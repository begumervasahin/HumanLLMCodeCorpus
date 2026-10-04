class Vertex:
    def __init__(self, id):
        self.id = id
        self._adjacent_vertices = {}
    def add_adjacent_vertex(self, vertex, weight):
        self._adjacent_vertices[vertex] = weight
    def __repr__(self):
        return f"Vertex(id={self.id})"