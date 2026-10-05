import sys
from GraphStuff import PriorityQueue
def prim(G, start):
    pq = PriorityQueue()
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in G])
    while not pq.isEmpty():
        current_vert = pq.delMin()
        for next_vert in current_vert.getConnections():
            new_cost = current_vert.getWeight(next_vert)
            if next_vert in pq and new_cost < next_vert.getDistance():
                next_vert.setPred(current_vert)
                next_vert.setDistance(new_cost)
                pq.decreaseKey(next_vert, new_cost)