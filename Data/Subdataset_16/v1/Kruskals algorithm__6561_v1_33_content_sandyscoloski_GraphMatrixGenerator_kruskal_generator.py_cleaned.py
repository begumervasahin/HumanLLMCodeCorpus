def fonk1(matrix):
    with open('kruskal.txt', 'w') as file:
        for lin in range(len(matrix)):
            for col in range(len(matrix[lin])):
                if matrix[lin][col] != 0 and col > lin:
                    file.write(f'{lin} {col} {matrix[lin][col]}\n')
if b1 = = '__main__':
    with open('matrix.txt', 'r') as arquivo:
        b2 = arquivo.readlines()
    b3 = len(b2)
    b4 = [[0 for _ in range(b3)] for _ in range(b3)]
    for lin, line in enumerate(b2):
        b5 = line.strip().split()
        for col in range(b3):
            b4[lin][col] = int(b5[col])
    fonk1(b4)