from collections import defaultdict
from heapq import heappop, heappush
def dijkstra(edges, start, end):
    graph = defaultdict(list)
    for left, right, cost in edges:
        graph[left].append((cost, right))
    priority_queue = [(0, start, ())]
    visited = set()
    while priority_queue:
        cost, vertex, path = heappop(priority_queue)
        if vertex not in visited:
            visited.add(vertex)
            path = (vertex, path)
            if vertex == end:
                return (cost, path)
            for next_cost, next_vertex in graph.get(vertex, ()):
                if next_vertex not in visited:
                    heappush(priority_queue, (cost + next_cost, next_vertex, path))
    return float("inf")