from DisJSets import DisJSet
from heapqriorityqueue import HeapPriorityQueue
def fonk1(graph):
    b1 = []
    b2 = HeapPriorityQueue()
    b3 = DisJSet()
    b4 = {}
    for vertex in graph.vertices():
        b4[vertex] = b3.make_group(vertex)
    for b6 in graph.edges():
        b2.insert(b6)
    b5 = graph.vertex_count()
    while len(b1) != b5 - 1 and not b2.is_empty():
        b6 = b2.deleteMin()
        u, b7 = b6.endpoints()
        b8 = b3.find(b4[u])
        b9 = b3.find(b4[b7])
        if b8 != b9:
            b1.append(b6)
            b3.unionSets(b8, b9)
    return b1