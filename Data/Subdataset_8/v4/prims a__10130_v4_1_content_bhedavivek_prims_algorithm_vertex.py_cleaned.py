class Vertex:
    def __init__(self, id):
        self.id = id
        self.position = 0
        self.parent_id = 0
        self.distance = float('inf')
    def get_distance(self):
        return self.distance