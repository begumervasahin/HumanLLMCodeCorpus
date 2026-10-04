from collections import namedtuple
from typing import List, Tuple
b1 = namedtuple('b1', ['vertex', 'weight'])
def fonk1(b5: List[str], b6: List[float]) -> int:
    a1 = 0
    b2 = None
    for i, (b3, wt) in enumerate(zip(b5, b6)):
        if b3 = = 'fringe' and wt > a1:
            a1 = wt
            b2 = i
    return b2
def fonk2(graph, source: int, destination: int) -> Tuple[List[int], float]:
    b4 = len(graph.get_vertex())
    b5 = ['unseen'] * b4
    b6 = [0] * b4
    b7 = [None] * b4
    b5[source] = 'intree'
    for edge in graph.get_edge(source):
        b5[edge.vertex] = 'fringe'
        b6[edge.vertex] = edge.weight
        b7[edge.vertex] = source
    while 'fringe' in b5:
        b8 = fonk1(b5, b6)
        if b8 is None:
            break
        b5[b8] = 'intree'
        for edge in graph.get_edge(b8):
            if b5[edge.vertex] == 'unseen':
                b5[edge.vertex] = 'fringe'
                b7[edge.vertex] = b8
                b6[edge.vertex] = min(b6[b8], edge.weight)
            elif b5[edge.vertex] == 'fringe' and b6[edge.vertex] < min(b6[b8], edge.weight):
                b7[edge.vertex] = b8
                b6[edge.vertex] = min(b6[b8], edge.weight)
    b9 = []
    b10 = destination
    while b10 is not None:
        b9.append(b10)
        b10 = b7[b10]
    b9.reverse()
    return b9, b6[destination]