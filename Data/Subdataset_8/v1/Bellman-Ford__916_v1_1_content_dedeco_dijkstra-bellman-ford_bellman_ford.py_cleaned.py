class Vertex:
    def __init__(self, id):
        self.id = id
        self.distance = float('inf')
        self.visited = False
    def get_distance(self):
        return self.distance
    def set_distance(self, dist):
        self.distance = dist
    def set_visited(self, visited):
        self.visited = visited
    def get_visited(self):
        return self.visited
class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)
    def add_edge(self, u, v, weight):
        if u not in self.vertices:
            self.add_vertex(u)
        if v not in self.vertices:
            self.add_vertex(v)
        self.edges.append((u, v, weight))
    def get_vertices(self):
        return self.vertices.values()
    def get_edges(self):
        return [(self.vertices[u], self.vertices[v], weight) for u, v, weight in self.edges]
    def get_vertex(self, vertex_id):
        return self.vertices.get(vertex_id)