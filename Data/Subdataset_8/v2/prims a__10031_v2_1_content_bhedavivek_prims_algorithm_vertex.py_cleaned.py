
class Vertex:
    def __init__(self, id):
        self.position = 0
        self.parentId = 0
        self.distance = 9999999
        self.id = id
    def getDistance(self):
        return self.distance
vertex1 = Vertex(1)
print("Distance of Vertex 1:", vertex1.getDistance())
