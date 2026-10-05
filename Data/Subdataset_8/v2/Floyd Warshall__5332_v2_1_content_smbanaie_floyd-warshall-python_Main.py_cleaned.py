from math import inf
from itertools import product
def floyd_warshall(n_vertices, edges):
    distances = [[inf] * n_vertices for _ in range(n_vertices)]
    next_nodes = [[0] * n_vertices for _ in range(n_vertices)]
    for i in range(n_vertices):
        distances[i][i] = 0
    for u, v, w in edges:
        distances[u - 1][v - 1] = w
        next_nodes[u - 1][v - 1] = v - 1
    for k, i, j in product(range(n_vertices), repeat=3):
        sum_ik_kj = distances[i][k] + distances[k][j]
        if distances[i][j] > sum_ik_kj:
            distances[i][j] = sum_ik_kj
            next_nodes[i][j] = next_nodes[i][k]
    print("    Pair        Distance     Path")
    for i, j in product(range(n_vertices), repeat=2):
        if i != j:
            path = [i]
            while path[-1] != j:
                path.append(next_nodes[path[-1]][j])
            print("%3d -> %3d  %7d       %s"
                  % (i + 1, j + 1, distances[i][j],
                     ' -> '.join(str(p + 1) for p in path)))
if __name__ == '__main__':
    floyd_warshall(4, [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]])