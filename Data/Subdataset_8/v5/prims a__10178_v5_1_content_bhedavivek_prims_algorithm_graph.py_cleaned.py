from vertex import Vertex
class Graph:
    def __init__(self, num_vertices):
        self.adjacency_list = [[] for _ in range(num_vertices)]
    def add_edge(self, source_vertex, target_vertex, weight):
        new_vertex = Vertex()
        new_vertex.id = target_vertex
        new_vertex.parent_id = source_vertex
        new_vertex.distance = weight
        new_vertex.position = 0
        self.adjacency_list[source_vertex - 1].append(new_vertex)