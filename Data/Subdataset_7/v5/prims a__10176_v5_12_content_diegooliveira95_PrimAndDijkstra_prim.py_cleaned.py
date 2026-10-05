from graph import Vertex
from graph import Graph
from pythonds.graphs import PriorityQueue
import sys
def fonk1(graph, start_vertex):
    b1 = PriorityQueue()
    for vertex in graph:
        vertex.setDistance(sys.maxsize)
        vertex.setPrevious(None)
    start_vertex.setDistance(0)
    b1.buildHeap([(vertex.getDistance(), vertex) for vertex in graph])
    while not b1.isEmpty():
        b2 = b1.delMin()
        for next_vertex in b2.getConnections():
            b3 = b2.getWeight(next_vertex)
            if next_vertex in b1 and b3 < next_vertex.getDistance():
                next_vertex.setPrevious(b2)
                next_vertex.setDistance(b3)
                b1.decreaseKey(next_vertex, b3)