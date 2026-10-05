class Edge:
    def __init__(self, b, e, w):
        self.u = b
        self.v = e
        self.weight = w
    def __repr__(self):
        return "e " + str(self.u) + " " + str(self.v) + " " + str(self.weight)
edge1 = Edge('a', 'b', 5)
edge2 = Edge('b', 'c', 7)
edge3 = Edge('c', 'd', 3)
print(edge1)
print(edge2)
print(edge3)
