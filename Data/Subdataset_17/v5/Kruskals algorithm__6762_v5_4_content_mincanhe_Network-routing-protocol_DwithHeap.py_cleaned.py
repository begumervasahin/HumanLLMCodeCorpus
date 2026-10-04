from collections import defaultdict
from heapq import heappop, heappush
def dijkstra(edges, start, target):
    graph = defaultdict(list)
    for from_node, to_node, cost in edges:
        graph[from_node].append((cost, to_node))
    priority_queue = [(0, start, ())]
    visited = set()
    while priority_queue:
        current_cost, current_node, path = heappop(priority_queue)
        if current_node not in visited:
            visited.add(current_node)
            path = (current_node, path)
            if current_node == target:
                return current_cost, path
            for neighbor_cost, neighbor in graph[current_node]:
                if neighbor not in visited:
                    heappush(priority_queue, (current_cost + neighbor_cost, neighbor, path))
    return float("inf"), None
def extract_path(path):
    result = []
    while path:
        node, path = path
        result.append(node)
    return result[::-1]
