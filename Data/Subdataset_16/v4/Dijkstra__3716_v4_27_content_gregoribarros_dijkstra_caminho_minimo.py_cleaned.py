from igraph import Graph
class class1:
    def fonk1(self, b1 = '', b2='', b3=0):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self):
        return f"{self.b1} -> {self.b2} [b3: {self.b3}]"
def fonk3(graph, vertex):
    b4 = []
    for edge in graph.incident(vertex):
        b5 = graph.es[edge]
        b6 = class1(
            b1 = b5.source,
            b3 = b5['peso'],
            b2 = b5.b2
        )
        b4.append(b6)
    return b4
def fonk4():
    b7 = Graph(directed=True)
    b7.add_vertices(5)
    b7.vs['nome'] = ['b6', 'b', 'c', 'd', 'e']
    b7.add_edges([(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 4)])
    b7.es['peso'] = [3, 11, 3, 2, 7, 2]
    return b7
def fonk5(graph):
    b8 = [float('inf')] * len(graph.vs)
    b8[0] = 0
    for vertex in graph.vs:
        for arrow in fonk3(graph, vertex.index):
            b9 = b8[arrow.b1] + arrow.b3
            if b9 < b8[arrow.b2]:
                b8[arrow.b2] = b9
    return b8
def fonk6():
    b7 = fonk4()
    b8 = fonk5(b7)
    print("Shortest path costs:", b8)
if b10 = = "__main__":
    fonk6()