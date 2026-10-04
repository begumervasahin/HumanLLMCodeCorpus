def popmin(pqueue):
    key_lowest = min(pqueue, key=pqueue.get)
    del pqueue[key_lowest]
    return key_lowest
def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph}
    pred = {v: None for v in graph}
    dist[start] = 0
    pqueue = {v: dist[v] for v in graph}
    while pqueue:
        u = popmin(pqueue)
        for v, w in graph[u].items():
            new_dist = dist[u] + w
            if new_dist < dist[v]:
                pqueue[v] = new_dist
                dist[v] = new_dist
                pred[v] = u
    return dist, pred
def print_results(dist, pred):
    print("Shortest distances from start node to all other nodes:")
    for node, distance in dist.items():
        print(f"Node {node}: {distance}")
    print("\nPaths from start node to all other nodes (predecessors of nodes):")
    for node, predecessor in pred.items():
        print(f"Node {node}: {predecessor}")
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
    print_results(dist, pred)
if __name__ == "__main__":
    main()