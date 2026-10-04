from vertex import Vertex
class Graph:
    def __init__(self, directed=False):
        self._vertices = {}
        self.directed = directed
    def add_vertex(self, id):
        vertex = Vertex(id)
        self._vertices[id] = vertex
        return vertex
    def add_edge(self, from_id, to_id, weight=0):
        if from_id not in self._vertices:
            self.add_vertex(from_id)
        if to_id not in self._vertices:
            self.add_vertex(to_id)
        self._vertices[from_id].add_adjacent_vertex(self._vertices[to_id], weight)
        if not self.directed:
            self._vertices[to_id].add_adjacent_vertex(self._vertices[from_id], weight)
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