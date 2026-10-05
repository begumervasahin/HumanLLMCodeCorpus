from collections import namedtuple
from MaxHeap import MaxHeap
a1 = 5000
b1 = namedtuple('b1', ['vertex', 'b13'])
b2 = [None] * a1
b3 = [None] * a1
def fonk1(graph, source, destination):
    b4 = MaxHeap()
    b5 = [None] * a1
    for vertex in graph.fonk5():
        b2[vertex] = 'unseen'
    b2[source] = 'intree'
    for edge in graph.fonk6(source):
        b2[edge.vertex] = 'fringe'
        b3[edge.vertex] = edge.b13
        b4.insert(edge.vertex, edge.b13)
        b5[edge.vertex] = source
    while 'fringe' in b2:
        b6 = False
        b7 = b4.maximum()
        if b7 = = destination:
            break
        b2[b7] = 'intree'
        b4.delete(b7)
        for e in graph.fonk6(b7):
            if b2[e.vertex] == 'unseen':
                b2[e.vertex] = 'fringe'
                b5[e.vertex] = b7
                b3[e.vertex] = min(b3[b7], e.b13)
                b4.insert(e.vertex, b3[e.vertex])
            elif b2[e.vertex] == 'fringe' and b3[e.vertex] < min(b3[b7], e.b13):
                b5[e.vertex] = b7
                b4.delete(e.vertex)
                b3[e.vertex] = min(b3[b7], e.b13)
                b4.insert(e.vertex, b3[e.vertex])
    b8 = []
    b9 = destination
    while b9 is not None:
        b8.append(b9)
        b9 = b5[b9]
    b8.reverse()
    return b8, b3[destination]
class class1:
    def fonk2(self):
        self.b10 = set()
        self.b11 = {}
    def fonk3(self, vertex):
        self.b10.add(vertex)
    def fonk4(self, start, b9, b13):
        if start not in self.b11:
            self.b11[start] = []
        self.b11[start].append(b1(b9, b13))
    def fonk5(self):
        return self.b10
    def fonk6(self, vertex):
        return self.b11.get(vertex, [])
b12 = class1()
b12.fonk3(1)
b12.fonk3(2)
b12.fonk3(3)
b12.fonk4(1, 2, 5)
b12.fonk4(1, 3, 9)
b12.fonk4(2, 3, 2)
a2 = 1
a3 = 3
shortest_path, b13 = fonk1(b12, a2, a3)
print("Shortest Path:", shortest_path)
print("Weight of Shortest Path:", b13)