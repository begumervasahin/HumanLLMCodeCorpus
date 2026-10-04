class Vertex:
    def __init__(self, vertex):
        self.name = vertex
        self.neighbors = []
    def add_neighbor(self, neighbor):
        if isinstance(neighbor, Vertex):
            if neighbor.name not in self.neighbors:
                self.neighbors.append(neighbor.name)
                neighbor.neighbors.append(self.name)
                self.neighbors = sorted(self.neighbors)
                neighbor.neighbors = sorted(neighbor.neighbors)
        else:
            return False
    def __repr__(self):
        return str(self.neighbors)
if __name__ == "__main__":
    v1 = Vertex("A")
    v2 = Vertex("B")
    v3 = Vertex("C")
    v1.add_neighbor(v2)
    v1.add_neighbor(v3)
    print(f"Neighbors of {v1.name}: {v1}")
    print(f"Neighbors of {v2.name}: {v2}")
    print(f"Neighbors of {v3.name}: {v3}")