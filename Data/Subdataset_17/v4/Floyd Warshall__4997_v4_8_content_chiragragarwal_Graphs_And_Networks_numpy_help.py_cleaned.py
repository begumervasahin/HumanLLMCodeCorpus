import numpy as np
def main():
    matrix_str = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
    formatted_str = matrix_str.replace(';', '\n')
    matrix = np.matrix(formatted_str)
    print("Matrix shape:", matrix.shape)
    print("Element at position (0, 1):", matrix[0, 1])
    print("Element at position (2, 3):", matrix[2, 3])
    matrix[0, 1] = -8
    print("Modified row 1:", matrix[1])
    print("Column 1:", matrix[:, 1])
if __name__ == '__main__':
    main()