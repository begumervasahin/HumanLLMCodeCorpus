from igraph import Graph
class class1:
    def fonk1(self, b1 = '', b2='', b3=0):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self):
        return f"{self.b1} -> {self.b2} [b3: {self.b3}]"
def fonk3(b7, vertex):
    b4 = []
    for edge in b7.incident(vertex):
        b5 = b7.es[edge]
        b6 = class1(
            b1 = b5.source,
            b2 = b5.b2,
            b3 = b5['peso']
        )
        b4.append(b6)
    return b4
def fonk4():
    b7 = Graph(directed=True)
    b7.add_vertices(5)
    b7.vs['nome'] = ['a', 'b', 'c', 'd', 'e']
    b7.add_edges([(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 4)])
    b7.es['peso'] = [3, 11, 3, 2, 7, 2]
    return b7
def fonk5(b7):
    b8 = len(b7.vs)
    b9 = [float('inf')] * b8
    b9[0] = 0
    for vertex in range(b8):
        for b6 in fonk3(b7, vertex):
            b10 = b9[b6.b1] + b6.b3
            if b10 < b9[b6.b2]:
                b9[b6.b2] = b10
    return b9
def fonk6():
    b7 = fonk4()
    b9 = fonk5(b7)
    print("Shortest path costs:", b9)
if b11 = = "__main__":
    fonk6()