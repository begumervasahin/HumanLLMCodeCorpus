class Edge:
    def __init__(self, vertex1, vertex2, weight, extra):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight
        self.extra = extra
        self.selected = False
    def __repr__(self):
        return f"Vertex1: {self.vertex1}  Vertex2: {self.vertex2}  Weight: {self.weight}  Selected: {self.selected}"
if __name__ == "__main__":
    edge = Edge(1, 2, 10, 0)
    print(edge)