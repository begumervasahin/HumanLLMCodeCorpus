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
graph = Graph()
graph.add_node(0)
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_edge(0, 1, 6)
graph.add_edge(0, 2, 1)
graph.add_edge(0, 3, 4)
graph.add_edge(1, 4, 3)
graph.add_edge(2, 1, -3)
graph.add_edge(2, 3, 2)
graph.add_edge(3, 4, -1)
graph.add_edge(4, 2, 5)
shortest_distances, predecessors = dijkstra(graph, 0)
print("Shortest distances from start node 0 to all other nodes:")
for node, distance in shortest_distances.items():
    print(f"{node} = {distance}")
print("Predecessors of nodes in the shortest paths:")
for node, predecessor in predecessors.items():
    print(f"{node} = {predecessor}")