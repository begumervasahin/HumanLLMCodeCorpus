import pdb
def initialize(graph, source):
    distances = {node: float('Inf') for node in graph}
    predecessors = {node: None for node in graph}
    distances[source] = 0
    return distances, predecessors
def relax(node, neighbor, graph, distances, predecessors):
    new_distance = distances[node] + graph[node][neighbor]
    if distances[neighbor] > new_distance:
        distances[neighbor] = new_distance
        predecessors[neighbor] = node
def bellman_ford(graph, source):
    distances, predecessors = initialize(graph, source)
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor in graph[node]:
                relax(node, neighbor, graph, distances, predecessors)
    for node in graph:
        for neighbor in graph[node]:
            if distances[neighbor] > distances[node] + graph[node][neighbor]:
                raise ValueError("Graph contains a negative weight cycle")
    return distances, predecessors
def test_bellman_ford():
    graph = {
        'a': {'b': -2, 'c': 1, 'd': 4},
        'b': {'e': 3},
        'c': {'b': -3, 'd': 2},
        'd': {'e': -1},
        'e': {'c': 5}
    }
    distances, predecessors = bellman_ford(graph, 'a')
    print("The shortest distances from source 'a' to all other nodes are:")
    for node in graph:
        print(f"{node} = {distances[node]}")
    print("\nThe paths (predecessors) from source 'a' to all other nodes are:")
    for node in graph:
        print(f"{node} = {predecessors[node]}")
if __name__ == '__main__':
    test_bellman_ford()