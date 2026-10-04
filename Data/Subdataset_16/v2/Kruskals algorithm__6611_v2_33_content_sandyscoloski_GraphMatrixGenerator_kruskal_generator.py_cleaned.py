def fonk1(b4, b1 = 'kruskal.txt'):
    with open(b1, 'w') as file:
        b2 = len(b4)
        for i in range(b2):
            for j in range(i + 1, b2):
                if b4[i][j] != 0:
                    file.write(f'{i} {j} {b4[i][j]}\n')
def fonk2(file_name):
    with open(file_name, 'r') as file:
        b3 = file.readlines()
    b2 = len(b3)
    b4 = []
    for line in b3:
        b5 = list(map(int, line.strip().split()))
        b4.append(b5)
    return b4
if b6 = = '__main__':
    b7 = 'b4.txt'
    b8 = fonk2(b7)
    fonk1(b8)