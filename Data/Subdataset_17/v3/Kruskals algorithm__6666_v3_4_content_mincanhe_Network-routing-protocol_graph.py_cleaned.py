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
        _connect_neighbors(vertices, vertex_indices, i, num_vertices, degree, edges)
    _write_edges_to_file(edges, './edges.txt')
    return vertices
def _connect_neighbors(vertices, vertex_indices, i, num_vertices, degree, edges):
    left, right = i, i
    for _ in range(degree
        left = (left + 1) % num_vertices
        right = (right - 1) % num_vertices
        _create_edge(vertices, vertex_indices, i, left, edges)
        _create_edge(vertices, vertex_indices, i, right, edges)
def _create_edge(vertices, vertex_indices, i, neighbor_index, edges):
    if neighbor_index > i:
        weight = random.randint(0, 100)
        current_vertex = vertices[vertex_indices[i]]
        neighbor_vertex = vertices[vertex_indices[neighbor_index]]
        current_vertex.add_connection(vertex_indices[neighbor_index], weight)
        neighbor_vertex.add_connection(vertex_indices[i], weight)
        edges.append((
            min(vertex_indices[i], vertex_indices[neighbor_index]),
            max(vertex_indices[i], vertex_indices[neighbor_index]),
            weight
        ))
def _write_edges_to_file(edges, filename):
    with open(filename, 'a') as file:
        for edge in edges:
            file.write(f"{edge[0]} {edge[1]} {edge[2]}\n")
defined_degree_graph(5000, 6)
defined_degree_graph(5000, 1000)