import math
def euclidean_distance(data1, data2):
    squared_diffs = [(a - b) ** 2 for a, b in zip(data1, data2)]
    return math.sqrt(sum(squared_diffs))
data1 = [1, 2, 3]
data2 = [4, 5, 6]
print(euclidean_distance(data1, data2))
