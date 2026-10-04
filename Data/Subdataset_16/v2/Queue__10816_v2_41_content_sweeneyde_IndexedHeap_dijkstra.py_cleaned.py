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
        self.b1.update({source, destination})
        self.b2[source].append((destination, weight))
    def fonk3(self, source, destination):
        if not {source, destination} <= self.b1:
            return inf, None
        b3 = {v: inf for v in self.b1}
        b3[source] = 0
        b4 = {}
        b5 = IndexedHeap((b3[v], v) for v in self.b1)
        while b5.peek() != destination:
            b6 = b5.pop()
            b7 = b3[b6]
            for neighbor, edge_weight in self.b2[b6]:
                b8 = b7 + edge_weight
                if b8 < b3[neighbor]:
                    b3[neighbor] = b8
                    b4[neighbor] = b6
                    b5.change_weight(neighbor, b8)
        if b3[destination] == inf:
            return inf, None
        b9 = []
        b10 = destination
        while b10 != source:
            b9.append(b10)
            b10 = b4.get(b10)
            if b10 is None:
                return inf, None
        b9.append(source)
        b9.reverse()
        return b3[destination], b9
if b11 = = "__main__":
    import doctest
    doctest.testmod()