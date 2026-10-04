import numpy as np
import sys
def bellman_ford(start, end, weights):
    V = weights.shape[0]
    Inf = sys.maxsize
    dist = np.ones(V) * np.inf
    pred = np.zeros(V, dtype=int) * Inf
    dist[start] = 0
    for _ in range(V - 1):
        for u in range(V):
            for v in range(V):
                w = weights[u, v]
                if w != 0 and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    pred[v] = u
    for u in range(V):
        for v in range(V):
            w = weights[u, v]
            if w != 0 and dist[u] + w < dist[v]:
                raise ValueError('Graph contains a negative-weight cycle')
    path = []
    current = end
    while current != start:
        path.append(current)
        current = pred[current]
    path.append(start)
    path.reverse()
    return path
if __name__ == '__main__':
    start_node = 4
    end_node = 3
    weights = np.array([
        [0, 20,  0, 80, 0,  0, 90,  0],
        [0,  0,  0,  0, 0, 10,  0,  0],
        [0,  0,  0, 10, 0, 50,  0, 20],
        [0,  0, 10,  0, 0,  0, 20,  0],
        [0, 50,  0,  0, 0,  0, 30,  0],
        [0,  0, 10, 40, 0,  0,  0,  0],
        [20,  0,  0,  0, 0,  0,  0,  0],
        [0,  0,  0,  0, 0,  0,  0,  0]
    ])
    try:
        shortest_path = bellman_ford(start_node, end_node, weights)
        print(f"The shortest path from {start_node} to {end_node} is: {shortest_path}")
    except ValueError as e:
        print(e)