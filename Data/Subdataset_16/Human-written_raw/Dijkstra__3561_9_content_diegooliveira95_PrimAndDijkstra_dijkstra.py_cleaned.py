from graph import Vertex as Vertex
from graph import Graph as Graph
import heapq
def fonk1(v, path):
    if v.previous:
        path.append(v.previous.getId())
        fonk1(v.previous, path)
    return
def fonk2(aGraph, start):
    start.setDistance(0)
    b1 = [(vertex.getDistance(),vertex) for vertex in aGraph]
    heapq.heapify(b1)
    while len(b1):
        b2 = heapq.heappop(b1)
        b3 = b2[1]
        b3.setVisited()
        for next in b3.adjacent:
            if next.visited:
                continue
            b4 = b3.getDistance() + b3.getWeight(next)
            if b4 < next.getDistance():
                next.setDistance(b4)
                next.setPrevious(b3)
        while len(b1):
            heapq.heappop(b1)
        b1 = [(vertex.getDistance(),vertex) for vertex in aGraph if not vertex.visited]
        heapq.heapify(b1)