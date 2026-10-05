import collections
class Dijkstra:
    def __init__(self, *nodes):
        self.nodes = list(nodes)
        self.distances = {node: float('inf') for node in self.nodes}
        self.edges = collections.defaultdict(dict)
    def add_edge(self, src, dest, dist):
        if src not in self.edges:
            self.edges[src] = {}
        self.edges[src][dist] = dest
    def relax(self, source, destinations):
        min_distance = float('inf')
        for distance, destination in destinations.items():
            min_distance = min(min_distance, distance)
            if self.distances[destination] == float('inf') or self.distances[destination] > distance + self.distances[source]:
                self.distances[destination] = distance + self.distances[source]
        self.source = destinations[min_distance]
    def calculate_shortest_paths(self, source):
        self.source = source
        if self.source in self.edges:
            self.distances[self.source] = 0
            for _ in range(len(self.edges)):
                for source_node, destinations in self.edges.items():
                    if source_node == self.source or self.distances[source_node] != float('inf'):
                        self.relax(source_node, destinations)
        print(self.distances)
if __name__ == '__main__':
    dijkstra = Dijkstra('A', 'B', 'C', 'D', 'E')
    dijkstra.add_edge('A', 'B', 4)
    dijkstra.add_edge('A', 'C', 2)
    dijkstra.add_edge('B', 'C', 5)
    dijkstra.add_edge('B', 'D', 10)
    dijkstra.add_edge('C', 'D', 3)
    dijkstra.add_edge('C', 'E', 7)
    dijkstra.add_edge('D', 'E', 8)
    dijkstra.calculate_shortest_paths('A')
