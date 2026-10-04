from collections import defaultdict
from math import inf
from indexedheap import IndexedHeap
class class1:
    def fonk1(self):
        self.b1 = set()
        self.b2 = defaultdict(list)
    def fonk2(self, source, destination, weight):
        if weight < 0:
            raise ValueError("Edge weights cannot be negative.")
        self.b1.update([source, destination])
        self.b2[source].append((destination, weight))
    def fonk3(self, source, destination):
        if source not in self.b1 or destination not in self.b1:
            return inf, None
        b3 = {vertex: inf for vertex in self.b1}
        b3[source] = 0
        b4 = {}
        b5 = IndexedHeap((b3[vertex], vertex) for vertex in self.b1)
        while not b5.is_empty():
            current_distance, b6 = b5.pop()
            if b6 = = destination:
                break
            for neighbor, weight in self.b2[b6]:
                b7 = current_distance + weight
                if b7 < b3[neighbor]:
                    b3[neighbor] = b7
                    b4[neighbor] = b6
                    b5.change_weight(neighbor, b7)
        if b3[destination] == inf:
            return inf, None
        b8 = self.fonk4(b4, source, destination)
        return b3[destination], b8
    def fonk4(self, b4, source, destination):
        b8 = []
        b9 = destination
        while b9 != source:
            b8.append(b9)
            b9 = b4.get(b9)
            if b9 is None:
                return None
        b8.append(source)
        b8.reverse()
        return b8
if b10 = = "__main__":
    import doctest
    doctest.testmod()