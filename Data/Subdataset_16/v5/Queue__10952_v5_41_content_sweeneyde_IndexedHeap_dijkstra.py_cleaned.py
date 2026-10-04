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
        while b5:
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
        b8 = []
        b6 = destination
        while b6 != source:
            b8.append(b6)
            b6 = b4[b6]
        b8.append(source)
        b8.reverse()
        return b3[destination], b8
if b9 = = "__main__":
    import doctest
    doctest.testmod()