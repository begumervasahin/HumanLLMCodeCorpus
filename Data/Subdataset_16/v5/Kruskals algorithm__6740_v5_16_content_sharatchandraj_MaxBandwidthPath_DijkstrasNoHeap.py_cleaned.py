from collections import namedtuple
from typing import List, Tuple, Optional
b1 = namedtuple('b1', ['vertex', 'weight'])
def fonk1(b6: List[str], b7: List[float]) -> Optional[int]:
    b2 = None
    b3 = float('-inf')
    for i, (b4, wt) in enumerate(zip(b6, b7)):
        if b4 = = 'fringe' and wt > b3:
            b3 = wt
            b2 = i
    return b2
def fonk2(graph, source: int, destination: int) -> Tuple[List[int], float]:
    b5 = len(graph.get_vertex())
    b6 = ['unseen'] * b5
    b7 = [float('-inf')] * b5
    b8 = [None] * b5
    b6[source] = 'intree'
    b7[source] = float('inf')
    for edge in graph.get_edge(source):
        b6[edge.vertex] = 'fringe'
        b7[edge.vertex] = edge.weight
        b8[edge.vertex] = source
    while 'fringe' in b6:
        b9 = fonk1(b6, b7)
        if b9 is None:
            break
        b6[b9] = 'intree'
        for edge in graph.get_edge(b9):
            if b6[edge.vertex] == 'unseen':
                b6[edge.vertex] = 'fringe'
                b8[edge.vertex] = b9
                b7[edge.vertex] = min(b7[b9], edge.weight)
            elif b6[edge.vertex] == 'fringe' and b7[edge.vertex] < min(b7[b9], edge.weight):
                b8[edge.vertex] = b9
                b7[edge.vertex] = min(b7[b9], edge.weight)
    b10 = []
    b11 = destination
    while b11 is not None:
        b10.append(b11)
        b11 = b8[b11]
    b10.reverse()
    return b10, b7[destination]