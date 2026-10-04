class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight
    def __str__(self):
        return f"{self.id} connected to: {[vertex.id for vertex in self.connected_to]}"
    def get_connections(self):
        return self.connected_to.keys()
    def get_id(self):
        return self.id
    def get_weight(self, neighbor):
        return self.connected_to[neighbor]
class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0
    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex
    def get_vertex(self, key):
        return self.vert_list.get(key)
    def __contains__(self, key):
        return key in self.vert_list
    def add_edge(self, from_vertex, to_vertex, cost=0):
        if from_vertex not in self.vert_list:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vert_list:
            self.add_vertex(to_vertex)
        self.vert_list[from_vertex].add_neighbor(self.vert_list[to_vertex], cost)
    def get_vertices(self):
        return self.vert_list.keys()
    def are_neighbors(self, vertex_a, vertex_b):
        if vertex_a not in self.vert_list or vertex_b not in self.vert_list:
            return False
        return any(
            neighbor.id == vertex_b and self.vert_list[vertex_a].get_weight(neighbor) < 6
            for neighbor in self.vert_list[vertex_a].get_connections()
        )
    def __iter__(self):
        return iter(self.vert_list.values())
    def is_connected(self, vertex_a, vertex_b):
        if vertex_a not in self.vert_list or vertex_b not in self.vert_list:
            return False
        return any(
            neighbor.id == vertex_b
            for neighbor in self.vert_list[vertex_a].get_connections()
        )
    def min_cost_neighbor(self, vertex_a):
        if vertex_a not in self.vert_list:
            return False
        return min(
            self.vert_list[vertex_a].get_weight(neighbor)
            for neighbor in self.vert_list[vertex_a].get_connections()
        )
    def min_cost_neighbor_id(self, vertex_a):
        if vertex_a not in self.vert_list:
            return False
        min_cost = float('inf')
        min_cost_id = None
        for neighbor in self.vert_list[vertex_a].get_connections():
            cost = self.vert_list[vertex_a].get_weight(neighbor)
            if cost < min_cost:
                min_cost = cost
                min_cost_id = neighbor.id
        return min_cost_id
    def get_edge_weight(self, vertex_a, vertex_b):
        if vertex_a not in self.vert_list or vertex_b not in self.vert_list:
            return False
        return self.vert_list[vertex_a].get_weight(self.vert_list[vertex_b])