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
    b5 = []
    b6 = []
    for point in b1:
        if 'y' in point:
            x_str, b7 = point[1:].split('y')
            b5.append(int(x_str))
            b6.append(int(b7))
    b8 = max(b5, default=0)
    b9 = max(b6, default=0)
    b10 = [['.' for _ in range(b8 + 1)] for _ in range(b9 + 1)]
    for x, y in zip(b5, b6):
        b10[y][x] = 'x'
    for row in b10:
        print(''.join(row))
    with open('map.txt', 'w') as file:
        for row in b10:
            file.write(''.join(row) + '\n')
    return b10
if b11 = = "__main__":
    fonk1("CoordinateSystem")