class Vertex:
    def __init__(self, id):
        self.id = id
        self.distance = float('inf')
        self.visited = False
    def get_distance(self):
        return self.distance
    def set_distance(self, distance):
        self.distance = distance
    def visit(self):
        self.visited = True
    def is_visited(self):
        return self.visited
class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = Vertex(vertex_id)
    def add_edge(self, source, destination, weight):
        self.add_vertex(source)
        self.add_vertex(destination)
        self.edges.append((source, destination, weight))
    def get_vertices(self):
        return self.vertices.values()
    def get_edges(self):
        return [(self.vertices[u], self.vertices[v], weight) for u, v, weight in self.edges]
def initialize_single_source(graph, source):
    for vertex in graph.get_vertices():
        vertex.set_distance(float('inf'))
        vertex.visited = False
    graph.get_vertex(source).set_distance(0)
def relax(u, v, weight):
    if v.get_distance() > u.get_distance() + weight:
        v.set_distance(u.get_distance() + weight)
def bellman_ford(graph, source):
    initialize_single_source(graph, source)
    for _ in range(len(graph.get_vertices()) - 1):
        for u, v, weight in graph.get_edges():
            if not v.is_visited():
                relax(u, v, weight)
    for u, v, weight in graph.get_edges():
        if v.get_distance() > u.get_distance() + weight:
            return False
    return True
graph = Graph()
graph.add_edge('A', 'B', -1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 3)
graph.add_edge('B', 'D', 2)
graph.add_edge('B', 'E', 2)
graph.add_edge('D', 'C', 5)
graph.add_edge('D', 'B', 1)
graph.add_edge('E', 'D', -3)
print("Graph contains negative-weight cycle:", not bellman_ford(graph, 'A'))