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
def dijkstra(graph, start_node):
    visited = {start_node: 0}
    path = {}
    nodes = set(graph.nodes)
    while nodes:
        current_node = None
        for node in nodes:
            if node in visited:
                if current_node is None or visited[node] < visited[current_node]:
                    current_node = node
        if current_node is None:
            break
        nodes.remove(current_node)
        current_weight = visited[current_node]
        for neighbor in graph.edges[current_node]:
            weight = current_weight + graph.distances[(current_node, neighbor)]
            if neighbor not in visited or weight < visited[neighbor]:
                visited[neighbor] = weight
                path[neighbor] = current_node
    return visited, path
def main():
    graph = Graph()
    nodes = ['A', 'B', 'C', 'D', 'E']
    for node in nodes:
        graph.add_node(node)
    edges = [
        ('A', 'B', 1),
        ('A', 'C', 3),
        ('B', 'C', 1),
        ('B', 'D', 6),
        ('C', 'D', 4),
        ('C', 'E', 2),
        ('D', 'E', 1)
    ]
    for edge in edges:
        graph.add_edge(*edge)
    visited, path = dijkstra(graph, 'A')
    print("Visited Nodes and Distances:", visited)
    print("Shortest Paths:", path)
if __name__ == '__main__':
    main()