
class Edge:
    def __init__(self, start_vertex, end_vertex, weight):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.weight = weight
    def __repr__(self):
        return f"Edge from {self.start_vertex} to {self.end_vertex} with weight {self.weight}"