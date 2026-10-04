import statistics
def db_to_list(filename):
    with open(filename, "r") as file:
        return [(float(x), float(y)) for line in file for x, y in [line.strip().split(",")]]
def calculate_distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
def find_closest_points(point, quadrant, num_closest=10):
    distances = [(neighbor, calculate_distance(point, neighbor)) for neighbor in quadrant if neighbor != point]
    distances.sort(key=lambda x: x[1])
    return [x[0] for x in distances[:num_closest]]
def write_paths_for_quadrant(quadrant, filename):
    with open(filename, "w") as file:
        for point in quadrant:
            closest_points = find_closest_points(point, quadrant)
            closest_points_str = " ".join(f"{x},{y}" for x, y in closest_points)
            file.write(f"{point[0]},{point[1]} {closest_points_str}\n")
def separate_coordinates(points):
    sorted_by_x = sorted(points, key=lambda p: p[0])
    x_values = [p[0] for p in sorted_by_x]
    y_values = [p[1] for p in points]
    return x_values, y_values
def create_quadrants(points):
    x_values, y_values = separate_coordinates(points)
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
points = db_to_list(filename)
quadrants = create_quadrants(points)[:4]
for idx, quadrant in enumerate(quadrants, 1):
    output_file = f"quadrant_{idx}_paths.txt"
    write_paths_for_quadrant(quadrant, output_file)