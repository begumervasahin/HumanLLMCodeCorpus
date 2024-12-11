import sys
from GraphStuff import PriorityQueue
def fonk1(G, start):
    b1 = PriorityQueue()
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    b1.buildHeap([(v.getDistance(), v) for v in G])
    while not b1.isEmpty():
        b2 = b1.delMin()
        for next_vert in b2.getConnections():
            b3 = b2.getWeight(next_vert)
            if next_vert in b1 and b3 < next_vert.getDistance():
                next_vert.setPred(b2)
                next_vert.setDistance(b3)
                b1.decreaseKey(next_vert, b3)