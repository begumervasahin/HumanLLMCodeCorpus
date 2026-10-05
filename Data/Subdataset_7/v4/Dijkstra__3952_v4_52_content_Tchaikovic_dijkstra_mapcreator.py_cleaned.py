import os
import csv
def fonk1(coordinates_directory):
    b1 = []
    for filename in os.listdir(coordinates_directory):
        with open(os.path.join(coordinates_directory, filename), 'r') as file:
            b2 = csv.b2(file, delimiter=',')
            for b3 in b2:
                b3 = [coordinate.strip() for coordinate in b3]
                b1.extend(b3)
    b4 = filter(lambda a: a != '', b1)
    b5 = [[0 for _ in range(len(b4))] for _ in range(2)]
    for i in range(len(b4)):
        x, b6 = map(int, b4[i][1:].split("b6"))
        b5[0][i] = x
        b5[1][i] = b6
    b7 = max(b5[0]) + 1
    b8 = max(b5[1]) + 1
    b9 = [['.' for _ in range(b7)] for _ in range(b8)]
    for i in range(len(b5[0])):
        b9[b5[1][i]][b5[0][i]] = 'x'
    with open('map.txt', 'w') as map_file:
        for row in b9:
            map_file.write(''.join(row) + '\n')
    return b9
fonk1("CoordinateSystem")