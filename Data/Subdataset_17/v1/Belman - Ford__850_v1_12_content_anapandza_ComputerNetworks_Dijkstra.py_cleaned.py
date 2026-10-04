def popmin(pqueue):
    lowest = float('inf')
    key_lowest = None
    for key in pqueue:
        if pqueue[key] < lowest:
            lowest = pqueue[key]
            key_lowest = key
    del pqueue[key_lowest]
    return key_lowest
def dijkstra(graph, start):
    pqueue = {}
    dist = {}
    pred = {}
    for v in graph:
        dist[v] = float('inf')
        pred[v] = None
    dist[start] = 0
    for v in graph:
        pqueue[v] = dist[v]
    while pqueue:
        u = popmin(pqueue)
        for v in graph[u]:
            w = graph[u][v]
            new_dist = dist[u] + w
            if new_dist < dist[v]:
                pqueue[v] = new_dist
                dist[v] = new_dist
                pred[v] = u
    return dist, pred
def main():
    graph = {
        0: {1: 6, 2: 1, 3: 4},
        1: {4: 3},
        2: {1: -3, 3: 2},
        3: {4: -1},
        4: {2: 5},
    }
    start_node = 0
    dist, pred = dijkstra(graph, start_node)
    print("Shortest distance from start node 0 to all other nodes is:")
    for v in dist:
        print(f"{v} = {dist[v]}")
    print("Paths from start node to all other nodes (predecessors of nodes):")
    for v in pred:
        print(f"{v} = {pred[v]}")
if __name__ == "__main__":
    main()