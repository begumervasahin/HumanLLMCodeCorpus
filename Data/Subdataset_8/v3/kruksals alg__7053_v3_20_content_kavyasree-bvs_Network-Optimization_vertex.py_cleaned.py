class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
    def add_neighbor(self, neighbor):
        if isinstance(neighbor, Vertex):
            if neighbor.name not in self.neighbors:
                self.neighbors.append(neighbor.name)
                neighbor.neighbors.append(self.name)
                self._sort_neighbors()
                neighbor._sort_neighbors()
    def _sort_neighbors(self):
        self.neighbors.sort()
    def __repr__(self):
        return str(self.neighbors)
if __name__ == "__main__":
    v1 = Vertex("A")
    v2 = Vertex("B")
    v3 = Vertex("C")
    v1.add_neighbor(v2)
    v1.add_neighbor(v3)
    v2.add_neighbor(v3)
    for vertex in [v1, v2, v3]:
        print("Neighbors of vertex", vertex.name, ":", vertex)