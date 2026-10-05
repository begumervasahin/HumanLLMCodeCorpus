import heapq
def shortest_path(v, path):
    if v.previous:
        path.append(v.previous.getId())
        shortest_path(v.previous, path)
def dijkstra(graph, start):
    start.setDistance(0)
    unvisited_queue = [(vertex.getDistance(), vertex) for vertex in graph]
    heapq.heapify(unvisited_queue)
    while unvisited_queue:
        distance, current = heapq.heappop(unvisited_queue)
        current.setVisited()
        for next_vertex in current.adjacent:
            if next_vertex.visited:
                continue
            new_distance = current.getDistance() + current.getWeight(next_vertex)
            if new_distance < next_vertex.getDistance():
                next_vertex.setDistance(new_distance)
                next_vertex.setPrevious(current)
        unvisited_queue.clear()
        unvisited_queue.extend([(vertex.getDistance(), vertex) for vertex in graph if not vertex.visited])
        heapq.heapify(unvisited_queue)