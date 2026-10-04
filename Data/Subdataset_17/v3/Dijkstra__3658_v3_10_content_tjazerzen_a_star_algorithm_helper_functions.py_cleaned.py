from math import sqrt
from typing import List, Tuple
Coordinates = List[Tuple[float, float]]
Connections = List[List[int]]
Distances = List[List[float]]
def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
def heuristic_value(end_point: int, coordinates: Coordinates) -> List[float]:
    end_x, end_y = coordinates[end_point]
    return [calculate_distance(end_x, end_y, x, y) for x, y in coordinates]
def calculate_connections(coordinates: Coordinates, connection_list: Connections) -> Distances:
    connection_distances = []
    for i, connections in enumerate(connection_list):
        distances = [calculate_distance(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1])
                     for j in connections]
        connection_distances.append(distances)
    return connection_distances
coordinates: Coordinates = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4)
]
connection_list: Connections = [
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