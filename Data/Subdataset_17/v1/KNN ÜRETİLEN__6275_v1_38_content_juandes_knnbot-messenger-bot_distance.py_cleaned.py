import math
def distance(data1, data2):
    points = zip(data1, data2)
    squared_difference = [pow(a - b, 2) for (a, b) in points]
    return math.sqrt(sum(squared_difference))
if __name__ == "__main__":
    data_point_1 = [1, 2, 3]
    data_point_2 = [4, 5, 6]
    result = distance(data_point_1, data_point_2)
    print(f"The distance between {data_point_1} and {data_point_2} is {result}")