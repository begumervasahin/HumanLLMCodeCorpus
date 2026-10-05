class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = {}
    def fonk2(self, adjacent_vertex, b3 = 0):
        self.b2[adjacent_vertex] = b3
class class2:
    def fonk3(self, b4 = False):
        self.b5 = {}
        self.b4 = b4
    def fonk4(self, b1):
        b6 = class1(b1)
        self.b5[b1] = b6
        return b6
    def fonk5(self, from_vertex_id, to_vertex_id, b3 = 0):
        if from_vertex_id not in self.b5:
            self.fonk4(from_vertex_id)
        if to_vertex_id not in self.b5:
            self.fonk4(to_vertex_id)
        b7 = self.b5[from_vertex_id]
        b8 = self.b5[to_vertex_id]
        b7.fonk2(b8, b3)
        if not self.b4:
            b8.fonk2(b7, b3)
    def fonk6(self):
        return list(self.b5.values())
    def fonk7(self, b1):
        return self.b5.get(b1)
    def fonk8(self):
        b9 = set()
        for b6 in self.b5.values():
            for adjacent_vertex, b3 in b6.b2.items():
                b9.add((b6, adjacent_vertex, b3))
        return b9
    def fonk9(self):
        return iter(self.b5.values())