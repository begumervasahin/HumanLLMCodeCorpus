def generate_kruskal_input(matrix):
    with open('kruskal.txt', 'w') as output_file:
        for row in range(len(matrix)):
            for col in range(row + 1, len(matrix[row])):
                weight = matrix[row][col]
                if weight != 0:
                    output_file.write(f'{row} {col} {weight}\n')
def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        size = len(lines)
        matrix = [[0 for _ in range(size)] for _ in range(size)]
        for i, line in enumerate(lines):
            values = list(map(int, line.split()))
            matrix[i] = values
    return matrix
if __name__ == '__main__':
    adjacency_matrix = read_matrix_from_file('matrix.txt')
    generate_kruskal_input(adjacency_matrix)