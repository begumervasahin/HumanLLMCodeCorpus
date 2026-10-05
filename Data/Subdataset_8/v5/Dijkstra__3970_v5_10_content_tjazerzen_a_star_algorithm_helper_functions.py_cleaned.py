from math import sqrt
def calculate_distance(x1, y1, x2, y2):
    delta_x = x2 - x1
    delta_y = y2 - y1
    distance = sqrt(delta_x ** 2 + delta_y ** 2)
    return distance
def calculate_heuristic_values(end_point, coordinates):
    end_x, end_y = coordinates[end_point]
    heuristic_values = []
    for point_x, point_y in coordinates:
        distance = calculate_distance(end_x, end_y, point_x, point_y)
        heuristic_values.append(distance)
    return heuristic_values
def calculate_connection_distances(coordinates, connection_list):
    distances = []
    for i, connections in enumerate(connection_list):
        point_distances = []
        for connection in connections:
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[connection]
            distance = calculate_distance(x1, y1, x2, y2)
            point_distances.append(distance)
        distances.append(point_distances)
    return distances
coordinates = [(0, 0), (3, 4), (6, 8)]
connection_list = [[1], [0, 2], [1]]
end_point = 0
print("Heuristic values:", calculate_heuristic_values(end_point, coordinates))
print("Connection distances:", calculate_connection_distances(coordinates, connection_list))