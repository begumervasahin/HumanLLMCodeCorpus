import queue
from collections import namedtuple
b1 = namedtuple('b1', ['vertex', 'weight'])
class class1(object):
    def fonk1(self, b2):
        self.b2 = b2
        self.b3 = [[] for _ in range(b2)]
    def fonk2(self, source, dest, weight):
        assert source < self.b2 and dest < self.b2
        self.b3[source].append(b1(dest, weight))
        self.b3[dest].append(b1(source, weight))
    def fonk3(self, vertex):
        return iter(self.b3[vertex])
def fonk4(b11, source, dest):
    b4 = queue.PriorityQueue()
    b5 = [None] * b11.b2
    b6 = [float('inf')] * b11.b2
    b6[source] = 0
    b4.put((0, source))
    while not b4.empty():
        curr_distance, b7 = b4.get()
        if curr_distance > b6[b7]:
            continue
        for edge in b11.fonk3(b7):
            neighbor_vertex, b8 = edge
            b9 = b6[b7] + b8
            if b9 < b6[neighbor_vertex]:
                b6[neighbor_vertex] = b9
                b5[neighbor_vertex] = b7
                b4.put((b9, neighbor_vertex))
    b10 = []
    b7 = dest
    while b7 is not None:
        b10.append(b7)
        b7 = b5[b7]
    b10.reverse()
    return b10, b6[dest]
b11 = class1(9)
b11.fonk2(0, 1, 4)
b11.fonk2(1, 7, 6)
b11.fonk2(1, 2, 1)
b11.fonk2(2, 3, 3)
b11.fonk2(3, 7, 1)
b11.fonk2(3, 4, 2)
b11.fonk2(3, 5, 1)
b11.fonk2(4, 5, 1)
b11.fonk2(5, 6, 1)
b11.fonk2(6, 7, 2)
b11.fonk2(6, 8, 2)
b11.fonk2(7, 8, 2)
b10, b12 = fonk4(b11, 0, 4)
print("Shortest path:", b10)
print("Distance:", b12)