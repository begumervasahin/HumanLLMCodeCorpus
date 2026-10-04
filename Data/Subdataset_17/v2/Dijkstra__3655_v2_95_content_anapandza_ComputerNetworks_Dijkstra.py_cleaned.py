def popmin(pqueue):
    lowest = float('inf')
    keylowest = None
    for key, value in pqueue.items():
        if value < lowest:
            lowest = value
            keylowest = key
    if keylowest is not None:
        del pqueue[keylowest]
    return keylowest
def dijkstra(graph, start):
    pqueue = {}
    dist = {}
    pred = {}
    for node in graph:
        dist[node] = float('inf')
        pred[node] = None
        pqueue[node] = dist[node]
    dist[start] = 0
    pqueue[start] = dist[start]
    while pqueue:
        current_node = popmin(pqueue)
        for neighbor, weight in graph.get(current_node, {}).items():
            new_distance = dist[current_node] + weight
            if new_distance < dist[neighbor]:
                dist[neighbor] = new_distance
                pred[neighbor] = current_node
                pqueue[neighbor] = new_distance
    return dist, pred
if __name__ == '__main__':
    graph = {
        0: {1: 6, 2: 1, 3: 4},
        1: {4: 3},
        2: {1: -3, 3: 2},
        3: {4: -1},
        4: {2: 5},
    }
    dist, pred = dijkstra(graph, 0)
    print("Shortest distance from start node 0 to all other nodes:")
    for node, distance in dist.items():
        print(f"Node {node}: Distance = {distance}")
    print("\nPredecessors in the shortest paths from start node 0:")
    for node, predecessor in pred.items():
        print(f"Node {node}: Predecessor = {predecessor}")