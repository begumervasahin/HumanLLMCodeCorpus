from DisJSets import DisJSet
from heapqriorityqueue import HeapPriorityQueue
def fonk1(graph):
    '''Computes a minimum spanning tree of a graph using Kruskal's algorithm
    Returns a list of edges that comprise the MST
    MUST return a set of vertices with their associated edges
    PLUS the total weight of the MST
    The elements of the graph's edges are assumed to be weights
    '''
    b1 = []
    b2 = HeapPriorityQueue()
    b3 = DisJSet()
    b4 = {}
    for vertex in graph.fonk6():
        b4[vertex] = b3.make_group(vertex)
    for b5 in graph.fonk7():
        b2.insert(b5)
    while len(b1) != graph.fonk5() - 1 and not b2.is_empty():
        b5 = b2.deleteMin()
        u, b6 = b5.fonk8()
        b7 = b3.find(b4[u])
        b8 = b3.find(b4[b6])
        if b7 != b8:
            b1.append(b5)
            b3.union_sets(b7, b8)
    return b1
class class1:
    def fonk2(self):
        self.b9 = set()
        self.b10 = []
    def fonk3(self, vertex):
        self.b9.add(vertex)
    def fonk4(self, b5):
        self.b10.append(b5)
    def fonk5(self):
        return len(self.b9)
    def fonk6(self):
        return self.b9
    def fonk7(self):
        return self.b10
    def fonk8(self):
        return (self.start, self.end)
b11 = class1()
b11.fonk3('A')
b11.fonk3('B')
b11.fonk3('C')
b11.fonk4(('A', 'B', 1))
b11.fonk4(('B', 'C', 2))
b11.fonk4(('A', 'C', 3))
b12 = fonk1(b11)
print("Minimum Spanning Tree:", b12)