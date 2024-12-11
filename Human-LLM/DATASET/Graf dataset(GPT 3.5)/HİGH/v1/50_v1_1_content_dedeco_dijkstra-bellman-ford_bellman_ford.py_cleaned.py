class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = float('inf')
        self.b3 = False
    def fonk2(self):
        return self.b2
    def fonk3(self, dist):
        self.b2 = dist
    def fonk4(self, b3):
        self.b3 = b3
    def fonk5(self):
        return self.b3
class class2:
    def fonk6(self):
        self.b4 = {}
        self.b5 = []
    def fonk7(self, vertex_id):
        self.b4[vertex_id] = class1(vertex_id)
    def fonk8(self, u, v, weight):
        if u not in self.b4:
            self.fonk7(u)
        if v not in self.b4:
            self.fonk7(v)
        self.b5.append((u, v, weight))
    def fonk9(self):
        return self.b4.values()
    def fonk10(self):
        return [(self.b4[u], self.b4[v], weight) for u, v, weight in self.b5]
    def fonk11(self, vertex_id):
        return self.b4.get(vertex_id)