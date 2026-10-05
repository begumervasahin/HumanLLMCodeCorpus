import math
def calculate_distance(data1, data2):
    squared_difference = [(a - b) ** 2 for a, b in zip(data1, data2)]
    distance = math.sqrt(sum(squared_difference))
    return distance