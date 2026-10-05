from collections import namedtuple
import MaxHeap
a1 = 5000
b1 = namedtuple('b1', ['vertex', 'b12'])
b2 = [None] * a1
b3 = [None] * a1
def fonk1(graph, source, destination):
    MaxHeap.initialize()
    b4 = [None] * a1
    for i in graph.fonk5():
        b2[i] = 'unseen'
    b2[source] = 'intree'
    for i in graph.fonk6(source):
        b2[i.vertex] = 'fringe'
        b3[i.vertex] = i.b12
        MaxHeap.Insert(i.vertex, i.b12)
        b4[i.vertex] = source
    while 'fringe' in b2:
        b5 = False
        b6 = MaxHeap.Max()
        if b6 = = destination:
            break
        b2[b6] = 'intree'
        MaxHeap.Delete(b6)
        for e in graph.fonk6(b6):
            if b2[e.vertex] == 'unseen':
                b2[e.vertex] = 'fringe'
                b4[e.vertex] = b6
                b3[e.vertex] = min(b3[b6], e.b12)
                MaxHeap.Insert(e.vertex, b3[e.vertex])
            elif b2[e.vertex] == 'fringe' and b3[e.vertex] < min(b3[b6], e.b12):
                b4[e.vertex] = b6
                MaxHeap.Delete(e.vertex)
                b3[e.vertex] = min(b3[b6], e.b12)
                MaxHeap.Insert(e.vertex, b3[e.vertex])
    b7 = []
    b8 = destination
    while b8 is not None:
        b7.append(b8)
        b8 = b4[b8]
    b7.reverse()
    return b7, b3[destination]
class class1:
    def fonk2(self):
        self.b9 = set()
        self.b10 = {}
    def fonk3(self, vertex):
        self.b9.add(vertex)
    def fonk4(self, start, b8, b12):
        if start not in self.b10:
            self.b10[start] = []
        self.b10[start].append(b1(b8, b12))
    def fonk5(self):
        return self.b9
    def fonk6(self, vertex):
        return self.b10.get(vertex, [])
b11 = class1()
b11.fonk3(1)
b11.fonk3(2)
b11.fonk3(3)
b11.fonk4(1, 2, 5)
b11.fonk4(1, 3, 9)
b11.fonk4(2, 3, 2)
a2 = 1
a3 = 3
shortest_path, b12 = fonk1(b11, a2, a3)
print("Shortest Path:", shortest_path)
print("Weight of Shortest Path:", b12)