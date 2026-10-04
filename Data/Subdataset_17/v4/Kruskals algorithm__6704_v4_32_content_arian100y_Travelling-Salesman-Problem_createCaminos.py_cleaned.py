import statistics
from operator import itemgetter
import time
def db_to_list(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            x, y = map(float, line.split(","))
            data.append((x, y))
    return data
def create_graph_edges(quadrant, output_filename):
    with open(output_filename, "w") as file:
        num_points = len(quadrant)
        for index, point in enumerate(quadrant):
            x, y = point
            connections = []
            for j in range(1, (num_points
                neighbors = [
                    (index + j) % num_points,
                    (index - j) % num_points
                ]
                for neighbor in neighbors:
                    nx, ny = quadrant[neighbor]
                    distance = ((nx - x) ** 2 + (ny - y) ** 2) ** 0.5
                    connections.append((nx, ny, distance))
            connections.sort(key=itemgetter(2))
            closest_points = connections[:10]
            result_line = f"{x},{y} " + " ".join(f"{cx},{cy}" for cx, cy, _ in closest_points)
            file.write(result_line + "\n")
def separate_coordinates(data):
    x_values = [point[0] for point in data]
    y_values = [point[1] for point in data]
    return x_values, y_values
def create_quadrants(data):
    x_values, y_values = separate_coordinates(data)
    x_median = statistics.median(x_values)
    y_median = statistics.median(y_values)
    q1, q2, q3, q4 = [], [], [], []
    for point in data:
        x, y = point
        if x <= x_median and y >= y_median:
            q1.append(point)
        elif x > x_median and y >= y_median:
            q2.append(point)
        elif x <= x_median and y < y_median:
            q3.append(point)
        else:
            q4.append(point)
    return q1, q2, q3, q4, x_median, y_median
