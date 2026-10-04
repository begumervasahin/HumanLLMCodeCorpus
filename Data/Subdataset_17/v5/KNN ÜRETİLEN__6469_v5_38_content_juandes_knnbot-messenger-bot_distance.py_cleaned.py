import math
def euclidean_distance(data1, data2):
    if len(data1) != len(data2):
        raise ValueError("Data points must have the same number of dimensions.")
    sum_squared_diff = sum((a - b) ** 2 for a, b in zip(data1, data2))
    return math.sqrt(sum_squared_diff)
point1 = [2, 3, 4]
point2 = [5, 6, 7]
print("Distance:", euclidean_distance(point1, point2))