def popmin(pqueue):
    key_lowest = min(pqueue, key=pqueue.get)
    del pqueue[key_lowest]
    return key_lowest
def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    pred = {node: None for node in graph}
    dist[start] = 0
    pqueue = {node: dist[node] for node in graph}
    while pqueue:
        u = popmin(pqueue)
        for v, weight in graph[u].items():
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                pqueue[v] = new_dist
                dist[v] = new_dist
                pred[v] = u
    return dist, pred
def print_results(dist, pred):
    print("Shortest distances from the start node to all other nodes:")
    for node, distance in dist.items():
        print(f"Node {node}: {distance}")
    print("\nPaths from the start node to all other nodes (predecessors of nodes):")
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