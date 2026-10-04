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