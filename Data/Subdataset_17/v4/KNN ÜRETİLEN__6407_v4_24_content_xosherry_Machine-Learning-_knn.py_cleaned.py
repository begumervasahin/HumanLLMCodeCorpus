import sys
import math
import itertools
def euclidean_distance(trained_point, test_point):
    sum_sq = sum((trained_point[i] - test_point[i]) ** 2 for i in range(len(trained_point)))
    return math.sqrt(sum_sq)
def knn(k, training_file, testing_file):
    with open(training_file, 'r') as trainfile:
        train_total, train_dimensions = map(int, trainfile.readline().split())
        training_points = [line.split() for line in trainfile]
    with open(testing_file, 'r') as testfile:
        test_total, test_dimensions = map(int, testfile.readline().split())
        testing_points = [line.split() for line in testfile]
    for point in training_points:
        for d in range(train_dimensions):
            point[d] = float(point[d])
        point[train_dimensions] = int(point[train_dimensions])
    for point in testing_points:
        for d in range(test_dimensions):
            point[d] = float(point[d])
    classes_count = {point[-1]: 0 for point in training_points}
    for test_point in testing_points:
        distances = [
            [euclidean_distance(train_point[:-1], test_point), train_point[-1]]
            for train_point in training_points
        ]
        distances.sort()
        k_nearest = distances[:k]
        for neighbor in k_nearest:
            label = neighbor[-1]
            classes_count[label] += 1
        most_frequent_class = max(classes_count, key=classes_count.get)
        most_frequent_count = classes_count[most_frequent_class]
        tied_classes = [
            key for key, value in classes_count.items() if value == most_frequent_count
        ]
        if len(tied_classes) == 1:
            test_point.append(most_frequent_class)
        else:
            tied_distances = [
                dist for dist in distances if dist[-1] in tied_classes
            ]
            tied_distances.sort()
            test_point.append(tied_distances[0][1])
        classes_count = {key: 0 for key in classes_count}
    for idx, item in enumerate(testing_points, start=1):
        formatted_point = ' '.join(f"{x:.1f}" for x in item[:-1])
        print(f"{idx}. {formatted_point} -- {item[-1]}")
if __name__ == "__main__":
    knn(int(sys.argv[1]), sys.argv[2], sys.argv[3])