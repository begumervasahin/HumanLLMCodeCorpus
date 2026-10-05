from math import inf
from itertools import product
def floyd_warshall(num_vertices, edges):
    distance_matrix = [[inf] * num_vertices for _ in range(num_vertices)]
    next_node_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    for i in range(num_vertices):
        distance_matrix[i][i] = 0
    for source, destination, weight in edges:
        distance_matrix[source - 1][destination - 1] = weight
        next_node_matrix[source - 1][destination - 1] = destination - 1
    for k, i, j in product(range(num_vertices), repeat=3):
        sum_ik_kj = distance_matrix[i][k] + distance_matrix[k][j]
        if distance_matrix[i][j] > sum_ik_kj:
            distance_matrix[i][j] = sum_ik_kj
            next_node_matrix[i][j] = next_node_matrix[i][k]
    print("    Pair        Distance     Path")
    for i, j in product(range(num_vertices), repeat=2):
        if i != j:
            path = [i]
            while path[-1] != j:
                path.append(next_node_matrix[path[-1]][j])
            print("%3d -> %3d  %7d       %s"
                  % (i + 1, j + 1, distance_matrix[i][j],
                     ' -> '.join(str(p + 1) for p in path)))
if __name__ == '__main__':
    floyd_warshall(4, [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]])