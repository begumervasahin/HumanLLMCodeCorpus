class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
    def add_neighbor(self, neighbor):
        if isinstance(neighbor, Vertex):
            if neighbor.name not in self.neighbors:
                self.neighbors.append(neighbor.name)
                neighbor.neighbors.append(self.name)
                self.neighbors.sort()
                neighbor.neighbors.sort()
        else:
            return False
    def __repr__(self):
        return f"Vertex({self.name}): Neighbors -> {self.neighbors}"