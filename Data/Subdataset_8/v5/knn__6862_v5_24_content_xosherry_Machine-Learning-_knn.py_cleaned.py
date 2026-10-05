import sys
import math
def euclidean_distance(point1, point2):
    return math.sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)))
def read_points(file_name):
    with open(file_name, 'r') as file:
        total, dimensions = map(int, file.readline().split())
        points = [[float(val) for val in line.split()] for line in file]
    return total, dimensions, points
def knn(k, training_file, testing_file):
    train_total, train_dimensions, training_points = read_points(training_file)
    test_total, test_dimensions, testing_points = read_points(testing_file)
    for test_point in testing_points:
        distances = [(euclidean_distance(train_point[:-1], test_point), train_point[-1]) for train_point in training_points]
        k_nearest = sorted(distances)[:k]
        class_counts = {}
        for distance, label in k_nearest:
            class_counts[label] = class_counts.get(label, 0) + 1
        most_popular_classes = [label for label, count in class_counts.items() if count == max(class_counts.values())]
        if len(most_popular_classes) == 1:
            test_point.append(most_popular_classes[0])
        else:
            tiebreaker = sorted([x for x in k_nearest if x[1] in most_popular_classes])
            test_point.append(tiebreaker[0][1] if tiebreaker[0][1] < tiebreaker[1][1] else tiebreaker[1][1])
    for i, item in enumerate(testing_points, 1):
        print(f"{i}. {' '.join(f'{val:.1f}' for val in item[:-1])} -- {item[-1]}")
knn(int(sys.argv[1]), sys.argv[2], sys.argv[3])