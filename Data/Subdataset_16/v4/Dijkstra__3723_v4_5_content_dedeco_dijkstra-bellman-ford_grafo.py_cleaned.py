from b3 import Vertex
class class1:
    def fonk1(self, b1 = False):
        self.b2 = {}
        self.b1 = b1
    def fonk2(self, id):
        b3 = Vertex(id)
        self.b2[id] = b3
        return b3
    def fonk3(self, from_id, to_id, b4 = 0):
        if from_id not in self.b2:
            self.fonk2(from_id)
        if to_id not in self.b2:
            self.fonk2(to_id)
        self.b2[from_id].add_adjacent_vertex(self.b2[to_id], b4)
        if not self.b1:
            self.b2[to_id].add_adjacent_vertex(self.b2[from_id], b4)
    def fonk4(self):
        return list(self.b2.values())
    def fonk5(self, id):
        return self.b2.get(id)
    def fonk6(self):
        b5 = set()
        for b3 in self.b2.values():
            for adjacent_vertex in b3.get_adjacent_vertices():
                b5.add((b3, adjacent_vertex))
        return b5
    def fonk7(self):
        return iter(self.b2.values())