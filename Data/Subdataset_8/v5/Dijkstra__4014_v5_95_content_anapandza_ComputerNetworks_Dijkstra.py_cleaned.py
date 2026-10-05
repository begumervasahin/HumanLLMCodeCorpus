def pop_min(priority_queue):
    min_distance = float('inf')
    min_node = None
    for node, distance in priority_queue.items():
        if distance < min_distance:
            min_distance = distance
            min_node = node
    del priority_queue[min_node]
    return min_node
def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph}
    predecessors = {node: -1 for node in graph}
    priority_queue = {node: float('inf') for node in graph}
    distances[start_node] = 0
    priority_queue[start_node] = 0
    while priority_queue:
        current_node = pop_min(priority_queue)
        for neighbor, weight in graph[current_node].items():
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node
                priority_queue[neighbor] = new_distance
    return distances, predecessors
graph = {
    0: {1: 6, 2: 1, 3: 4},
    1: {4: 3},
    2: {1: -3, 3: 2},
    3: {4: -1},
    4: {2: 5},
}
shortest_distances, predecessors = dijkstra(graph, 0)
print("Shortest distances from start node 0 to all other nodes:")
for node, distance in shortest_distances.items():
    print(f"{node} = {distance}")
print("Predecessors of nodes in the shortest paths:")
for node, predecessor in predecessors.items():
    print(f"{node} = {predecessor}")