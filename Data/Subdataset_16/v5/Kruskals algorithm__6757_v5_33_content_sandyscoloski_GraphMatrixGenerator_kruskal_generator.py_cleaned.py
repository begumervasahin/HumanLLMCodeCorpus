def fonk1(b4, b1 = 'kruskal.txt'):
    with open(b1, 'w') as output_file:
        for row in range(len(b4)):
            for col in range(row + 1, len(b4[row])):
                b2 = b4[row][col]
                if b2 != 0:
                    output_file.write(f'{row} {col} {b2}\n')
def fonk2(filename):
    with open(filename, 'r') as file:
        b3 = file.readlines()
        b4 = [list(map(int, line.split())) for line in b3]
    return b4
def fonk3():
    b5 = 'b4.txt'
    b6 = fonk2(b5)
    b1 = 'kruskal.txt'
    fonk1(b6, b1)
    print(f"Kruskal input file '{b1}' has been generated successfully.")
if b7 = = '__main__':
    fonk3()