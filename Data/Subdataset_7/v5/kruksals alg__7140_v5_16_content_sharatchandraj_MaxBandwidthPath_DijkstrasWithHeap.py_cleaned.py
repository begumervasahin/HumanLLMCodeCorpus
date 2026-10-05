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
        if destination in b2 and b2[destination] == 'intree':
            break
        b5 = MaxHeap.Max()
        b2[b5] = 'intree'
        MaxHeap.Delete(b5)
        for e in graph.get_edge(b5):
            if b2[e.vertex] == 'unseen':
                fonk2(e, b5, source, destination, b4)
            elif b2[e.vertex] == 'fringe':
                fonk3(e, b5, source, destination, b4)
    b6 = fonk4(destination, b4)
    return b6, b3[destination]
def fonk2(e, b5, source, destination, b4):
    b2[e.vertex] = 'fringe'
    b4[e.vertex] = b5
    b3[e.vertex] = min(b3[b5], e.weight)
    MaxHeap.Insert(e.vertex, b3[e.vertex])
def fonk3(e, b5, source, destination, b4):
    if b3[e.vertex] < min(b3[b5], e.weight):
        b4[e.vertex] = b5
        MaxHeap.Delete(e.vertex)
        b3[e.vertex] = min(b3[b5], e.weight)
        MaxHeap.Insert(e.vertex, b3[e.vertex])
def fonk4(destination, b4):
    b6 = []
    b7 = destination
    while b7 is not None:
        b6.append(b7)
        b7 = b4[b7]
    b6.reverse()
    return b6