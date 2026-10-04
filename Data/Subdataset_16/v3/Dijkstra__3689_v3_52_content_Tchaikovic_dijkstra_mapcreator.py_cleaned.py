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
    x_coords, b5 = zip(*[
        (int(x_str), int(y_str))
        for point in b1
        if 'y' in point
        for x_str, y_str in [point[1:].split('y')]
    ]) if b1 else ([], [])
    b6 = max(x_coords, default=0)
    b7 = max(b5, default=0)
    b8 = [['.' for _ in range(b6 + 1)] for _ in range(b7 + 1)]
    for x, y in zip(x_coords, b5):
        b8[y][x] = 'x'
    for row in b8:
        print(''.join(row))
    with open('map.txt', 'w') as file:
        for row in b8:
            file.write(''.join(row) + '\n')
    return b8
if b9 = = "__main__":
    b10 = fonk1("CoordinateSystem")