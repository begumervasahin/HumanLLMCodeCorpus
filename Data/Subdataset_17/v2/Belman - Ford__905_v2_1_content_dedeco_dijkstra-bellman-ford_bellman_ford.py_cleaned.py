from utils import initialize_single_source, relax
class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = Vertex(vertex)
    def add_edge(self, u, v, weight):
        if u not in self.vertices:
            self.add_vertex(u)
        if v not in self.vertices:
            self.add_vertex(v)
        self.edges.append((u, v, weight))
        self.vertices[u].add_neighbor(self.vertices[v], weight)
    def get_vertices(self):
        return self.vertices.values()
    def get_edges(self):
        return self.edges
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.distance = float('Inf')
        self.visited = False
    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight
    def get_connections(self):
        return self.connected_to.keys()
    def get_id(self):
        return self.id
    def get_weight(self, neighbor):
        return self.connected_to[neighbor]
    def set_distance(self, dist):
        self.distance = dist
    def get_distance(self):
        return self.distance
    def set_visited(self):
        self.visited = True
    def get_visited(self):
        return self.visited
def bellman_ford(graph, start):
    initialize_single_source(graph, start)
    for _ in range(len(graph.get_vertices()) - 1):
        for u, v, weight in graph.get_edges():
            if v.get_visited():
                continue
            relax(u, v, weight)
    for u, v, weight in graph.get_edges():
        if v.get_distance() > u.get_distance() + u.get_weight(v):
            print("Graph contains a negative weight cycle")
            return False
    return True
if __name__ == "__main__":
    graph = Graph()
    edges = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 2),
        (3, 2, 5),
        (3, 1, 1),
        (4, 3, -3)
    ]
    for u, v, w in edges:
        graph.add_edge(u, v, w)
    start_vertex = graph.vertices[0]
    result = bellman_ford(graph, start_vertex)
    print("No negative weight cycle detected" if result else "Graph contains a negative weight cycle")