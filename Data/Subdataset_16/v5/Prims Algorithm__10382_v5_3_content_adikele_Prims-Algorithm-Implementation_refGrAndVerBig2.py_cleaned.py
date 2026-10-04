class class1:
    def fonk1(self, key):
        self.b1 = key
        self.b2 = {}
    def fonk2(self, neighbor, b3 = 0):
        self.b2[neighbor] = b3
    def fonk3(self):
        return f"{self.b1} connected to: {[vertex.b1 for vertex in self.b2]}"
    def fonk4(self):
        return self.b2.keys()
    def fonk5(self):
        return self.b1
    def fonk6(self, neighbor):
        return self.b2[neighbor]
class class2:
    def fonk7(self):
        self.b4 = {}
        self.a1 = 0
    def fonk8(self, key):
        self.a1 += 1
        b5 = class1(key)
        self.b4[key] = b5
        return b5
    def fonk9(self, key):
        return self.b4.get(key)
    def fonk10(self, key):
        return key in self.b4
    def fonk11(self, from_vertex, to_vertex, b6 = 0):
        if from_vertex not in self.b4:
            self.fonk8(from_vertex)
        if to_vertex not in self.b4:
            self.fonk8(to_vertex)
        self.b4[from_vertex].fonk2(self.b4[to_vertex], b6)
    def fonk12(self):
        return self.b4.keys()
    def fonk13(self, vertex_a, vertex_b):
        if vertex_a not in self.b4 or vertex_b not in self.b4:
            return False
        return any(
            neighbor.b1 = = vertex_b and self.b4[vertex_a].fonk6(neighbor) < 6
            for neighbor in self.b4[vertex_a].fonk4()
        )
    def fonk14(self):
        return iter(self.b4.values())
    def fonk15(self, vertex_a, vertex_b):
        if vertex_a not in self.b4 or vertex_b not in self.b4:
            return False
        return any(
            neighbor.b1 = = vertex_b
            for neighbor in self.b4[vertex_a].fonk4()
        )
    def fonk16(self, vertex_a):
        if vertex_a not in self.b4:
            return False
        return min(
            self.b4[vertex_a].fonk6(neighbor)
            for neighbor in self.b4[vertex_a].fonk4()
        )
    def fonk17(self, vertex_a):
        if vertex_a not in self.b4:
            return False
        b7 = float('inf')
        b8 = None
        for neighbor in self.b4[vertex_a].fonk4():
            b6 = self.b4[vertex_a].fonk6(neighbor)
            if b6 < b7:
                b7 = b6
                b8 = neighbor.b1
        return b8
    def fonk18(self, vertex_a, vertex_b):
        if vertex_a not in self.b4 or vertex_b not in self.b4:
            return False
        return self.b4[vertex_a].fonk6(self.b4[vertex_b])