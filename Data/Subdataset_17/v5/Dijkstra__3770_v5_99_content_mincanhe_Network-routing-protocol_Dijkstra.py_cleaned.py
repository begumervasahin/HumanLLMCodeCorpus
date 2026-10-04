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
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    predecessors = {}
    distances[start] = 0
    unvisited_nodes = set(graph.nodes)
    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: distances[node])
        if distances[current_node] == float('inf'):
            break
        unvisited_nodes.remove(current_node)
        current_distance = distances[current_node]
        for neighbor in graph.edges[current_node]:
            edge_weight = graph.distances[(current_node, neighbor)]
            new_distance = current_distance + edge_weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node
    return distances, predecessors
if __name__ == '__main__':
    graph = Graph()
    nodes = [0, 1, 2, 3, 4]
    edges = [
        (0, 1, 6),
        (0, 2, 1),
        (0, 3, 4),
        (1, 4, 3),
        (2, 1, -3),
        (2, 3, 2),
        (3, 4, -1),
        (4, 2, 5)
    ]
    for node in nodes:
        graph.add_node(node)
    for from_node, to_node, distance in edges:
        graph.add_edge(from_node, to_node, distance)
    distances, predecessors = dijkstra(graph, 0)
    print("Shortest distances from start node 0 to all other nodes:")
    for node, distance in distances.items():
        print(f"Node {node}: Distance = {distance}")
    print("\nPredecessors in the shortest paths from start node 0:")
    for node, predecessor in predecessors.items():
        print(f"Node {node}: Predecessor = {predecessor}")