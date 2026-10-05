import math
def calculate_distance(data1, data2):
    points = zip(data1, data2)
    squared_difference = [pow(a - b, 2) for (a, b) in points]
    distance = math.sqrt(sum(squared_difference))
    return distance