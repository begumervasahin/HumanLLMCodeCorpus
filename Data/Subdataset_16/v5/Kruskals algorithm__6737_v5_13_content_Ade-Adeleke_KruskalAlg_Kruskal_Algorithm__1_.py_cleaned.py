class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, vertex):
        self.b1[vertex] = vertex
    def fonk3(self, vertex):
        if self.b1[vertex] != vertex:
            self.b1[vertex] = self.fonk3(self.b1[vertex])
        return self.b1[vertex]
    def fonk4(self, u, v):
        b2 = self.fonk3(u)
        b3 = self.fonk3(v)
        if b2 != b3:
            self.b1[b2] = b3
def fonk5(graph):
    b4 = class1()
    b5 = set()
    for vertex in graph['V']:
        b4.fonk2(vertex)
    b6 = sorted(graph['E'])
    for weight, u, v in b6:
        if b4.fonk3(u) != b4.fonk3(v):
            b5.add((weight, u, v))
            b4.fonk4(u, v)
    return b5