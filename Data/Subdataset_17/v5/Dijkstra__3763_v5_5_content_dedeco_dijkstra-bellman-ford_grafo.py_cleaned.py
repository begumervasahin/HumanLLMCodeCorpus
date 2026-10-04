from vertex import Vertex
class Graph:
    def __init__(self, directed=False):
        self._vertices = {}
        self.directed = directed
    def add_vertex(self, id):
        if id not in self._vertices:
            self._vertices[id] = Vertex(id)
        return self._vertices[id]
    def add_edge(self, from_id, to_id, weight=0):
        from_vertex = self.add_vertex(from_id)
        to_vertex = self.add_vertex(to_id)
        from_vertex.add_adjacent_vertex(to_vertex, weight)
        if not self.directed:
            to_vertex.add_adjacent_vertex(from_vertex, weight)
    def get_vertices(self):
        return list(self._vertices.values())
    def get_vertex(self, id):
        return self._vertices.get(id)
    def get_edges(self):
        edges = set()
        for vertex in self._vertices.values():
            for adjacent_vertex in vertex.get_adjacent_vertices():
                edges.add((vertex, adjacent_vertex))
        return edges
    def __iter__(self):
        return iter(self._vertices.values())