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
        return f"{self.neighbors}"
if __name__ == "__main__":
    vertex_a = Vertex("A")
    vertex_b = Vertex("B")
    vertex_c = Vertex("C")
    vertex_a.add_neighbor(vertex_b)
    vertex_a.add_neighbor(vertex_c)
    print(f"Neighbors of {vertex_a.name}: {vertex_a}")
    print(f"Neighbors of {vertex_b.name}: {vertex_b}")
    print(f"Neighbors of {vertex_c.name}: {vertex_c}")