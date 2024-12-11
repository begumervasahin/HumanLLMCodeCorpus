import heapq
def fonk1(v, path):
    if v.previous:
        path.append(v.previous.getId())
        fonk1(v.previous, path)
def fonk2(graph, start):
    start.setDistance(0)
    b1 = [(vertex.getDistance(), vertex) for vertex in graph]
    heapq.heapify(b1)
    while len(b1):
        b2 = heapq.heappop(b1)
        b3 = b2[1]
        b3.setVisited()
        for next_vertex in b3.adjacent:
            if next_vertex.visited:
                continue
            b4 = b3.getDistance() + b3.getWeight(next_vertex)
            if b4 < next_vertex.getDistance():
                next_vertex.setDistance(b4)
                next_vertex.setPrevious(b3)
        while len(b1):
            heapq.heappop(b1)
        b1 = [(vertex.getDistance(), vertex) for vertex in graph if not vertex.visited]
        heapq.heapify(b1)