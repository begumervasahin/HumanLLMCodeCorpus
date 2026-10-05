import random
class class1:
    def fonk1(self, b1 = False):
        self.b2 = {}
        self.b3 = False
        self.b4 = b1
    def fonk2(self):
        return list(self.b2.keys())
    def fonk3(self):
        b5 = set()
        b6 = []
        for vertex in self.fonk2():
            for adjacent_vertex in self.fonk4(vertex):
                b7 = self.fonk8((vertex, adjacent_vertex))
                b8 = (vertex, adjacent_vertex, b7)
                b9 = (min(vertex, adjacent_vertex), max(vertex, adjacent_vertex))
                if b9 not in b5:
                    b6.append(b8)
                    b5.add(b9)
        return b6
    def fonk4(self, vertex):
        return list(self.b2.get(vertex, {}).keys())
    def fonk5(self, origin, vertex):
        return vertex in self.b2.get(origin, {})
    def fonk6(self, vertex):
        if vertex not in self.b2:
            self.b2[vertex] = {}
    def fonk7(self, b8, b7 = 1):
        vertex1, b10 = b8
        self.b2[vertex1][b10] = b7
        if self.fonk11():
            self.b2[b10][vertex1] = b7
        self.b3 = self.b3 or b7 != 1
    def fonk8(self, b8):
        vertex1, b10 = b8
        return self.b2[vertex1].get(b10, None)
    def fonk9(self):
        b11 = self.fonk2()
        return random.choice(b11)
    def fonk10(self):
        return self.b3
    def fonk11(self):
        return self.b4