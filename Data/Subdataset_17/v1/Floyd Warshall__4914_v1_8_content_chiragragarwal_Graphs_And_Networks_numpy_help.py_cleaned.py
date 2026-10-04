import numpy as np
def main():
    mat_str = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
    mat_str = mat_str.replace(';', '\n')
    graph_mat = np.matrix(mat_str)
    print(f"Matrix shape: {graph_mat.shape}")
    print(f"Element at position (0, 1): {graph_mat[0, 1]}")
    print(f"Element at position (2, 3): {graph_mat[2, 3]}")
    graph_mat[0, 1] = -8
    print(f"Modified row 1: {graph_mat[1]}")
    print(f"Column 1: {graph_mat[:, 1]}")
if __name__ == '__main__':
    main()