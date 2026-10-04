
class Vertex:
    def __init__(self, id):
        self.id = id
        self.adjacent = {}
        self.distance = float('inf')
        self.visited = False
    def add_adjacent(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
    def get_adjacent(self):
        return self.adjacent.keys()
    def get_id(self):
        return self.id
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
    def set_distance(self, dist):
        self.distance = dist
    def get_distance(self):
        return self.distance
    def set_visited(self):
        self.visited = True
    def is_visited(self):
        return self.visited
from vertice import Vertex
class Graph:
    def __init__(self, directed=False):
        self.vertices = {}
        self.directed = directed
    def add_vertex(self, id):
        v = Vertex(id)
        self.vertices[id] = v
        return v
    def add_edge(self, from_vert, to_vert, weight=0):
        if from_vert not in self.vertices:
            self.add_vertex(from_vert)
        if to_vert not in self.vertices:
            self.add_vertex(to_vert)
        self.vertices[from_vert].add_adjacent(self.vertices[to_vert], weight)
        if not self.directed:
            self.vertices[to_vert].add_adjacent(self.vertices[from_vert], weight)
    def get_vertices(self):
        return [v for k, v in self.vertices.items()]
    def get_vertex(self, id):
        if id in self.vertices:
            return self.vertices[id]
        else:
            return None
    def get_edges(self):
        edges = set()
        for id, v in self.vertices.items():
            for a in v.adjacent:
                edges.add((v, a))
        return edges
    def __iter__(self):
        return iter(self.vertices.values())
if __name__ == "__main__":
    graph = Graph(directed=False)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 1)
    graph.add_edge(2, 1, 2)
    graph.add_edge(1, 3, 1)
    graph.add_edge(2, 3, 5)
    graph.add_edge(3, 4, 3)
    print("Vertices of graph:")
    for vertex in graph:
        print(f"Vertex {vertex.id}")
    print("\nEdges of graph:")
    for edge in graph.get_edges():
        print(f"Edge from {edge[0].id} to {edge[1].id} with weight {edge[0].get_weight(edge[1])}")
    v = graph.get_vertex(2)
    if v:
        print(f"\nVertex {v.id} found in graph")
    else:
        print("\nVertex not found in graph")