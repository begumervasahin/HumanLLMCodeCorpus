from vertex import Vertex
class class1:
    def fonk1(self, b1 = False):
        self.b2 = {}
        self.b1 = b1
    def fonk2(self, id):
        if id not in self.b2:
            self.b2[id] = Vertex(id)
        return self.b2[id]
    def fonk3(self, from_id, to_id, b3 = 0):
        b4 = self.fonk2(from_id)
        b5 = self.fonk2(to_id)
        b4.add_adjacent_vertex(b5, b3)
        if not self.b1:
            b5.add_adjacent_vertex(b4, b3)
    def fonk4(self):
        return list(self.b2.values())
    def fonk5(self, id):
        return self.b2.get(id)
    def fonk6(self):
        b6 = set()
        for vertex in self.b2.values():
            for adjacent_vertex in vertex.get_adjacent_vertices():
                b6.add((vertex, adjacent_vertex))
        return b6
    def fonk7(self):
        return iter(self.b2.values())