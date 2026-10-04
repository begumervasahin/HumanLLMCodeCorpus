from collections import defaultdict
from heapq import heappush, heappop
def dijkstra(edges, start, target):
    graph = defaultdict(list)
    for left, right, cost in edges:
        graph[left].append((cost, right))
    queue = [(0, start, ())]
    seen = set()
    while queue:
        (cost, current_vertex, path) = heappop(queue)
        if current_vertex not in seen:
            seen.add(current_vertex)
            path = (current_vertex, path)
            if current_vertex == target:
                return (cost, path)
            for neighbor_cost, neighbor in graph.get(current_vertex, ()):
                if neighbor not in seen:
                    heappush(queue, (cost + neighbor_cost, neighbor, path))
    return float("inf")
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
    print("Shortest path from {} to {}:".format(start_node, target_node))
    print("Cost:", cost)
    print("Path:", extract_path(path))