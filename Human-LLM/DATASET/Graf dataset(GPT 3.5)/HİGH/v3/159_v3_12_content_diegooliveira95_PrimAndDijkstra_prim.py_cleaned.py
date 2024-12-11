
from graph import Vertex, Graph
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
        for neighbor_vertex in b2.getConnections():
            b3 = b2.getWeight(neighbor_vertex)
            if neighbor_vertex in b1 and b3 < neighbor_vertex.getDistance():
                neighbor_vertex.setPrevious(b2)
                neighbor_vertex.setDistance(b3)
                b1.decreaseKey(neighbor_vertex, b3)
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
    for vertex in b5:
        b6 = vertex.getPrevious()
        if b6:
            print("(%s, %s) -> %s" % (b6.getId(), vertex.getId(), vertex.getDistance()))