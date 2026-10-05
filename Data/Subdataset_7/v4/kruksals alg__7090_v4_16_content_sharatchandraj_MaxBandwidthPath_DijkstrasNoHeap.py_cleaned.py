from collections import namedtuple
import time
import GraphGeneration
b1 = namedtuple('b1', ['vertex', 'weight'])
a1 = 5000
b2 = [None] * a1
b3 = [None] * a1
def fonk1():
    a2 = 0
    b4 = None
    for i in range(len(b2)):
        if b2[i] == 'fringe' and b3[i] > a2:
            a2 = b3[i]
            b4 = i
    return b4
def fonk2(graph, source, destination):
    b5 = [None] * a1
    for i in graph.get_vertex():
        b2[i] = 'unseen'
    b2[source] = 'intree'
    for i in graph.get_edge(source):
        b2[i.vertex] = 'fringe'
        b3[i.vertex] = i.weight
        b5[i.vertex] = source
    while 'fringe' in b2:
        b6 = fonk1()
        b2[b6] = 'intree'
        for e in graph.get_edge(b6):
            if b2[e.vertex] == 'unseen':
                b2[e.vertex] = 'fringe'
                b5[e.vertex] = b6
                b3[e.vertex] = b3[b6] if b3[b6] < e.weight else e.weight
            elif b2[e.vertex] == 'fringe' and b3[e.vertex] < min(b3[b6], e.weight):
                b5[e.vertex] = b6
                b3[e.vertex] = b3[b6] if b3[b6] < e.weight else e.weight
    b7 = []
    b8 = destination
    while b8 is not None:
        b7.append(b8)
        b8 = b5[b8]
    b7.reverse()
    return b7, b3[destination]