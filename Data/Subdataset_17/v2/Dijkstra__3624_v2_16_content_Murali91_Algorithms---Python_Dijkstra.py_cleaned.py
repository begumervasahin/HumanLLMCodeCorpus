import collections
class Dijkstra:
    def __init__(self, *nodes):
        self.nodes = list(nodes)
        self.distances = dict.fromkeys(self.nodes, float('inf'))
        self.edges = collections.defaultdict(dict)
    def add_edge(self, src, dest, cost):
        self.edges[src][dest] = cost
    def calculate(self, source):
        self.distances[source] = 0
        visited = set()
        nodes_to_visit = [source]
        while nodes_to_visit:
            current_node = nodes_to_visit.pop(0)
            if current_node in visited:
                continue
            visited.add(current_node)
            for neighbor, cost in self.edges[current_node].items():
                if self.distances[neighbor] > self.distances[current_node] + cost:
                    self.distances[neighbor] = self.distances[current_node] + cost
                    nodes_to_visit.append(neighbor)
        print(self.distances)
if __name__ == '__main__':
    graph = Dijkstra('a', 'b', 'c', 'd', 'e')
    graph.add_edge('a', 'b', 1)
    graph.add_edge('a', 'c', 4)
    graph.add_edge('b', 'c', 2)
    graph.add_edge('b', 'd', 5)
    graph.add_edge('c', 'd', 1)
    graph.add_edge('d', 'e', 3)
    graph.calculate('a')