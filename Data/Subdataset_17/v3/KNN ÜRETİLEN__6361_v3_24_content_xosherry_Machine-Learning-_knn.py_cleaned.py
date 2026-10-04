import sys
import math
from collections import defaultdict
def euclidean_distance(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))
def knn(k, training_file, testing_file):
    def load_data(file_path):
        with open(file_path, 'r') as file:
            total, dimensions = map(int, file.readline().split())
            points = [line.split() for line in file]
            return total, dimensions, points
    def convert_points(points, dimensions):
        for point in points:
            for d in range(dimensions):
                point[d] = float(point[d])
            point[dimensions] = int(point[dimensions]) if len(point) > dimensions else None
        return points
    train_total, train_dimensions, training_points = load_data(training_file)
    test_total, test_dimensions, testing_points = load_data(testing_file)
    training_points = convert_points(training_points, train_dimensions)
    testing_points = convert_points(testing_points, test_dimensions)
    for test_point in testing_points:
        distances = []
        for train_point in training_points:
            label = train_point[-1]
            train_coords = train_point[:-1]
            distance = euclidean_distance(train_coords, test_point)
            distances.append((distance, label))
        distances.sort()
        k_nearest = distances[:k]
        class_votes = defaultdict(int)
        for _, label in k_nearest:
            class_votes[label] += 1
        max_votes = max(class_votes.values())
        most_popular_classes = [label for label, votes in class_votes.items() if votes == max_votes]
        if len(most_popular_classes) == 1:
            test_point.append(most_popular_classes[0])
        else:
            k_nearest_filtered = [x for x in k_nearest if x[1] in most_popular_classes]
            k_nearest_filtered.sort()
            test_point.append(k_nearest_filtered[0][1])
    for count, item in enumerate(testing_points, 1):
        formatted_coords = ' '.join(f"{x:.1f}" for x in item[:-1])
        print(f"{count}. {formatted_coords} -- {item[-1]}")
