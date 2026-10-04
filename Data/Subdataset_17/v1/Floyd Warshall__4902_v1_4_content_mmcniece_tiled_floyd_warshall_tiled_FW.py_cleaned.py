import random
import timeit
from pprint import pprint
from copy import deepcopy
MAXINT = 100000000
N = 9
TILE_SIZE = 3
NEGATIVE_EDGES = True
def generate_adj_matrix(dim, connectivity=0.5):
    matrix = [[0] * dim for _ in range(dim)]
    lower_bound_weight = -1 if NEGATIVE_EDGES else 1
    for _ in range(int(connectivity * (dim ** 2))):
        rand_row = random.randint(0, dim - 1)
        rand_col = random.randint(0, dim - 1)
        if rand_row != rand_col:
            rand_weight = random.randint(lower_bound_weight, 20)
            matrix[rand_row][rand_col] = rand_weight
    for i in range(dim):
        for j in range(dim):
            if i != j and matrix[i][j] == 0:
                matrix[i][j] = MAXINT
    return matrix
def floyd_warshall(graph):
    dist = deepcopy(graph)
    N = len(graph)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
def pad_matrix(matrix, tile_size):
    dim_to_add = tile_size - (len(matrix) % tile_size)
    total_dim = len(matrix) + dim_to_add
    for row in matrix:
        row.extend([MAXINT] * dim_to_add)
    for _ in range(dim_to_add):
        matrix.append([MAXINT] * total_dim)
    return matrix
def update_submatrix(a_row, a_col, b_row, b_col, c_row, c_col, matrix, block_size, debug=False):
    for k in range(block_size):
        for i in range(block_size):
            for j in range(block_size):
                matrix[a_row + i][a_col + j] = min(
                    matrix[a_row + i][a_col + j],
                    matrix[b_row + i][b_col + k] + matrix[c_row + k][c_col + j]
                )
                if debug:
                    print(f"Ai, Aj ({a_row + i}, {a_col + j}) Bi, Bk ({b_row + i}, {b_col + k}) Ck, Cj ({c_row + k}, {c_col + j})")
    return matrix
def tiled_fw(matrix, tile_size):
    matrix = pad_matrix(matrix, tile_size)
    num_tiles_row = len(matrix)
    for d in range(num_tiles_row):
        update_submatrix(d*tile_size, d*tile_size, d*tile_size, d*tile_size, d*tile_size, d*tile_size, matrix, tile_size)
        for j in range(num_tiles_row):
            if j != d:
                update_submatrix(d*tile_size, j*tile_size, d*tile_size, d*tile_size, d*tile_size, j*tile_size, matrix, tile_size)
        for i in range(num_tiles_row):
            if i != d:
                update_submatrix(i*tile_size, d*tile_size, i*tile_size, d*tile_size, d*tile_size, d*tile_size, matrix, tile_size)
        for i in range(num_tiles_row):
            for j in range(num_tiles_row):
                if i != d and j != d:
                    update_submatrix(i*tile_size, j*tile_size, i*tile_size, d*tile_size, d*tile_size, j*tile_size, matrix, tile_size)
    return matrix
def test_case(n, tile, debug=False):
    adj_mat = generate_adj_matrix(n)
    print(f"Running Naive FW on {n} x {n}, n = {n}")
    start_time = timeit.default_timer()
    dist_naive = floyd_warshall(adj_mat)
    elapsed = timeit.default_timer() - start_time
    print(f"Finished, took {elapsed} seconds")
    print(f"Running Tiled FW on same {n} x {n} matrix, n = {n}, tile_size = {tile}")
    start_time = timeit.default_timer()
    dist_tiled = tiled_fw(adj_mat, tile)
    elapsed = timeit.default_timer() - start_time
    print(f"Finished, took {elapsed} seconds")
    print("Correctness Info:")
    for i in range(n):
        for j in range(n):
            if dist_naive[i][j] != dist_tiled[i][j]:
                print(f"Error, elements ({i}, {j}) differ")
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
    wiki_matrix = [
        [0, MAXINT, -2, MAXINT],
        [4, 0, 3, MAXINT],
        [MAXINT, MAXINT, 0, 2],
        [MAXINT, -1, MAXINT, 0]
    ]
    block_size = 2
    print("****WIKI MATRIX TESTING****")
    padded_matrix = pad_matrix(wiki_matrix, block_size)
    print("Initial Matrix:")
    pprint(padded_matrix)
    print("Solved with normal FW:")
    pprint(floyd_warshall(padded_matrix))
    print("Solved with tiled FW:")
    pprint(tiled_fw(padded_matrix, block_size))
    print("****RAND GENERATED MATRIX****")
    test_status = test_case(N, TILE_SIZE)
    print(f"Test status: {'Passed' if test_status else 'Failed'}")
if __name__ == '__main__':
    main()