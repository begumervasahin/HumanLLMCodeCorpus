import math
def euclidean_distance(point1, point2):
    squared_difference = [(a - b) ** 2 for a, b in zip(point1, point2)]
    return math.sqrt(sum(squared_difference))
if __name__ == "__main__":
    point1 = [1, 2, 3]
    point2 = [4, 5, 6]
    distance = euclidean_distance(point1, point2)
    print(f"The Euclidean distance between {point1} and {point2} is {distance:.2f}")