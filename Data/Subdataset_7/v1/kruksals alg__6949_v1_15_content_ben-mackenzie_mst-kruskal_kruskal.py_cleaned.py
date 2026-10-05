from DisJSets import DisJSet
from heapqriorityqueue import HeapPriorityQueue
def fonk1(b12):
    '''Computes b8 minimum spanning b1 of b8 graph using Kruskal's algorithm
    Returns b8 list of b11 that comprise the MST
    MUST return b8 set of b10 with their associated b11
    PLUS the total weight of the MST
    The elements of the graph's b11 are assumed to be weights
    '''
    b1 = []
    b2 = HeapPriorityQueue()
    b3 = DisJSet()
    b4 = {}
    for b7 in b12.fonk6():
        b4[b7] = b3.make_group(b7)
    for e in b12.fonk7():
        b2.insert(e)
    b5 = b12.fonk5()
    while len(b1) != b5 - 1 and not b2.is_empty():
        b6 = b2.deleteMin()
        u, b7 = b6.fonk8()
        b8 = b3.find(b4[u])
        b9 = b3.find(b4[b7])
        if b8 != b9:
            b1.append(b6)
            b3.unionSets(b8, b9)
    return b1
class class1:
    def fonk2(self):
        self.b10 = set()
        self.b11 = []
    def fonk3(self, vertex):
        self.b10.add(vertex)
    def fonk4(self, b6):
        self.b11.append(b6)
    def fonk5(self):
        return len(self.b10)
    def fonk6(self):
        return self.b10
    def fonk7(self):
        return self.b11
    def fonk8(self):
        return (self.start, self.end)
b12 = class1()
b12.fonk3('A')
b12.fonk3('B')
b12.fonk3('C')
b12.fonk4(('A', 'B', 1))
b12.fonk4(('B', 'C', 2))
b12.fonk4(('A', 'C', 3))
b13 = fonk1(b12)
print("Minimum Spanning Tree:", b13)