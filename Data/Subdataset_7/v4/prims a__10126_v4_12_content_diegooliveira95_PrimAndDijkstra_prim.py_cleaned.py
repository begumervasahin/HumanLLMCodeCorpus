from graph import Vertex
from graph import Graph
from pythonds.graphs import PriorityQueue
import sys
def fonk1(aGraph, start):
    b1 = PriorityQueue()
    for vertex in aGraph:
        vertex.setDistance(sys.maxsize)
        vertex.setPrevious(None)
    start.setDistance(0)
    b1.buildHeap([(vertex.getDistance(), vertex) for vertex in aGraph])
    while not b1.isEmpty():
        b2 = b1.delMin()
        for nextVertex in b2.getConnections():
            b3 = b2.getWeight(nextVertex)
            if nextVertex in b1 and b3 < nextVertex.getDistance():
                nextVertex.setPrevious(b2)
                nextVertex.setDistance(b3)
                b1.decreaseKey(nextVertex, b3)