import random
class Vertex:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.connections = []
    def insert_connection(self, target_vertex, weight):
        self.connections.append((target_vertex, weight))
    def remove_connection(self, target_vertex):
        self.connections = [
            connection for connection in self.connections
            if connection[0] != target_vertex
        ]
    def exists_connection(self, target_vertex):
        return any(connection[0] == target_vertex for connection in self.connections)
def defined_degree_graph(num_vertices, degree):
    vertices = [Vertex(i) for i in range(num_vertices)]
    edges = []
    vertex_ids = list(range(num_vertices))
    random.shuffle(vertex_ids)
    for i in range(num_vertices):
        current_vertex = vertex_ids[i]
        for k in range(1, degree
            right_index = (i + k) % num_vertices
            right_vertex = vertex_ids[right_index]
            _add_edge(vertices, current_vertex, right_vertex, edges)
            left_index = (i - k) % num_vertices
            left_vertex = vertex_ids[left_index]
            _add_edge(vertices, current_vertex, left_vertex, edges)
    _write_edges_to_file('edges.txt', edges)
    return vertices
def _add_edge(vertices, vertex_a, vertex_b, edges):
    weight = random.randint(0, 100)
    vertices[vertex_a].insert_connection(vertex_b, weight)
    vertices[vertex_b].insert_connection(vertex_a, weight)
    edges.append(sorted([vertex_a, vertex_b]) + [weight])
def _write_edges_to_file(filename, edges):
    with open(filename, 'a') as file:
        for edge in edges:
            file.write(f"{edge[0]} {edge[1]} {edge[2]}\n")
defined_degree_graph(5000, 6)
defined_degree_graph(5000, 1000)