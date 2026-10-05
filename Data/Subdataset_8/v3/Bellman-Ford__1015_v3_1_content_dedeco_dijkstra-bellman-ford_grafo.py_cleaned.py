class Vertex:
    def __init__(self, id):
        self.id = id
        self.adjacent_vertices = {}
    def add_adjacent_vertex(self, adjacent_vertex, weight=0):
        self.adjacent_vertices[adjacent_vertex] = weight
class Graph:
    def __init__(self, directed=False):
        self.vertices = {}
        self.directed = directed
    def add_vertex(self, id):
        vertex = Vertex(id)
        self.vertices[id] = vertex
        return vertex
    def add_edge(self, from_vertex_id, to_vertex_id, weight=0):
        if from_vertex_id not in self.vertices:
            self.add_vertex(from_vertex_id)
        if to_vertex_id not in self.vertices:
            self.add_vertex(to_vertex_id)
        from_vertex = self.vertices[from_vertex_id]
        to_vertex = self.vertices[to_vertex_id]
        from_vertex.add_adjacent_vertex(to_vertex, weight)
        if not self.directed:
            to_vertex.add_adjacent_vertex(from_vertex, weight)
    def get_vertices(self):
        return list(self.vertices.values())
    def get_vertex(self, id):
        return self.vertices.get(id)
    def get_edges(self):
        edges = set()
        for vertex in self.vertices.values():
            for adjacent_vertex, weight in vertex.adjacent_vertices.items():
                edges.add((vertex, adjacent_vertex, weight))
        return edges
    def __iter__(self):
        return iter(self.vertices.values())