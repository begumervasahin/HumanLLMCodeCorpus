import random
class Vertex:
    def __init__(self, label):
        self.label = label
        self.connections = []
    def add_connection(self, vertex_label, weight):
        self.connections.append((vertex_label, weight))
    def remove_connection(self, vertex_label):
        self.connections = [conn for conn in self.connections if conn[0] != vertex_label]
    def has_connection(self, vertex_label):
        return any(conn[0] == vertex_label for conn in self.connections)
def defined_degree_graph(num_vertices, degree):
    vertices = [Vertex(i) for i in range(num_vertices)]
    edges = []
    vertex_indices = list(range(num_vertices))
    random.shuffle(vertex_indices)
    for i in range(num_vertices):
        left, right = i, i
        for _ in range(degree
            left = (left + 1) % num_vertices
            right = (right - 1) % num_vertices
            if left > i:
                weight = random.randint(0, 100)
                vertices[vertex_indices[i]].add_connection(vertex_indices[left], weight)
                vertices[vertex_indices[left]].add_connection(vertex_indices[i], weight)
                edges.append((min(vertex_indices[i], vertex_indices[left]),
                              max(vertex_indices[i], vertex_indices[left]),
                              weight))
            if right > i:
                weight = random.randint(0, 100)
                vertices[vertex_indices[i]].add_connection(vertex_indices[right], weight)
                vertices[vertex_indices[right]].add_connection(vertex_indices[i], weight)
                edges.append((min(vertex_indices[i], vertex_indices[right]),
                              max(vertex_indices[i], vertex_indices[right]),
                              weight))
    with open('./edges.txt', 'a') as file:
        for edge in edges:
            file.write(f"{edge[0]} {edge[1]} {edge[2]}\n")
    return vertices
defined_degree_graph(5000, 6)
defined_degree_graph(5000, 1000)