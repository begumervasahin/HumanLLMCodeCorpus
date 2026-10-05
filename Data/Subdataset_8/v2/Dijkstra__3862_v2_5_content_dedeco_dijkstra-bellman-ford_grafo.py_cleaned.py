class Vertex:
    def __init__(self, identifier):
        self.id = identifier
        self.adjacent_vertices = {}
    def add_adjacent_vertex(self, vertex, weight=0):
        self.adjacent_vertices[vertex] = weight
    def get_adjacent_vertices(self):
        return list(self.adjacent_vertices.keys())
    def get_weight(self, vertex):
        return self.adjacent_vertices[vertex]
class Graph:
    def __init__(self, directed=False):
        self.vertices = {}
        self.directed = directed
    def add_vertex(self, identifier):
        if identifier not in self.vertices:
            vertex = Vertex(identifier)
            self.vertices[identifier] = vertex
            return vertex
        else:
            return None
    def add_edge(self, source, destination, weight=0):
        if source not in self.vertices:
            self.add_vertex(source)
        if destination not in self.vertices:
            self.add_vertex(destination)
        self.vertices[source].add_adjacent_vertex(self.vertices[destination], weight)
        if not self.directed:
            self.vertices[destination].add_adjacent_vertex(self.vertices[source], weight)
    def get_vertices(self):
        return list(self.vertices.values())
    def get_vertex(self, identifier):
        return self.vertices.get(identifier, None)
    def get_edges(self):
        edges = set()
        for vertex in self.vertices.values():
            for adjacent_vertex, weight in vertex.adjacent_vertices.items():
                edges.add((vertex.id, adjacent_vertex.id, weight))
        return edges
    def __iter__(self):
        return iter(self.vertices.values())
