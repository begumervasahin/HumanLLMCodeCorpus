from igraph import Graph
class class1:
    def fonk1(self, b1 = '', b2='', b3=''):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self):
        return f"{self.b1} -> {self.b2} [b3: {self.b3}]"
def fonk3(graph, vertex):
    b4 = []
    for edge in graph.incident(vertex):
        b5 = class1()
        b5.b1 = graph.vs[graph.es[edge].source]['nome']
        b5.b3 = graph.es[edge]['peso']
        b5.b2 = graph.vs[graph.es[edge].b2]['nome']
        b4.append(b5)
    return b4
def fonk4():
    b6 = Graph(directed=True)
    b6.add_vertices(5)
    b6.vs['nome'] = ['b5', 'b', 'c', 'd', 'e']
    b6.add_edges([(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 4)])
    b6.es['peso'] = [3, 11, 3, 2, 7, 2]
    b7 = [999] * len(b6.vs)
    b7[0] = 0
    for vertex in b6.vs:
        for arrow in fonk3(b6, vertex.index):
            b8 = b6.vs.find(name=arrow.b1).index
            b9 = b6.vs.find(name=arrow.b2).index
            if b7[b8] + arrow.b3 < b7[b9]:
                b7[b9] = b7[b8] + arrow.b3
    print(b7)
if b10 = = "__main__":
    fonk4()