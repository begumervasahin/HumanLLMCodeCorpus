def pop_min(pqueue):
    min_key = min(pqueue, key=pqueue.get)
    del pqueue[min_key]
    return min_key
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    predecessors = {node: -1 for node in graph}
    unvisited = {node: float('inf') for node in graph}
    distances[start] = 0
    unvisited[start] = 0
    while unvisited:
        current_node = pop_min(unvisited)
        for neighbor, weight in graph[current_node].items():
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node
                unvisited[neighbor] = new_distance
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