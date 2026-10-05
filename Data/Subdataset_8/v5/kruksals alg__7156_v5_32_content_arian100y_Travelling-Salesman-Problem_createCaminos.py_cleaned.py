from operator import itemgetter
import statistics
import time as ti
timer = ti.clock()
def db_to_list(filename):
    data_list = []
    with open(filename, "r") as file:
        for line in file:
            values = line.split(",")
            data_list.append((float(values[0]), float(values[1])))
    return data_list
def create_nearby_paths(quadrant, filename):
    with open(filename, "w") as file:
        n = len(quadrant)
        for u in quadrant:
            nearby_points = set()
            for j in range(1, int(len(quadrant) / 2) + 1):
                v1 = (quadrant.index(u) + j) % len(quadrant)
                v2 = (quadrant.index(u) - j) % len(quadrant)
                x_v1, y_v1 = quadrant[v1][0], quadrant[v1][1]
                d1 = ((x_v1 - u[0]) ** 2 + (y_v1 - u[1]) ** 2) ** 0.5
                x_v2, y_v2 = quadrant[v2][0], quadrant[v2][1]
                d2 = ((x_v2 - u[0]) ** 2 + (y_v2 - u[1]) ** 2) ** 0.5
                nearby_points.add((v1, x_v1, y_v1, d1))
                nearby_points.add((v2, x_v2, y_v2, d2))
            nearby_points = sorted(nearby_points, key=itemgetter(3))[:10]
            nearby_paths = " ".join([f"{point[1]},{point[2]}" for point in nearby_points])
            file.write(f"{u[0]},{u[1]} {nearby_paths}\n")
def separate_lists(data_list):
    y_values = [point[1] for point in data_list]
    x_values = [point[0] for point in sorted(data_list, key=itemgetter(0))]
    return x_values, y_values
def create_quadrants(data_list):
    x_values, y_values = separate_lists(data_list)
    y_median = statistics.median(y_values)
    x_median = statistics.median(x_values)
    print("Median values:", x_median, y_median)
    q1, q2, q3, q4 = [], [], [], []
    for point in data_list:
        x, y = point
        if x <= x_median and y >= y_median:
            q1.append(point)
        elif x > x_median and y >= y_median:
            q2.append(point)
        elif x <= x_median and y < y_median:
            q3.append(point)
        elif x > x_median and y < y_median:
            q4.append(point)
    return q1, q2, q3, q4, x_median, y_median