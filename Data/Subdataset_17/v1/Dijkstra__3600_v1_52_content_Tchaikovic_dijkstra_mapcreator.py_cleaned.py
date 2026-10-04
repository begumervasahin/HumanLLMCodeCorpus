import os
import csv
def parse_and_create_map(coordinates_directory):
    points = []
    for filename in os.listdir(coordinates_directory):
        filepath = os.path.join(coordinates_directory, filename)
        with open(filepath, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for line in reader:
                line = [x.strip() for x in line]
                points.extend(line)
    filtered = list(filter(lambda a: a != '', points))
    points_matrix = [[0 for _ in range(len(filtered))] for _ in range(2)]
    for i, point in enumerate(filtered):
        x, y = point[1:].split('y')
        points_matrix[0][i] = int(x)
        points_matrix[1][i] = int(y)
    max_x = max(points_matrix[0])
    max_y = max(points_matrix[1])
    map_ = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for i in range(len(points_matrix[0])):
        x = points_matrix[0][i]
        y = points_matrix[1][i]
        map_[y][x] = 'x'
    for row in map_:
        print(''.join(row))
    with open('map.txt', 'w') as thefile:
        for row in map_:
            thefile.write(''.join(row) + '\n')
    return map_
if __name__ == "__main__":
    parse_and_create_map("CoordinateSystem")