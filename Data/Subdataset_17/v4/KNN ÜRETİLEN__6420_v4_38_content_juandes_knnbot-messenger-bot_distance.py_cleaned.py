import math
def distance(data1, data2):
    paired_points = zip(data1, data2)
    squared_differences = [(a - b) ** 2 for a, b in paired_points]
    return math.sqrt(sum(squared_differences))
point1 = [2, 3, 4]
point2 = [5, 6, 7]
print("Distance:", distance(point1, point2))