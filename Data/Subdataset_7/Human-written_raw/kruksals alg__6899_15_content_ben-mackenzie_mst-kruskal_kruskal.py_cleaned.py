'''
Created on Apr 2, 2018
@author: benjaminmackenzie
'''
from DisJSets import DisJSet
from heapqriorityqueue import HeapPriorityQueue
def fonk1(g):
    '''Computes b8 minimum spanning b1 of b8 graph using Kruskal's algorithm
    Returns b8 list of edges that comprise the MST
    MUST return b8 set of vertices with their associated edges
    PLUS the total weight of the MST
    The elements of the graph's edges are assumed to be weights
    '''
    b1 = []
    b2 = HeapPriorityQueue()
    b3 = DisJSet()
    b4 = {}
    for b7 in g.vertices():
        b4[b7] = b3.make_group(b7)
    for e in g.edges():
        b2.insert(e)
    b5 = g.vertex_count()
    while len(b1) != b5 - 1 and not b2.is_empty():
        b6 = b2.deleteMin()
        u,b7 = b6.endpoints()
        b8 = b3.find(b4[u])
        b9 = b3.find(b4[b7])
        if b8 != b9:
            b1.append(b6)
            b3.unionSets(b8,b9)
    return b1