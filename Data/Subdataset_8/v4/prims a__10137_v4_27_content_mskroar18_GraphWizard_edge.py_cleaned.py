class Edge:
    def __init__(self, Vertex1, Vertex2, weight, extra):
        self.Vertex1 = Vertex1
        self.Vertex2 = Vertex2
        self.weight = weight
        self.extra = extra
        self.selected = False
    def __repr__(self):
        return f"V1: {self.Vertex1}  V2: {self.Vertex2}  W: {self.weight}  SEL: {self.selected}"