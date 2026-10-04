import sys
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
    def get_connections(self):
        return self.adjacent.keys()
    def get_id(self):
        return self.id
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
    def set_distance(self, distance):
        self.distance = distance
    def get_distance(self):
        return self.distance
    def set_previous(self, previous):
        self.previous = previous
    def set_visited(self):
        self.visited = True
    def __str__(self):
        return f'{self.id} adjacent(s): {[x.id for x in self.adjacent]}'
class Graph:
    def __init__(self):
        self.vertex_dict = {}
        self.num_vertices = 0
    def __iter__(self):
        return iter(self.vertex_dict.values())
    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vertex_dict[node] = new_vertex
        return new_vertex
    def get_vertex(self, node):
        return self.vertex_dict.get(node)
    def add_edge(self, from_node, to_node, cost=0):
        if from_node not in self.vertex_dict or to_node not in self.vertex_dict:
            return 'One or both nodes are not in the graph'
        self.vertex_dict[from_node].add_neighbor(self.vertex_dict[to_node], cost)
        self.vertex_dict[to_node].add_neighbor(self.vertex_dict[from_node], cost)
    def get_vertices(self):
        return self.vertex_dict.keys()
    def set_previous(self, current):
        self.previous = current
    def get_previous(self, current):
        return self.previous