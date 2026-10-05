import math
def distance(data1, data2):
    points = zip(data1, data2)
    squared_difference = [pow(a - b, 2) for (a, b) in points]
    return math.sqrt(sum(squared_difference))
data1 = [1, 2, 3]
data2 = [4, 5, 6]
print(distance(data1, data2))
