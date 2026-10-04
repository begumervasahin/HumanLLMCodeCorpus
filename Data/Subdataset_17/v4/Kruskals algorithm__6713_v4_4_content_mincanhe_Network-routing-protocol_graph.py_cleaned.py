import random
class Vertex:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.connections = []
    def insert_connection(self, connection):
        self.connections.append(connection)
    def remove_connection(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
    def exists_connection(self, target_vertex):
        return any(connection[0] == target_vertex for connection in self.connections)
def defined_degree_graph(num_vertices, degree):
    vertices = [Vertex(i) for i in range(num_vertices)]
    edges = []
    vertex_ids = list(range(num_vertices))
    random.shuffle(vertex_ids)
    for i in range(num_vertices):
        current_vertex = vertex_ids[i]
        for k in range(degree
            right_index = (i + k + 1) % num_vertices
            right_vertex = vertex_ids[right_index]
            weight = random.randint(0, 100)
            vertices[current_vertex].insert_connection([right_vertex, weight])
            vertices[right_vertex].insert_connection([current_vertex, weight])
            edge = sorted([current_vertex, right_vertex]) + [weight]
            edges.append(edge)
            left_index = (i - k - 1) % num_vertices
            left_vertex = vertex_ids[left_index]
            weight = random.randint(0, 100)
            vertices[current_vertex].insert_connection([left_vertex, weight])
            vertices[left_vertex].insert_connection([current_vertex, weight])
            edge = sorted([current_vertex, left_vertex]) + [weight]
            edges.append(edge)
    with open('edges.txt', 'a') as file:
        for edge in edges:
            file.write(f"{edge[0]} {edge[1]} {edge[2]}\n")
    return vertices
defined_degree_graph(5000, 6)
defined_degree_graph(5000, 1000)