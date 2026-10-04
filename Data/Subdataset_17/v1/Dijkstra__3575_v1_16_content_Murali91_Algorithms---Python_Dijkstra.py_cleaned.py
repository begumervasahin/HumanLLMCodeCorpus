import collections
class Dijkstra:
    def __init__(self, *args):
        self.nodes = list(args)
        self.result = dict.fromkeys(self.nodes, float('inf'))
        self.edges = collections.defaultdict(dict)
    def add_edge(self, src, dest, dist):
        self.edges[src][dest] = dist
    def traverse(self, index, item):
        low = float('inf')
        for key, value in item.items():
            low = min(low, self.result[index] + value)
            if self.result[value] == float('inf') or self.result[value] > self.result[index] + value:
                self.result[value] = self.result[index] + value
    def calculate(self, source):
        self.result[source] = 0
        visited = set()
        nodes_to_visit = [source]
        while nodes_to_visit:
            current_node = nodes_to_visit.pop(0)
            if current_node in visited:
                continue
            visited.add(current_node)
            if current_node in self.edges:
                for neighbor, dist in self.edges[current_node].items():
                    if self.result[neighbor] > self.result[current_node] + dist:
                        self.result[neighbor] = self.result[current_node] + dist
                        nodes_to_visit.append(neighbor)
        print(self.result)
if __name__ == '__main__':
    graph = Dijkstra('a', 'b', 'c', 'd', 'e')
    graph.add_edge('a', 'b', 1)
    graph.add_edge('a', 'c', 4)
    graph.add_edge('b', 'c', 2)
    graph.add_edge('b', 'd', 5)
    graph.add_edge('c', 'd', 1)
    graph.add_edge('d', 'e', 3)
    graph.calculate('a')