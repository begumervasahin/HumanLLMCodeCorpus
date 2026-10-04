import numpy as np
def bellman_ford(start, end, weights):
    num_vertices = weights.shape[0]
    dist = np.full(num_vertices, np.inf)
    pred = np.full(num_vertices, None)
    dist[start] = 0
    for _ in range(num_vertices - 1):
        for u in range(num_vertices):
            for v in range(num_vertices):
                weight = weights[u, v]
                if weight != 0 and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    pred[v] = u
    for u in range(num_vertices):
        for v in range(num_vertices):
            weight = weights[u, v]
            if weight != 0 and dist[u] + weight < dist[v]:
                raise ValueError('Graph contains a negative-weight cycle')
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = pred[current_node]
    path.reverse()
    if path[0] != start:
        raise ValueError('No path from start to end')
    return path
def main():
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
    except ValueError as error:
        print(error)
if __name__ == "__main__":
    main()