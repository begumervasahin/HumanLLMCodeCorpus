def fonk1(b4):
    with open('kruskal.txt', 'w') as output_file:
        for row in range(len(b4)):
            for col in range(row + 1, len(b4[row])):
                b1 = b4[row][col]
                if b1 != 0:
                    output_file.write(f'{row} {col} {b1}\n')
def fonk2(filename):
    with open(filename, 'r') as file:
        b2 = file.readlines()
        b3 = len(b2)
        b4 = [[0 for _ in range(b3)] for _ in range(b3)]
        for i, line in enumerate(b2):
            b5 = list(map(int, line.split()))
            b4[i] = b5
    return b4
if b6 = = '__main__':
    b7 = fonk2('b4.txt')
    fonk1(b7)