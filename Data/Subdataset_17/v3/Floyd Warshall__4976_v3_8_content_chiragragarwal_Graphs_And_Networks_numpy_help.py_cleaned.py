import numpy as np
def create_matrix_from_string(matrix_str):
    formatted_str = matrix_str.replace(';', '\n')
    return np.matrix(formatted_str)
def main():
    matrix_str = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
    matrix = create_matrix_from_string(matrix_str)
    print(f"Matrix shape: {matrix.shape}")
    print(f"Element at position (0, 1): {matrix[0, 1]}")
    print(f"Element at position (2, 3): {matrix[2, 3]}")
    matrix[0, 1] = -8
    print(f"Modified row 1: {matrix[1]}")
    print(f"Column 1: {matrix[:, 1]}")
if __name__ == '__main__':
    main()