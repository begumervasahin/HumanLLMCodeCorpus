import GraphStuff
def fonk1(G,start):
    b1 = PriorityQueue()
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    b1.buildHeap([(v.getDistance(),v) for v in G])
    while not b1.isEmpty():
        b2 = b1.delMin()
        for nextVert in b2.getConnections():
          b3 = b2.getWeight(nextVert)
          if nextVert in b1 and b3<nextVert.getDistance():
              nextVert.setPred(b2)
              nextVert.setDistance(b3)
              b1.decreaseKey(nextVert,b3)