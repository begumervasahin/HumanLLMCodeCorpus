import statistics
import time
def db_to_list(filename):
    with open(filename, "r") as file:
        return [(float(x[0]), float(x[1])) for x in (line.split(",") for line in file)]
def create_paths_for_quadrant(quadrant, filename):
    with open(filename, "w") as file:
        num_points = len(quadrant)
        for i, point in enumerate(quadrant):
            connections = []
            for j in range(1, num_points
                for direction in [-1, 1]:
                    neighbor_index = (i + j * direction) % num_points
                    neighbor = quadrant[neighbor_index]
                    distance = ((neighbor[0] - point[0]) ** 2 + (neighbor[1] - point[1]) ** 2) ** 0.5
                    connections.append((neighbor, distance))
            connections.sort(key=lambda x: x[1])
            closest_points = " ".join(f"{x[0][0]},{x[0][1]}" for x in connections[:10])
            file.write(f"{point[0]},{point[1]} {closest_points}\n")
def separate_lists(points):
    sorted_by_x = sorted(points, key=lambda p: p[0])
    x_values = [p[0] for p in sorted_by_x]
    y_values = [p[1] for p in points]
    return x_values, y_values
def create_quadrants(points):
    x_values, y_values = separate_lists(points)
    x_median = statistics.median(x_values)
    y_median = statistics.median(y_values)
    q1, q2, q3, q4 = [], [], [], []
    for x, y in points:
        if x <= x_median and y >= y_median:
            q1.append((x, y))
        elif x > x_median and y >= y_median:
            q2.append((x, y))
        elif x <= x_median and y < y_median:
            q3.append((x, y))
        else:
            q4.append((x, y))
    return q1, q2, q3, q4, x_median, y_median
filename = "data.csv"
quadrant_data = db_to_list(filename)
quadrants = create_quadrants(quadrant_data)
for idx, quadrant in enumerate(quadrants[:4], 1):
    output_file = f"quadrant_{idx}_paths.txt"
    create_paths_for_quadrant(quadrant, output_file)