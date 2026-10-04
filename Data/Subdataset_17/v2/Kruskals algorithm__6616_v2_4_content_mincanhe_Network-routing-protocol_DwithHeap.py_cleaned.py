from collections import defaultdict
from heapq import heappush, heappop
def dijkstra(edges, start, target):
    graph = defaultdict(list)
    for from_node, to_node, cost in edges:
        graph[from_node].append((cost, to_node))
    priority_queue = [(0, start, ())]
    visited = set()
    while priority_queue:
        current_cost, current_vertex, path = heappop(priority_queue)
        if current_vertex not in visited:
            visited.add(current_vertex)
            path = (current_vertex, path)
            if current_vertex == target:
                return current_cost, path
            for neighbor_cost, neighbor in graph.get(current_vertex, ()):
                if neighbor not in visited:
                    heappush(priority_queue, (current_cost + neighbor_cost, neighbor, path))
    return float("inf"), ()
def extract_path(path_tuple):
    path = []
    while path_tuple:
        path.append(path_tuple[0])
        path_tuple = path_tuple[1]
    return path[::-1]
if __name__ == "__main__":
    edges = [
        ('A', 'B', 1),
        ('A', 'C', 4),
        ('B', 'C', 2),
        ('B', 'D', 5),
        ('C', 'D', 1),
        ('D', 'E', 3),
    ]
    start_node = 'A'
    target_node = 'E'
    cost, path = dijkstra(edges, start_node, target_node)
    print(f"Shortest path from {start_node} to {target_node}:")
    print(f"Cost: {cost}")
    print(f"Path: {extract_path(path)}")