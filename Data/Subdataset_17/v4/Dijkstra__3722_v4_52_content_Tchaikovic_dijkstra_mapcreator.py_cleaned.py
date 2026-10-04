import os
import csv
def parse_and_create_map(coordinates_directory):
    points = []
    for filename in os.listdir(coordinates_directory):
        filepath = os.path.join(coordinates_directory, filename)
        with open(filepath, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                cleaned_row = [entry.strip() for entry in row if entry.strip()]
                points.extend(cleaned_row)
    filtered_points = [point for point in points if point]
    x_coords = []
    y_coords = []
    for point in filtered_points:
        x_str, y_str = point[1:].split('y')
        x_coords.append(int(x_str))
        y_coords.append(int(y_str))
    max_x = max(x_coords, default=0)
    max_y = max(y_coords, default=0)
    map_ = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y in zip(x_coords, y_coords):
        map_[y][x] = 'x'
    for row in map_:
        print(''.join(row))
    with open('map.txt', 'w') as file:
        for row in map_:
            file.write(''.join(row) + '\n')
    return map_
if __name__ == "__main__":
    parse_and_create_map("CoordinateSystem")