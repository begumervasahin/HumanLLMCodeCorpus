from collections import defaultdict
from heapq import heappop, heappush
def dijkstra(graph, start, end):
    graph_dict = defaultdict(list)
    for node, next_node, weight in graph:
        graph_dict[node].append((weight, next_node))
    queue = [(0, start, ())]
    visited = set()
    while queue:
        cost, current_node, path = heappop(queue)
        if current_node not in visited:
            visited.add(current_node)
            path = (current_node, path)
            if current_node == end:
                return (cost, path)
            for weight, next_node in graph_dict.get(current_node, ()):
                if next_node not in visited:
                    heappush(queue, (cost + weight, next_node, path))
    return float("inf")
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
    print(dijkstra(graph, "A", "H"))