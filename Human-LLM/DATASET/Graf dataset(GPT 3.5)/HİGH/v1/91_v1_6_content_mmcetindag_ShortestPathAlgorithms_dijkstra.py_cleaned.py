import queue
from collections import namedtuple
b1 = namedtuple('b1', ['vertex', 'b8'])
class class1(object):
    def fonk1(self, b2):
        self.b2 = b2
        self.b3 = [[] for _ in range(b2)]
    def fonk2(self, b9, dest, b8):
        assert b9 < self.b2
        assert dest < self.b2
        self.b3[b9].append(b1(dest, b8))
        self.b3[dest].append(b1(b9, b8))
    def fonk3(self, vertex):
        for e in self.b3[vertex]:
            yield e
    def fonk4(self):
        for b11 in range(self.b2):
            yield b11
def fonk5(graph, b9, dest):
    b4 = queue.PriorityQueue()
    b5 = []
    b6 = []
    b7 = float("inf")
    for i in graph.fonk4():
        b8 = b7
        if b9 = = i:
            b8 = 0
        b6.append(b8)
        b5.append(None)
    b4.put(([0, b9]))
    while not b4.empty():
        b10 = b4.get()
        b11 = b10[1]
        for e in graph.fonk3(b11):
            b12 = b6[b11] + e.b8
            if b6[e.vertex] > b12:
                b6[e.vertex] = b12
                b5[e.vertex] = b11
                if b12 < -1000:
                    raise Exception("Negative cycle detected")
                b4.put(([b6[e.vertex], e.vertex]))
    b13 = []
    b14 = dest
    while b14 is not None:
        b13.append(b14)
        b14 = b5[b14]
    b13.reverse()
    return b13, b6[dest]
b15 = class1(9)
b15.fonk2(0, 1, 4)
b15.fonk2(1, 7, 6)
b15.fonk2(1, 2, 1)
b15.fonk2(2, 3, 3)
b15.fonk2(3, 7, 1)
b15.fonk2(3, 4, 2)
b15.fonk2(3, 5, 1)
b15.fonk2(4, 5, 1)
b15.fonk2(5, 6, 1)
b15.fonk2(6, 7, 2)
b15.fonk2(6, 8, 2)
b15.fonk2(7, 8, 2)
b13, b16 = fonk5(b15, 0, 4)
print("Shortest path:", b13)
print("Distance:", b16)