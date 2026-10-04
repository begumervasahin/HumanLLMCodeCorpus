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
    b4 = [list(map(int, line.strip().split())) for line in b3]
    return b4
def fonk3():
    b5 = 'b4.txt'
    b6 = fonk2(b5)
    fonk1(b6)
if b7 = = '__main__':
    fonk3()