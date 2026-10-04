import collections
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = collections.defaultdict(list)
        self.distances = {}
    def add_node(self, value):
        self.nodes.add(value)
    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance
def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}
    nodes = set(graph.nodes)
    while nodes:
        max_node = None
        for node in nodes:
            if node in visited:
                if max_node is None:
                    max_node = node
                elif visited[node] > visited[max_node]:
                    max_node = node
        if max_node is None:
            break
        nodes.remove(max_node)
        current_weight = visited[max_node]
        for edge in graph.edges[max_node]:
            weight = current_weight + graph.distances[(max_node, edge)]
            if edge not in visited or weight > visited[edge]:
                visited[edge] = weight
                path[edge] = max_node
    return visited, path
if __name__ == '__main__':
    graph = Graph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_node('D')
    graph.add_node('E')
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 3)
    graph.add_edge('B', 'C', 1)
    graph.add_edge('B', 'D', 6)
    graph.add_edge('C', 'D', 4)
    graph.add_edge('C', 'E', 2)
    graph.add_edge('D', 'E', 1)
    visited, path = dijkstra(graph, 'A')
    print("Visited Nodes and Distances:", visited)
    print("Paths:", path)