def kruskal_gen(matrix):
    with open('kruskal.txt', 'w') as file:
        for lin in range(len(matrix)):
            for col in range(len(matrix[lin])):
                if matrix[lin][col] != 0 and col > lin:
                    file.write(f'{lin} {col} {matrix[lin][col]}\n')
if __name__ == '__main__':
    with open('matrix.txt', 'r') as arquivo:
        lines = arquivo.readlines()
    size = len(lines)
    mat = [[0 for _ in range(size)] for _ in range(size)]
    for lin, line in enumerate(lines):
        values = line.strip().split()
        for col in range(size):
            mat[lin][col] = int(values[col])
    kruskal_gen(mat)