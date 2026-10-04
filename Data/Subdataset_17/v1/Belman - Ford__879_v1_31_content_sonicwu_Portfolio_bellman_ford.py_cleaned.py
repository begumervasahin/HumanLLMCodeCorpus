def _initialize(graph, source):
    distance = {}
    predecessor = {}
    for node in graph:
        distance[node] = float('Inf')
        predecessor[node] = None
    distance[source] = 0
    return distance, predecessor
def _relax(node, neighbour, graph, distance, predecessor):
    if distance[neighbour] > distance[node] + graph[node][neighbour]:
        distance[neighbour] = distance[node] + graph[node][neighbour]
        predecessor[neighbour] = node
def bellman_ford(graph, source):
    distance, predecessor = _initialize(graph, source)
    for _ in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                _relax(u, v, graph, distance, predecessor)
    for u in graph:
        for v in graph[u]:
            if distance[v] > distance[u] + graph[u][v]:
                raise RuntimeError('Negative cycle detected, cannot find the shortest paths')
    return distance, predecessor
if __name__ == "__main__":
    graph = {
        'A': {'B': -1, 'C': 4},
        'B': {'C': 3, 'D': 2, 'E': 2},
        'C': {},
        'D': {'B': 1, 'C': 5},
        'E': {'D': -3}
    }
    source = 'A'
    try:
        distances, predecessors = bellman_ford(graph, source)
        print("Distances from source:", distances)
        print("Predecessors:", predecessors)
    except RuntimeError as e:
        print(e)