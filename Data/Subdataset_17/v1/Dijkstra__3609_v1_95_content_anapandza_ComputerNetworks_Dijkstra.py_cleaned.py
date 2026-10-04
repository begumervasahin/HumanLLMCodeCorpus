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
    for v in graph:
        dist[v] = float('inf')
        pred[v] = None
        pqueue[v] = dist[v]
    dist[start] = 0
    pqueue[start] = dist[start]
    while pqueue:
        u = popmin(pqueue)
        for v, w in graph.get(u, {}).items():
            newdist = dist[u] + w
            if newdist < dist[v]:
                dist[v] = newdist
                pred[v] = u
                pqueue[v] = newdist
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
    for v, d in dist.items():
        print(f"Node {v}: Distance = {d}")
    print("\nPredecessors of nodes in the shortest paths from start node 0:")
    for v, p in pred.items():
        print(f"Node {v}: Predecessor = {p}")