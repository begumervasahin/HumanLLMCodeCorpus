def pop_min(pqueue):
    lowest = float('inf')
    keylowest = None
    for key in pqueue:
        if pqueue[key] < lowest:
            lowest = pqueue[key]
            keylowest = key
    del pqueue[keylowest]
    return keylowest
def dijkstra(graph, start):
    pqueue = {}
    dist = {}
    pred = {}
    for v in graph:
        dist[v] = float('inf')
        pred[v] = -1
    dist[start] = 0
    for v in graph:
        pqueue[v] = dist[v]
    while pqueue:
        u = pop_min(pqueue)
        for v in graph[u].keys():
            w = graph[u][v]
            new_dist = dist[u] + w
            if new_dist < dist[v]:
                pqueue[v] = new_dist
                dist[v] = new_dist
                pred[v] = u
    return dist, pred
graph = {
    0: {1: 6, 2: 1, 3: 4},
    1: {4: 3},
    2: {1: -3, 3: 2},
    3: {4: -1},
    4: {2: 5},
}
distances, predecessors = dijkstra(graph, 0)
print("Shortest distance from start node 0 to all other nodes:")
for v in distances:
    print(v, '=', distances[v])
print("Paths from start node to all other nodes (predecessors of nodes):")
for v in predecessors:
    print(v, '=', predecessors[v])