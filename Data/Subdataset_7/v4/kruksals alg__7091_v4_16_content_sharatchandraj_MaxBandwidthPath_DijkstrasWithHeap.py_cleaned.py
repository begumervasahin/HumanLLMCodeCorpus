from collections import namedtuple
import MaxHeap
a1 = 5000
b1 = namedtuple('b1', ['vertex', 'weight'])
b2 = [None] * a1
b3 = [None] * a1
def fonk1(graph, source, destination):
    MaxHeap.initialize()
    b4 = [None] * a1
    for i in graph.get_vertex():
        b2[i] = 'unseen'
    b2[source] = 'intree'
    for i in graph.get_edge(source):
        b2[i.vertex] = 'fringe'
        b3[i.vertex] = i.weight
        MaxHeap.Insert(i.vertex, i.weight)
        b4[i.vertex] = source
    while 'fringe' in b2:
        b5 = False
        b6 = MaxHeap.Max()
        if b6 = = destination:
            break
        b2[b6] = 'intree'
        MaxHeap.Delete(b6)
        for e in graph.get_edge(b6):
            if b2[e.vertex] == 'unseen':
                b2[e.vertex] = 'fringe'
                b4[e.vertex] = b6
                b3[e.vertex] = min(b3[b6], e.weight)
                MaxHeap.Insert(e.vertex, b3[e.vertex])
            elif b2[e.vertex] == 'fringe' and b3[e.vertex] < min(b3[b6], e.weight):
                b4[e.vertex] = b6
                MaxHeap.Delete(e.vertex)
                b3[e.vertex] = min(b3[b6], e.weight)
                MaxHeap.Insert(e.vertex, b3[e.vertex])
    b7 = []
    b8 = destination
    while b8 is not None:
        b7.append(b8)
        b8 = b4[b8]
    b7.reverse()
    return b7, b3[destination]