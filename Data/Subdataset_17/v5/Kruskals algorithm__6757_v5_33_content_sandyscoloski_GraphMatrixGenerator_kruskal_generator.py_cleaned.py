def generate_kruskal_input(matrix, output_filename='kruskal.txt'):
    with open(output_filename, 'w') as output_file:
        for row in range(len(matrix)):
            for col in range(row + 1, len(matrix[row])):
                weight = matrix[row][col]
                if weight != 0:
                    output_file.write(f'{row} {col} {weight}\n')
def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        matrix = [list(map(int, line.split())) for line in lines]
    return matrix
def main():
    input_filename = 'matrix.txt'
    adjacency_matrix = read_matrix_from_file(input_filename)
    output_filename = 'kruskal.txt'
    generate_kruskal_input(adjacency_matrix, output_filename)
    print(f"Kruskal input file '{output_filename}' has been generated successfully.")
if __name__ == '__main__':
    main()