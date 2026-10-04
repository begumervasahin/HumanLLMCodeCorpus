'''
Emmanuel John (emmanuj)
'''
class Edge:
    def __init__(self, b, e, w):
        self.u = b
        self.v = e
        self.weight = w
    def __repr__(self):
        return "e " + str(self.u) + " " + str(self.v) + " " + str(self.weight)
if __name__ == "__main__":
    edge = Edge(1, 2, 3.5)
    print(edge)
