class Edge:
    def __init__(self, start_vertex, end_vertex, weight):
        self.u = start_vertex
        self.v = end_vertex
        self.weight = weight
    def __repr__(self):
        return f"Edge({self.u}, {self.v}, {self.weight})"