from collections import namedtuple
import MaxHeap
a1 = 5000
b1 = namedtuple('b1', ['vertex', 'weight'])
def fonk1():
    b2 = ['unseen'] * a1
    b3 = [float('-inf')] * a1
    return b2, b3
def fonk2(source, graph, b2, b3, b4):
    for edge in graph.get_edge(source):
        b2[edge.vertex] = 'fringe'
        b3[edge.vertex] = edge.weight
        MaxHeap.Insert(edge.vertex, edge.weight)
        b4[edge.vertex] = source
def fonk3(graph, source, destination):
    MaxHeap.initialize()
    b4 = [None] * a1
    b2, b3 = fonk1()
    b2[source] = 'intree'
    fonk2(source, graph, b2, b3, b4)
    while 'fringe' in b2:
        b5 = MaxHeap.Max()
        if b5 = = destination:
            break
        b2[b5] = 'intree'
        MaxHeap.Delete(b5)
        for edge in graph.get_edge(b5):
            if b2[edge.vertex] == 'unseen':
                b2[edge.vertex] = 'fringe'
                b4[edge.vertex] = b5
                b3[edge.vertex] = min(b3[b5], edge.weight)
                MaxHeap.Insert(edge.vertex, b3[edge.vertex])
            elif b2[edge.vertex] == 'fringe' and b3[edge.vertex] < min(b3[b5], edge.weight):
                b4[edge.vertex] = b5
                MaxHeap.Delete(edge.vertex)
                b3[edge.vertex] = min(b3[b5], edge.weight)
                MaxHeap.Insert(edge.vertex, b3[edge.vertex])
    return fonk4(b4, destination), b3[destination]
def fonk4(b4, destination):
    b6 = []
    b7 = destination
    while b7 is not None:
        b6.append(b7)
        b7 = b4[b7]
    b6.reverse()
    return b6