from math import sqrt
def calculate_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
def heuristic_value(end_point, coordinates):
    end_x, end_y = coordinates[end_point]
    distances = []
    for x, y in coordinates:
        distance = calculate_distance(end_x, end_y, x, y)
        distances.append(distance)
    return distances
def calculate_connections(coordinates, connection_list):
    connection_distances = []
    for i, connections in enumerate(connection_list):
        distances = []
        for j in connections:
            distance = calculate_distance(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1])
            distances.append(distance)
        connection_distances.append(distances)
    return connection_distances
coordinates = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4)
]
connection_list = [
    [1, 2],
    [0, 2, 3],
    [0, 1, 3, 4],
    [1, 2, 4],
    [2, 3]
]
end_point = 4
heuristic_values = heuristic_value(end_point, coordinates)
print("Heuristic Values:", heuristic_values)
connection_distances = calculate_connections(coordinates, connection_list)
print("Connection Distances:", connection_distances)