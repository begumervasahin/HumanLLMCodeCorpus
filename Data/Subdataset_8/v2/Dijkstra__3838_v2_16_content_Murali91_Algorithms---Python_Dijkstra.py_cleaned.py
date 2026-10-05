import collections
class Dijkstra:
    def __init__(self, *nodes):
        self.nodes = list(nodes)
        self.result = {node: float('inf') for node in self.nodes}
        self.edges = collections.defaultdict(dict)
    def add_path(self, src, dest, dist):
        if src not in self.edges:
            self.edges[src] = {}
        self.edges[src][dist] = dest
    def traverse(self, index, item):
        min_dist = float('inf')
        for key, value in item.items():
            min_dist = min(min_dist, key)
            if self.result[value] == float('inf') or self.result[value] > key + self.result[index]:
                self.result[value] = key + self.result[index]
        self.source = item[min_dist]
    def calculate(self, source):
        self.source = source
        if self.source in self.edges:
            self.result[self.source] = 0
            i = 0
            while i <= len(self.edges):
                for key, value in self.edges.items():
                    if key == self.source or self.result[key] != float('inf'):
                        self.traverse(key, value)
                i += 1
        print(self.result)
if __name__ == '__main__':
    dijkstra = Dijkstra('A', 'B', 'C', 'D', 'E')
    dijkstra.add_path('A', 'B', 4)
    dijkstra.add_path('A', 'C', 2)
    dijkstra.add_path('B', 'C', 5)
    dijkstra.add_path('B', 'D', 10)
    dijkstra.add_path('C', 'D', 3)
    dijkstra.add_path('C', 'E', 7)
    dijkstra.add_path('D', 'E', 8)
    dijkstra.calculate('A')
