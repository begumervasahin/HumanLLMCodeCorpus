import os
import csv
def parse_and_create_map(coordinates_directory):
    points = []
    for filename in os.listdir(coordinates_directory):
        with open(os.path.join(coordinates_directory, filename), 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                line = [coordinate.strip() for coordinate in line]
                points.extend(line)
    filtered_points = filter(lambda a: a != '', points)
    points_matrix = [[0 for _ in range(len(filtered_points))] for _ in range(2)]
    for i in range(len(filtered_points)):
        x, y = map(int, filtered_points[i][1:].split("y"))
        points_matrix[0][i] = x
        points_matrix[1][i] = y
    max_x = max(points_matrix[0]) + 1
    max_y = max(points_matrix[1]) + 1
    map_output = [['.' for _ in range(max_x)] for _ in range(max_y)]
    for i in range(len(points_matrix[0])):
        map_output[points_matrix[1][i]][points_matrix[0][i]] = 'x'
    with open('map.txt', 'w') as map_file:
        for row in map_output:
            map_file.write(''.join(row) + '\n')
    return map_output
parse_and_create_map("CoordinateSystem")