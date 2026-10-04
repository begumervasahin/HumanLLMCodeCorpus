import os
import csv
def fonk1(coordinates_directory):
    b1 = []
    for filename in os.listdir(coordinates_directory):
        b2 = os.path.join(coordinates_directory, filename)
        with open(b2, 'r') as f:
            b3 = csv.b3(f, delimiter=',')
            for b4 in b3:
                b4 = [b11.strip() for b11 in b4]
                b1.extend(b4)
    b5 = list(filter(lambda a: a != '', b1))
    b6 = [[0 for _ in range(len(b5))] for _ in range(2)]
    for i, point in enumerate(b5):
        b11, b7 = point[1:].split('b7')
        b6[0][i] = int(b11)
        b6[1][i] = int(b7)
    b8 = max(b6[0])
    b9 = max(b6[1])
    b10 = [['.' for _ in range(b8 + 1)] for _ in range(b9 + 1)]
    for i in range(len(b6[0])):
        b11 = b6[0][i]
        b7 = b6[1][i]
        b10[b7][b11] = 'b11'
    for row in b10:
        print(''.join(row))
    with open('map.txt', 'w') as thefile:
        for row in b10:
            thefile.write(''.join(row) + '\n')
    return b10
if b12 = = "__main__":
    fonk1("CoordinateSystem")