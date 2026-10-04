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
    unvisited_nodes = set(graph.nodes)
    while unvisited_nodes:
        current_node = None
        for node in unvisited_nodes:
            if node in visited:
                if current_node is None or visited[node] < visited[current_node]:
                    current_node = node
        if current_node is None:
            break
        unvisited_nodes.remove(current_node)
        current_distance = visited[current_node]
        for neighbor in graph.edges[current_node]:
            distance = current_distance + graph.distances[(current_node, neighbor)]
            if neighbor not in visited or distance < visited[neighbor]:
                visited[neighbor] = distance
                path[neighbor] = current_node
    return visited, path
