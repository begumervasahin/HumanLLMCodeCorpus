from collections import defaultdict
from heapq import heappop, heappush
def dijkstra(graph, start, end):
    adjacency_list = defaultdict(list)
    for node, next_node, weight in graph:
        adjacency_list[node].append((weight, next_node))
    priority_queue = [(0, start, ())]
    visited = set()
    while priority_queue:
        current_cost, current_node, path = heappop(priority_queue)
        if current_node not in visited:
            visited.add(current_node)
            path = (current_node, path)
            if current_node == end:
                return current_cost, path
            for weight, neighbor in adjacency_list[current_node]:
                if neighbor not in visited:
                    heappush(priority_queue, (current_cost + weight, neighbor, path))
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
    graph = [
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
    result = dijkstra(graph, "A", "H")
    print("Shortest path from A to H:")
    print_result(result)