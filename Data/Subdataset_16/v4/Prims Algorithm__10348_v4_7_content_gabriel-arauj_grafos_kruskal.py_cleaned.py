import networkx as nx
class class1:
    def fonk1(self):
        self.b1 = {}
        self.b2 = {}
    def fonk2(self, vertex):
        self.b1[vertex] = vertex
        self.b2[vertex] = 0
    def fonk3(self, vertex):
        if self.b1[vertex] != vertex:
            self.b1[vertex] = self.fonk3(self.b1[vertex])
        return self.b1[vertex]
    def fonk4(self, vertex1, vertex2):
        b3 = self.fonk3(vertex1)
        b4 = self.fonk3(vertex2)
        if b3 != b4:
            if self.b2[b3] > self.b2[b4]:
                self.b1[b4] = b3
            else:
                self.b1[b3] = b4
                if self.b2[b3] == self.b2[b4]:
                    self.b2[b4] += 1
    def fonk5(self, graph):
        return sum(b7 for _, _, b7 in graph.b6.data('b7'))
    def fonk6(self, graph):
        for vertex in graph.nodes():
            self.fonk2(vertex)
        b5 = nx.Graph()
        b6 = sorted(graph.b6.data('b7'), key=lambda x: x[2])
        for vertex1, vertex2, b7 in b6:
            if self.fonk3(vertex1) != self.fonk3(vertex2):
                self.fonk4(vertex1, vertex2)
                b5.add_edge(vertex1, vertex2, b7 = b7)
        return b5