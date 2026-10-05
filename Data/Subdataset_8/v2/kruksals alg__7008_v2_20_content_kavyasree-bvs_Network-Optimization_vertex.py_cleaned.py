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
        return str(self.neighbors)
if __name__ == "__main__":
    v1 = Vertex("A")
    v2 = Vertex("B")
    v3 = Vertex("C")
    v1.add_neighbor(v2)
    v1.add_neighbor(v3)
    v2.add_neighbor(v3)
    print("Neighbors of vertex", v1.name, ":", v1)
    print("Neighbors of vertex", v2.name, ":", v2)
    print("Neighbors of vertex", v3.name, ":", v3)