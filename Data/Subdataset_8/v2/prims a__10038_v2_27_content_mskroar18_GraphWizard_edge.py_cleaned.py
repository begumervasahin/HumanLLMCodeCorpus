class Edge:
    def __init__(self, vertex1, vertex2, weight, extra=0, selected=False):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight
        self.extra = extra
        self.selected = selected
    def __repr__(self):
        return f"Edge(Vertex1: {self.vertex1}, Vertex2: {self.vertex2}, Weight: {self.weight}, Extra: {self.extra}, Selected: {self.selected})"
if __name__ == "__main__":
    edge1 = Edge(1, 2, 5)
    print(edge1)
    edge2 = Edge(2, 3, 7, extra=2, selected=True)
    print(edge2)