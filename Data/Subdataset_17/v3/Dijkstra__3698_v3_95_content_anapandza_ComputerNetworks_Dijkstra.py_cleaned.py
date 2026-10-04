def pop_min(pqueue):
    min_value = float('inf')
    key_with_min_value = None
    for key, value in pqueue.items():
        if value < min_value:
            min_value = value
            key_with_min_value = key
    if key_with_min_value is not None:
        del pqueue[key_with_min_value]
    return key_with_min_value
def dijkstra(graph, start):
    priority_queue = {}
    distances = {}
    predecessors = {}
    for node in graph:
        distances[node] = float('inf')
        predecessors[node] = None
        priority_queue[node] = distances[node]
    distances[start] = 0
    priority_queue[start] = distances[start]
    while priority_queue:
        current_node = pop_min(priority_queue)
        for neighbor, weight in graph.get(current_node, {}).items():
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node
                priority_queue[neighbor] = new_distance
    return distances, predecessors
if __name__ == '__main__':
    graph = {
        0: {1: 6, 2: 1, 3: 4},
        1: {4: 3},
        2: {1: -3, 3: 2},
        3: {4: -1},
        4: {2: 5},
    }
    distances, predecessors = dijkstra(graph, 0)
    print("Shortest distances from start node 0 to all other nodes:")
    for node, distance in distances.items():
        print(f"Node {node}: Distance = {distance}")
    print("\nPredecessors in the shortest paths from start node 0:")
    for node, predecessor in predecessors.items():
        print(f"Node {node}: Predecessor = {predecessor}")