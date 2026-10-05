from math import sqrt
def calculate_distance(x1, y1, x2, y2):
    dx_sq = (x1 - x2) ** 2
    dy_sq = (y1 - y2) ** 2
    distance = sqrt(dx_sq + dy_sq)
    return distance
def calculate_heuristic_values(end_point, coordinates):
    end_x, end_y = coordinates[end_point]
    heuristic_values = []
    for point_x, point_y in coordinates:
        distance = calculate_distance(end_x, end_y, point_x, point_y)
        heuristic_values.append(distance)
    return heuristic_values
def calculate_connection_distances(coordinates, connection_list):
    connection_distances = []
    for i, connections in enumerate(connection_list):
        distances_from_current_point = []
        for connection in connections:
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[connection]
            distance = calculate_distance(x1, y1, x2, y2)
            distances_from_current_point.append(distance)
        connection_distances.append(distances_from_current_point)
    return connection_distances
coordinates = [(0, 0), (3, 4), (6, 8)]
connection_list = [[1], [0, 2], [1]]
end_point = 0
print("Heuristic values:", calculate_heuristic_values(end_point, coordinates))
print("Connection distances:", calculate_connection_distances(coordinates, connection_list))