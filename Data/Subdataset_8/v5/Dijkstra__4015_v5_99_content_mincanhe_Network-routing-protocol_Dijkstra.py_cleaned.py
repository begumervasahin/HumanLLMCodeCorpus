import collections
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = collections.defaultdict(list)
        self.distances = {}
    def add_node(self, node):
        self.nodes.add(node)
    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance
def dijkstra(graph, start_node):
    visited = {start_node: 0}
    path = {}
    unvisited_nodes = set(graph.nodes)
    while unvisited_nodes:
        max_node = None
        for node in unvisited_nodes:
            if node in visited:
                if max_node is None or visited[node] > visited[max_node]:
                    max_node = node
        if max_node is None:
            break
        unvisited_nodes.remove(max_node)
        current_weight = visited[max_node]
        for neighbor in graph.edges[max_node]:
            weight = current_weight + graph.distances[(max_node, neighbor)]
            if neighbor not in visited or weight > visited[neighbor]:
                visited[neighbor] = weight
                path[neighbor] = max_node
    return visited, path