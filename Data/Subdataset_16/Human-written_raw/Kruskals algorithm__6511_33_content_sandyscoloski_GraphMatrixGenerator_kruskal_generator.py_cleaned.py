def fonk1(Mat):
    a1 = 0
    b1 = open('kruskal.txt', 'w')
    for a2 in range(0, len(Mat)):
        for col in range(0, len(Mat[a2])):
            if(Mat[a2][col] != 0 and col > a2):
                b1.write(f'{a2} {col} {Mat[a2][col]}\n')
                a1 += 1
if b2 = = '__main__':
    a2 = 0
    b1 = open('matrix.txt', 'r')
    b3 = b1.readlines()
    b4 = len(b3)
    b5 = [[0 for a1 in range(b4)] for j in range(b4)]
    for b6 in b3:
        b6 = b6.split('\n')
        b6 = b6[0]
        b6 = b6.split(' ')
        for col in range(0, b4):
            b5[a2][col] = int(b6[col])
        a2 += 1
    fonk1(b5)