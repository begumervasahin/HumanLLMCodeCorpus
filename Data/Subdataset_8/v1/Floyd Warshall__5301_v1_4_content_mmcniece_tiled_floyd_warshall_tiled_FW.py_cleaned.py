import random
import timeit
from pprint import pprint
from copy import deepcopy
MAXINT = 100000000
N = 9
tile_size = 3
global_debug = False
negative_edges = True
def generate_adj_matrix(dim, connectivity=0.5):
    global negative_edges
    matrix = [[0] * dim for _ in range(dim)]
    if negative_edges:
        lower_bound_weight = -1
    else:
        lower_bound_weight = 1
    for _ in range(int(connectivity * (dim**2))):
        rand_row = random.randint(0, dim - 1)
        rand_col = random.randint(0, dim - 1)
        if rand_col == rand_row:
            continue
        rand_weight = random.randint(lower_bound_weight, 20)
        matrix[rand_row][rand_col] = rand_weight
    for i in range(dim):
        for j in range(dim):
            if i != j and matrix[i][j] == 0:
                matrix[i][j] = MAXINT
    return matrix
def floyd_warshall(graph):
    dist = [deepcopy(row) for row in graph]
    n = len(graph[0])
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
def pad_matrix(matrix, tile_size):
    dimension_rem = len(matrix[0]) % tile_size
    if dimension_rem == 0:
        return matrix
    else:
        dim_to_add = tile_size - dimension_rem
    total_dim = len(matrix[0]) + dim_to_add
    for i in range(len(matrix)):
        matrix[i].extend([MAXINT] * dim_to_add)
    matrix.extend([[MAXINT] * total_dim for _ in range(dim_to_add)])
    assert len(matrix) == total_dim
    assert len(matrix[0]) == total_dim
    return matrix
def update_submatrix(a_row, a_col, b_row, b_col, c_row, c_col, matrix, block_size, debug=False):
    for k in range(block_size):
        for i in range(block_size):
            for j in range(block_size):
                matrix[a_row + i][a_col + j] = min(matrix[a_row + i][a_col + j],
                                                   matrix[b_row + i][b_col + k] + matrix[c_row + k][c_col + j])
                if debug:
                    print("Ai, Aj", a_row + i, a_col + j, "Bi, Bk", b_row+i, b_col+k, "Ck, Cj", c_row+k, c_col+j)
    return matrix
def tiled_floyd_warshall(matrix, tile_size):
    matrix = pad_matrix(matrix, tile_size)
    num_tiles_row = len(matrix)
    nb_row = len(matrix)
    for d in range(num_tiles_row):
        update_submatrix(d * nb_row, d * nb_row, d * nb_row, d * nb_row, d * nb_row, d * nb_row, matrix, tile_size)
        for j in range(num_tiles_row):
            if j == d:
                continue
            update_submatrix(d * nb_row, j * nb_row,
                             d * nb_row, d * nb_row,
                             d * nb_row, j * nb_row,
                             matrix, tile_size)
        for i in range(num_tiles_row):
            if i == d:
                continue
            update_submatrix(i * nb_row, d * nb_row,
                             i * nb_row, d * nb_row,
                             d * nb_row, d * nb_row,
                             matrix, tile_size)
        for i in range(num_tiles_row):
            for j in range(num_tiles_row):
                if i == d or j == d:
                    continue
                update_submatrix(i * nb_row, j * nb_row,
                                 i * nb_row, d * nb_row,
                                 d * nb_row, j * nb_row,
                                 matrix, tile_size)
    return matrix
def test_case(n, tile, debug=False):
    adj_mat = generate_adj_matrix(n)
    print("Running Naive Floyd-Warshall on n x n, n =", n)
    start_time = timeit.default_timer()
    dist_naive = floyd_warshall(adj_mat)
    elapsed = timeit.default_timer() - start_time
    print("Finished, took", elapsed, "seconds")
    print("Running Tiled Floyd-Warshall on same n x n matrix, n =", n, ", tile_size =", tile)
    start_time = timeit.default_timer()
    dist_tiled = tiled_floyd_warshall(adj_mat, tile)
    elapsed = timeit.default_timer() - start_time
    print("Finished, took", elapsed, "seconds")
    print("Correctness Info:")
    for i in range(n):
        for j in range(n):
            if dist_naive[i][j] != dist_tiled[i][j]:
                print("Error, elements (", i, ",", j, ") differ")
                if debug:
                    print("Dumping distance naive:")
                    pprint(dist_naive)
                    print("Dumping distance tiled:")
                    pprint(dist_tiled)
                return False
    print("Correctness Check Passed!!")
    if debug:
        print("Dumping distance naive:")
        pprint(dist_naive)
        print("Dumping distance tiled:")
        pprint(dist_tiled)
    return True
def main():
    global N
    global tile_size
    global global_debug
    wiki_matrix = [
        [0, MAXINT, -2, MAXINT],
        [4, 0, 3, MAXINT],
        [MAXINT, MAXINT, 0, 2],
        [MAXINT, -1, MAXINT, 0]
    ]
    block_size = 2
    print("****WIKI MATRIX TESTING****")
    pad_matrix(wiki_matrix, block_size)
    print("Initial Matrix:")
    pprint(wiki_matrix)
    print("Solved with normal Floyd-Warshall:")
    pprint(floyd_warshall(wiki_matrix))
    print("Solved with tiled:")
    pprint(tiled_floyd_warshall(wiki_matrix, block_size))
    print("****RANDOMLY GENERATED MATRIX****")
    test_status = test_case(N, tile_size, debug=global_debug)
if __name__ == '__main__':
    main()