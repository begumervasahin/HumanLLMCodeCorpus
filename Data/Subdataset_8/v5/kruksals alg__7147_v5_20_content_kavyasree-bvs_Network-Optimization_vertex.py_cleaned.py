class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
    def add_neighbor(self, neighbor):
        if not isinstance(neighbor, Vertex):
            return False
        if neighbor.name not in self.neighbors:
            self.neighbors.append(neighbor.name)
            neighbor.neighbors.append(self.name)
            self.neighbors.sort()
            neighbor.neighbors.sort()
    def __repr__(self):
        return str(self.neighbors)