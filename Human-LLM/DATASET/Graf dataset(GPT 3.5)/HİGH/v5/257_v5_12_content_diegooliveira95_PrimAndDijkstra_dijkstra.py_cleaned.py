import heapq
def fonk1(v, path):
    if v.previous:
        path.append(v.previous.getId())
        fonk1(v.previous, path)
def fonk2(graph, start):
    start.setDistance(0)
    b1 = [(vertex.getDistance(), vertex) for vertex in graph]
    heapq.heapify(b1)
    while b1:
        distance, b2 = heapq.heappop(b1)
        b2.setVisited()
        for next_vertex in b2.adjacent:
            if next_vertex.visited:
                continue
            b3 = b2.getDistance() + b2.getWeight(next_vertex)
            if b3 < next_vertex.getDistance():
                next_vertex.setDistance(b3)
                next_vertex.setPrevious(b2)
        b1.clear()
        b1.extend([(vertex.getDistance(), vertex) for vertex in graph if not vertex.visited])
        heapq.heapify(b1)