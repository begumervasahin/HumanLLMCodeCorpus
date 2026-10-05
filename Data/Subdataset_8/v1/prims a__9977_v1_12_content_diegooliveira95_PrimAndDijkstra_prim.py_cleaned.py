
from graph import Vertex as Vertex
from graph import Graph as Graph
from pythonds.graphs import PriorityQueue
import sys
def prim(aGraph, start):
    pq = PriorityQueue()
    for vertex in aGraph:
        vertex.setDistance(sys.maxsize)
        vertex.setPrevious(None)
    start.setDistance(0)
    pq.buildHeap([(vertex.getDistance(), vertex) for vertex in aGraph])
    while not pq.isEmpty():
        currentVertex = pq.delMin()
        for nextVertex in currentVertex.getConnections():
            newCost = currentVertex.getWeight(nextVertex)
            if nextVertex in pq and newCost < nextVertex.getDistance():
                nextVertex.setPrevious(currentVertex)
                nextVertex.setDistance(newCost)
                pq.decreaseKey(nextVertex, newCost)
if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)
    prim(g, g.getVertex(0))
    for v in g:
        if v.getPrevious():
            print("(%s, %s) -> %s" % (v.getPrevious().getId(), v.getId(), v.getDistance()))