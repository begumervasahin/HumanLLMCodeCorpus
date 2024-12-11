import queue
from collections import namedtuple
b1 = namedtuple('b1', ['vertex', 'weight'])
class class1:
    def fonk1(self, b2):
        self.b2 = b2
        self.b3 = [[] for _ in range(b2)]
    def fonk2(self, source, dest, weight):
        assert 0 <= source < self.b2
        assert 0 <= dest < self.b2
        self.b3[source].append(b1(dest, weight))
        self.b3[dest].append(b1(source, weight))
    def fonk3(self, vertex):
        for edge in self.b3[vertex]:
            yield edge
def fonk4(graph, source, dest):
    b4 = queue.PriorityQueue()
    b5 = [None] * graph.b2
    b6 = [float('inf')] * graph.b2
    b6[source] = 0
    b4.put((0, source))
    while not b4.empty():
        curr_distance, b7 = b4.get()
        if curr_distance > b6[b7]:
            continue
        for edge in graph.fonk3(b7):
            neighbor_vertex, b8 = edge
            b9 = b6[b7] + b8
            if b9 < b6[neighbor_vertex]:
                b6[neighbor_vertex] = b9
                b5[neighbor_vertex] = b7
                b4.put((b9, neighbor_vertex))
    b10 = []
    b11 = dest
    while b11 is not None:
        b10.append(b11)
        b11 = b5[b11]
    b10.reverse()
    return b10, b6[dest]
b12 = class1(9)
b12.fonk2(0, 1, 4)
b12.fonk2(1, 7, 6)
b12.fonk2(1, 2, 1)
b12.fonk2(2, 3, 3)
b12.fonk2(3, 7, 1)
b12.fonk2(3, 4, 2)
b12.fonk2(3, 5, 1)
b12.fonk2(4, 5, 1)
b12.fonk2(5, 6, 1)
b12.fonk2(6, 7, 2)
b12.fonk2(6, 8, 2)
b12.fonk2(7, 8, 2)
b10, b13 = fonk4(b12, 0, 4)
print("Shortest path:", b10)
print("Distance:", b13)