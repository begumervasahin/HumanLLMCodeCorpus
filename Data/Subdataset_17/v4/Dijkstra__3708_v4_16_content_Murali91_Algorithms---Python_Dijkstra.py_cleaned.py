import collections
class Dijkstra:
    def __init__(self, *nodes):
        self.nodes = list(nodes)
        self.distances = {node: float('inf') for node in self.nodes}
        self.edges = collections.defaultdict(dict)
    def add_edge(self, src, dest, cost):
        if src not in self.edges:
            self.edges[src] = {}
        self.edges[src][dest] = cost
    def traverse(self, node, neighbors):
        lowest_cost = float('inf')
        for neighbor, cost in neighbors.items():
            lowest_cost = min(lowest_cost, cost)
            if self.distances[neighbor] == float('inf') or self.distances[neighbor] > self.distances[node] + cost:
                self.distances[neighbor] = self.distances[node] + cost
        self.current_node = next((n for n, c in neighbors.items() if c == lowest_cost), None)
    def calculate(self, source):
        self.distances[source] = 0
        self.current_node = source
        visited = set()
        while self.current_node and self.current_node not in visited:
            visited.add(self.current_node)
            if self.current_node in self.edges:
                self.traverse(self.current_node, self.edges[self.current_node])
        return self.distances
if __name__ == '__main__':
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