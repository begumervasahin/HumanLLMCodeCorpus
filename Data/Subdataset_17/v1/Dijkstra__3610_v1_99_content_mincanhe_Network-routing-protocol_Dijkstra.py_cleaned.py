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
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break
        nodes.remove(min_node)
        current_weight = visited[min_node]
        for neighbor in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, neighbor)]
            if neighbor not in visited or weight < visited[neighbor]:
                visited[neighbor] = weight
                path[neighbor] = min_node
    return visited, path
if __name__ == '__main__':
    g = Graph()
    g.add_node(0)
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_edge(0, 1, 6)
    g.add_edge(0, 2, 1)
    g.add_edge(0, 3, 4)
    g.add_edge(1, 4, 3)
    g.add_edge(2, 1, -3)
    g.add_edge(2, 3, 2)
    g.add_edge(3, 4, -1)
    g.add_edge(4, 2, 5)
    distances, predecessors = dijkstra(g, 0)
    print("Shortest distances from start node 0 to all other nodes:")
    for node, distance in distances.items():
        print(f"Node {node}: Distance = {distance}")
    print("\nPredecessors in the shortest paths from start node 0:")
    for node, predecessor in predecessors.items():
        print(f"Node {node}: Predecessor = {predecessor}")