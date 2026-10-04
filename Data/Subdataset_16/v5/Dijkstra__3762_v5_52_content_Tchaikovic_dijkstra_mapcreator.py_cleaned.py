import os
import csv
def fonk1(coordinates_directory):
    b1 = []
    for filename in os.listdir(coordinates_directory):
        b2 = os.path.join(coordinates_directory, filename)
        with open(b2, 'r') as file:
            b3 = csv.b3(file, delimiter=',')
            for row in b3:
                b1.extend(entry.strip() for entry in row if entry.strip())
    x_coords, b4 = [], []
    for point in b1:
        x_str, b5 = point[1:].split('y')
        x_coords.append(int(x_str))
        b4.append(int(b5))
    b6 = max(x_coords, default=0)
    b7 = max(b4, default=0)
    b8 = [['.' for _ in range(b6 + 1)] for _ in range(b7 + 1)]
    for x, y in zip(x_coords, b4):
        b8[y][x] = 'x'
    for row in b8:
        print(''.join(row))
    with open('map.txt', 'w') as file:
        for row in b8:
            file.write(''.join(row) + '\n')
    return b8
if b9 = = "__main__":
    fonk1("CoordinateSystem")