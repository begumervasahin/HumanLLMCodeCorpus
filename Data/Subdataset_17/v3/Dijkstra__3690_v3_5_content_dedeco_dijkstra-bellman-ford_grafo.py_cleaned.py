class Vertex:
    def __init__(self, id):
        self.id = id
        self._adjacent_vertices = {}
    def add_adjacent_vertex(self, vertex, weight):
        if not isinstance(vertex, Vertex):
            raise ValueError("The vertex must be an instance of the Vertex class.")
        if not isinstance(weight, (int, float)):
            raise ValueError("The weight must be a numeric value.")
        self._adjacent_vertices[vertex] = weight
    def __repr__(self):
        return f"Vertex(id={self.id})"
    def get_adjacent_vertices(self):
        return self._adjacent_vertices