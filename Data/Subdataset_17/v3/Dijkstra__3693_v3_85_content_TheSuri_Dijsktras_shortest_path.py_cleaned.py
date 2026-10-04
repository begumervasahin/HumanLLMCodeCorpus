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
    priority_queue = []
    heapq.heappush(priority_queue, (0, source))
    visited = set()
    path = {source: None}
    distances = {source: 0}
    while priority_queue:
        curr_distance, curr_node = heapq.heappop(priority_queue)
        if curr_node in visited:
            continue
        if curr_node == target:
            return get_path(source, target, path), curr_distance
        visited.add(curr_node)
        for neighbor, edge_weight in graph.get_neighbors(curr_node):
            if neighbor not in visited:
                new_distance = curr_distance + edge_weight
                if neighbor not in distances or new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    path[neighbor] = curr_node
                    heapq.heappush(priority_queue, (new_distance, neighbor))
    return None, float('inf')
def get_path(source, target, path_dict):
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = path_dict.get(node)
    path.reverse()
    return path
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