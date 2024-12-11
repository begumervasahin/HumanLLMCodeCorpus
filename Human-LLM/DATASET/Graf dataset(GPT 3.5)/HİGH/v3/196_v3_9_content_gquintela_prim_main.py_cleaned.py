class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, start, end, weight):
        if start not in self.b1:
            self.b1[start] = {}
        self.b1[start][end] = weight
        if end not in self.b1:
            self.b1[end] = {}
def fonk3(graph, start_vertex):
    b2 = {vertex: False for vertex in graph.b1}
    b3 = {vertex: None for vertex in graph.b1}
    b4 = {vertex: float('inf') for vertex in graph.b1}
    b4[start_vertex] = 0
    while False in b2.values():
        b5 = min(filter(lambda x: not b2[x], b4), b4=b4.get)
        b2[b5] = True
        for v, weight in graph.b1[b5].items():
            if not b2[v] and weight < b4[v]:
                b3[v] = b5
                b4[v] = weight
    b6 = class1()
    for v in b3:
        if b3[v] is not None:
            b6.fonk2(b3[v], v, graph.b1[b3[v]][v])
    return b6
def fonk4():
    b7 = class1()
    b7.fonk2('a', 'b', 4)
    b7.fonk2('a', 'h', 8)
    b7.fonk2('b', 'c', 8)
    b7.fonk2('c', 'd', 7)
    b7.fonk2('b', 'h', 11)
    b7.fonk2('h', 'i', 7)
    b7.fonk2('i', 'c', 2)
    b7.fonk2('i', 'g', 6)
    b7.fonk2('h', 'g', 1)
    b7.fonk2('g', 'f', 2)
    b7.fonk2('c', 'f', 4)
    b7.fonk2('d', 'f', 14)
    b7.fonk2('d', 'e', 9)
    b7.fonk2('f', 'e', 10)
    b6 = fonk3(b7, 'a')
    for start_vertex, edges in b6.b1.items():
        for end_vertex, weight in edges.items():
            print(f"({start_vertex}, {end_vertex}, {weight})")
if b8 = = "__main__":
    fonk4()