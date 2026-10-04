import statistics
from operator import itemgetter
def read_data_from_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            x, y = map(float, line.strip().split(","))
            data.append((x, y))
    return data
def create_graph_edges(quadrant, output_filename, max_connections=10):
    with open(output_filename, "w") as file:
        num_points = len(quadrant)
        for index, (x, y) in enumerate(quadrant):
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
            closest_points = sorted(connections, key=itemgetter(2))[:max_connections]
            result_line = f"{x},{y} " + " ".join(f"{cx},{cy}" for cx, cy, _ in closest_points)
            file.write(result_line + "\n")
def separate_coordinates(data):
    x_values = [x for x, _ in data]
    y_values = [y for _, y in data]
    return x_values, y_values
def create_quadrants(data):
    x_values, y_values = separate_coordinates(data)
    x_median = statistics.median(x_values)
    y_median = statistics.median(y_values)
    q1, q2, q3, q4 = [], [], [], []
    for x, y in data:
        if x <= x_median and y >= y_median:
            q1.append((x, y))
        elif x > x_median and y >= y_median:
            q2.append((x, y))
        elif x <= x_median and y < y_median:
            q3.append((x, y))
        else:
            q4.append((x, y))
    return q1, q2, q3, q4, x_median, y_median
