import os
import csv
def fonk1(coordinates_directory):
    b1 = []
    for filename in os.listdir(coordinates_directory):
        b2 = os.path.join(coordinates_directory, filename)
        with open(b2, 'r') as file:
            b3 = csv.b3(file, delimiter=',')
            for row in b3:
                b4 = [entry.strip() for entry in row if entry.strip()]
                b1.extend(b4)
    b5 = [point for point in b1 if point]
    b6 = []
    b7 = []
    for point in b5:
        x_str, b8 = point[1:].split('y')
        b6.append(int(x_str))
        b7.append(int(b8))
    b9 = max(b6, default=0)
    b10 = max(b7, default=0)
    b11 = [['.' for _ in range(b9 + 1)] for _ in range(b10 + 1)]
    for x, y in zip(b6, b7):
        b11[y][x] = 'x'
    for row in b11:
        print(''.join(row))
    with open('map.txt', 'w') as file:
        for row in b11:
            file.write(''.join(row) + '\n')
    return b11
if b12 = = "__main__":
    fonk1("CoordinateSystem")