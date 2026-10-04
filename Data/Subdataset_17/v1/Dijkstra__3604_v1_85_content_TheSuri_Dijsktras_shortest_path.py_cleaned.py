import heapq
class Graph:
    def __init__(self):
        self.adjacency_list = {}
    def add_edge(self, u, v, weight):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))
    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])
def shortest_path(graph, source, target):
    priority_q = []
    heapq.heappush(priority_q, (0, source))
    visited = set()
    path = {source: None}
    remaining = {}
    while priority_q:
        curr_path_weight, curr_node = heapq.heappop(priority_q)
        if curr_node in visited:
            continue
        if curr_node == target:
            return get_path(source, curr_node, path), curr_path_weight
        for neighbor, edge_weight in graph.get_neighbors(curr_node):
            if neighbor not in visited and (neighbor not in remaining or remaining[neighbor] > curr_path_weight + edge_weight):
                remaining[neighbor] = curr_path_weight + edge_weight
                path[neighbor] = curr_node
                heapq.heappush(priority_q, (remaining[neighbor], neighbor))
        visited.add(curr_node)
    return None, float('inf')
def get_path(source, target, path_dict):
    result = []
    node = target
    while node is not None:
        result.append(node)
        node = path_dict[node]
    result.reverse()
    return result
def main():
    graph = Graph()
    graph.add_edge(1, 2, 15)
    graph.add_edge(1, 3, 71)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 4, 1)
    graph.add_edge(3, 4, 19)
    graph.add_edge(4, 3, 1)
    source = 1
    target = 4
    path, distance = shortest_path(graph, source, target)
    if path:
        print(f"Shortest path from {source} to {target}: {path}")
        print(f"Total distance: {distance}")
    else:
        print(f"No path found from {source} to {target}")
if __name__ == "__main__":
    main()