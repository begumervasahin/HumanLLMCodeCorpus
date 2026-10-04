
class Edge:
    def __init__(self, start_vertex, end_vertex, weight):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.weight = weight
    def __repr__(self):
        """
        Returns a string representation of the Edge object.
        Format: "e start_vertex end_vertex weight"
        """
        return f"e {self.start_vertex} {self.end_vertex} {self.weight}"
if __name__ == "__main__":
    edge = Edge(1, 2, 3.5)
    print(edge)
