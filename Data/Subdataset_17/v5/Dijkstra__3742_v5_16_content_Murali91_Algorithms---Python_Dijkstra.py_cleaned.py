import collections
class Dijkstra:
    def __init__(self, *nodes):
        self.nodes = list(nodes)
        self.distances = {node: float('inf') for node in self.nodes}
        self.edges = collections.defaultdict(dict)
    def add_edge(self, src, dest, cost):
        self.edges[src][dest] = cost
    def _update_distances(self, node, neighbors):
        for neighbor, cost in neighbors.items():
            new_distance = self.distances[node] + cost
            if new_distance < self.distances[neighbor]:
                self.distances[neighbor] = new_distance
    def calculate(self, source):
        self.distances[source] = 0
        visited = set()
        while len(visited) < len(self.nodes):
            current_node = min((node for node in self.nodes if node not in visited), key=lambda node: self.distances[node])
            visited.add(current_node)
            if current_node in self.edges:
                self._update_distances(current_node, self.edges[current_node])
        return self.distances
def main():
    graph = Dijkstra('a', 'b', 'c', 'd', 'e')
    graph.add_edge('a', 'b', 1)
    graph.add_edge('a', 'c', 4)
    graph.add_edge('b', 'c', 2)
    graph.add_edge('b', 'd', 5)
    graph.add_edge('c', 'd', 1)
    graph.add_edge('d', 'e', 3)
    shortest_paths = graph.calculate('a')
    print("Shortest paths from node 'a':")
    for node, distance in shortest_paths.items():
        print(f"Distance to {node}: {distance}")
if __name__ == '__main__':
    main()