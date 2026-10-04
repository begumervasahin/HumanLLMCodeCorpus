def generate_kruskal_edges(matrix, output_file='kruskal.txt'):
    with open(output_file, 'w') as file:
        size = len(matrix)
        for i in range(size):
            for j in range(i + 1, size):
                if matrix[i][j] != 0:
                    file.write(f'{i} {j} {matrix[i][j]}\n')
def read_adjacency_matrix(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    size = len(lines)
    matrix = []
    for line in lines:
        row = list(map(int, line.strip().split()))
        matrix.append(row)
    return matrix
if __name__ == '__main__':
    matrix_file = 'matrix.txt'
    adjacency_matrix = read_adjacency_matrix(matrix_file)
    generate_kruskal_edges(adjacency_matrix)