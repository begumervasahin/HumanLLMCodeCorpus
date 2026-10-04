from math import sqrt
from typing import List, Tuple
b1 = List[Tuple[float, float]]
b2 = List[List[int]]
b3 = List[List[float]]
def fonk1(x1: float, y1: float, x2: float, y2: float) -> float:
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
def fonk2(a1: int, coordinates: b1) -> List[float]:
    end_x, b4 = coordinates[a1]
    return [fonk1(end_x, b4, x, y) for x, y in coordinates]
def fonk3(coordinates: b1, connection_list: b2) -> b3:
    b5 = []
    for i, connections in enumerate(connection_list):
        b6 = [fonk1(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1])
                     for j in connections]
        b5.append(b6)
    return b5
coordinates: b1 = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4)
]
connection_list: b2 = [
    [1, 2],
    [0, 2, 3],
    [0, 1, 3, 4],
    [1, 2, 4],
    [2, 3]
]
a1 = 4
b7 = fonk2(a1, coordinates)
print("Heuristic Values:", b7)
b5 = fonk3(coordinates, connection_list)
print("Connection b3:", b5)