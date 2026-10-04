import math
def euclidean_distance(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))
if __name__ == "__main__":
    point1 = [1.0, 2.0, 3.0]
    point2 = [4.0, 5.0, 6.0]
    distance = euclidean_distance(point1, point2)
    print(f"The Euclidean distance between {point1} and {point2} is {distance:.2f}")