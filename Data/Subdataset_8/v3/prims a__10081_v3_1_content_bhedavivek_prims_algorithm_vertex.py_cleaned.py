class Vertex:
    def __init__(self, id):
        self.position = 0
        self.parent_id = 0
        self.distance = 9999999
        self.id = id
    def get_distance(self):
        return self.distance
vertex1 = Vertex(1)
print("Distance of Vertex 1:", vertex1.get_distance())
