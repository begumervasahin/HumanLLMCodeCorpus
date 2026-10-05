class Edge(object):
    def __init__(self, Vertex1, Vertex2, weight, extra=0, selected=False):
        self.Vertex1 = Vertex1
        self.Vertex2 = Vertex2
        self.weight = weight
        self.extra = extra
        self.selected = selected
    def __repr__(self):
        return ("V1:  " + str(self.Vertex1) + "  V2:  " +str(self.Vertex2)+ "  W:  "+ str(self.weight)+ "  SEL:  "+ str(self.selected))
if __name__ == "__main__":
    edge1 = Edge(1, 2, 5)
    print(edge1)
    edge2 = Edge(2, 3, 7, extra=2, selected=True)
    print(edge2)