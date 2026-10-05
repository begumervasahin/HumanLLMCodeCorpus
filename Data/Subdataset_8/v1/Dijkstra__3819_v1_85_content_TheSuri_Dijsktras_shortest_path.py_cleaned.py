import heapq
class Graph:
    def __init__(self):
        self.adjacency_list = {}
    def add_edge(self, u, v, weight):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append((v, weight))
    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])
class ShortestPathFinder:
    def __init__(self, graph):
        self.graph = graph
    def shortest_path(self, source, target):
        priority_q = []
        heapq.heappush(priority_q, (0, source))
        visited = set()
        path = {source: None}
        remaining = {}
        while priority_q:
            curr_path_weight, curr_node = heapq.heappop(priority_q)
            if curr_node in visited:
                continue
            elif curr_node == target:
                return self.get_path(source, curr_node, path), curr_path_weight
            for neighbor, edge_weight in self.graph.get_neighbors(curr_node):
                if neighbor not in visited and (neighbor not in remaining or remaining[neighbor] > curr_path_weight + edge_weight):
                    remaining[neighbor] = curr_path_weight + edge_weight
                    path[neighbor] = curr_node
                    heapq.heappush(priority_q, (remaining[neighbor], neighbor))
            visited.add(curr_node)
        return None
    def get_path(self, source, target, path_dict):
        result = []
        node = target
        while node is not None:
            result.append(node)
            node = path_dict[node]
        return result
def main():
    graph = Graph()
    graph.add_edge('A', 'B', 5)
    graph.add_edge('A', 'C', 3)
    graph.add_edge('B', 'D', 2)
    graph.add_edge('C', 'D', 4)
    graph.add_edge('D', 'E', 6)
    path_finder = ShortestPathFinder(graph)
    source = 'A'
    target = 'E'
    shortest_path, shortest_distance = path_finder.shortest_path(source, target)
    if shortest_path:
        print(f"Shortest path from {source} to {target}: {' -> '.join(shortest_path)}")
        print(f"Shortest distance: {shortest_distance}")
    else:
        print(f"No path found from {source} to {target}")
if __name__ == "__main__":
    main()