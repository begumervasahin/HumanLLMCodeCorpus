import heapq
def shortest(v, path):
    if v.previous:
        path.append(v.previous.getId())
        shortest(v.previous, path)
def dijkstra(graph, start):
    start.setDistance(0)
    unvisitedQueue = [(vertex.getDistance(), vertex) for vertex in graph]
    heapq.heapify(unvisitedQueue)
    while len(unvisitedQueue):
        aVertex = heapq.heappop(unvisitedQueue)
        current = aVertex[1]
        current.setVisited()
        for next_vertex in current.adjacent:
            if next_vertex.visited:
                continue
            newDistance = current.getDistance() + current.getWeight(next_vertex)
            if newDistance < next_vertex.getDistance():
                next_vertex.setDistance(newDistance)
                next_vertex.setPrevious(current)
        while len(unvisitedQueue):
            heapq.heappop(unvisitedQueue)
        unvisitedQueue = [(vertex.getDistance(), vertex) for vertex in graph if not vertex.visited]
        heapq.heapify(unvisitedQueue)