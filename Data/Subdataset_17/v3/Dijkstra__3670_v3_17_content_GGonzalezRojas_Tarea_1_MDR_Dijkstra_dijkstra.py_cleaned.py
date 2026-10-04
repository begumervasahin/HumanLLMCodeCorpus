from collections import defaultdict
from heapq import heappop, heappush
def dijkstra(edges, start, end):
    graph = defaultdict(list)
    for src, dest, cost in edges:
        graph[src].append((cost, dest))
    priority_queue = [(0, start, ())]
    seen = set()
    while priority_queue:
        cost, vertex, path = heappop(priority_queue)
        if vertex not in seen:
            seen.add(vertex)
            path = (vertex, path)
            if vertex == end:
                return cost, path
            for cost_to_neighbor, neighbor in graph[vertex]:
                if neighbor not in seen:
                    heappush(priority_queue, (cost + cost_to_neighbor, neighbor, path))
    return float("inf"), ()
def print_result(result):
    cost, path = result
    node_list = []
    while path:
        node, path = path
        node_list.append(node)
    print(f"Cost: {cost}")
    print("Path:", " -> ".join(reversed(node_list)))
if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11),
        ("G", "H", 5)
    ]
    print("=== Dijkstra ===")
    paths_to_check = [("A", "H"), ("A", "D"), ("D", "F"), ("F", "G"), ("G", "H"), ("F", "G")]
    for start_node, end_node in paths_to_check:
        print(f"{start_node} -> {end_node}:")
        print_result(dijkstra(edges, start_node, end_node))