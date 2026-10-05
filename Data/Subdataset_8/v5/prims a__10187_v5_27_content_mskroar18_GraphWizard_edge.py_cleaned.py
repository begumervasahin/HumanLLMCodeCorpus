
class Edge:
    def __init__(self, vertex1, vertex2, weight, extra):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight
        self.extra = extra
        self.selected = False
    def __repr__(self):
        return f"Vertex 1: {self.vertex1}  Vertex 2: {self.vertex2}  Weight: {self.weight}  Selected: {self.selected}"