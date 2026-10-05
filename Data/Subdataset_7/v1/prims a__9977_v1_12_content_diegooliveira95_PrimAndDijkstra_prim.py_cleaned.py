
from graph import Vertex as Vertex
from graph import Graph as Graph
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
if b4 = = "__main__":
    b5 = Graph()
    for i in range(6):
        b5.addVertex(i)
    b5.addEdge(0, 1, 5)
    b5.addEdge(0, 5, 2)
    b5.addEdge(1, 2, 4)
    b5.addEdge(2, 3, 9)
    b5.addEdge(3, 4, 7)
    b5.addEdge(3, 5, 3)
    b5.addEdge(4, 0, 1)
    b5.addEdge(5, 4, 8)
    b5.addEdge(5, 2, 1)
    fonk1(b5, b5.getVertex(0))
    for v in b5:
        if v.getPrevious():
            print("(%s, %s) -> %s" % (v.getPrevious().getId(), v.getId(), v.getDistance()))